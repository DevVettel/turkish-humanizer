#!/usr/bin/env python3
"""tara.py: Türkçe bir metinde katalogdaki örüntüleri sayar, istenirse
yeniden yazılmış metni kaynağıyla karşılaştırır.

Bu bir "yapay zeka dedektörü" değildir. Metni kimin yazdığı hakkında hiçbir
şey söylemez. Yalnızca `references/ai-oruntuleri.md` kataloğundaki, düz
metinden sayılabilen örüntüleri ve cümle uzunluğu dağılımını raporlar.
Bulgular birer adaydır: Her örüntünün katalogdaki "Dokunma" satırı geçerlidir.

Kullanım:
    python3 tara.py metin.md
    python3 tara.py metin.md --register akademik
    python3 tara.py yeni.md --kaynak eski.md      # sayı, ad, temkin korunmuş mu?
    cat metin.md | python3 tara.py - --json

Yalnızca standart kitaplığı kullanır (Python 3.8+).
"""
import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

REGISTERLAR = ("gundelik", "is", "akademik")

# ---------------------------------------------------------------- metin hazırlığı


def kucult(metin):
    """Türkçe küçük harfe çevirir. Uzunluk değişmez, konumlar kaynakla aynı kalır."""
    return metin.replace("İ", "i").replace("I", "ı").lower()


def _bosalt(eslesme):
    # Satır sonlarını koruyarak boşlukla doldurur: satır numaraları kaymaz.
    return re.sub(r"[^\n]", " ", eslesme.group(0))


KOD_BLOGU = re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.S | re.M)
SATIR_ICI_KOD = re.compile(r"`[^`\n]+`")
HTML_YORUM = re.compile(r"<!--.*?-->", re.S)
ADRES = re.compile(r"https?://[^\s)>\]]+|\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
BAGLANTI_HEDEFI = re.compile(r"(?<=\])\([^)\n]*\)")


def kodsuz(metin):
    """Kod, yorum ve adresleri boşlukla örter. Bunlar üslup taramasına girmez."""
    for desen in (KOD_BLOGU, HTML_YORUM, SATIR_ICI_KOD, BAGLANTI_HEDEFI, ADRES):
        metin = desen.sub(_bosalt, metin)
    return metin


BASLIK = re.compile(r"^\s{0,3}#{1,6}\s.*$", re.M)
TABLO = re.compile(r"^\s*\|.*$", re.M)
ISARET = re.compile(r"^\s*(?:>\s?)*(?:[-*+•]\s+|\d+[.)]\s+)?", re.M)
VURGU = re.compile(r"\*\*|__|(?<!\w)[*_](?=\w)|(?<=\w)[*_](?!\w)")


def duzyazi(metin):
    """Cümle ölçümü için: başlık, tablo, liste ve alıntı işaretleri çıkarılır."""
    metin = TABLO.sub(_bosalt, BASLIK.sub(_bosalt, metin))
    return VURGU.sub("", ISARET.sub("", metin))


KISALTMA = re.compile(
    r"(?:\b(?:dr|prof|doç|av|sn|vb|vs|vd|bkz|örn|yy|no|tel|mah|cad|sok|apt|ltd|şti|a\.ş)|\b[A-ZÇĞİÖŞÜ])\.$",
    re.I,
)
CUMLE_SINIRI = re.compile(r"(?<=[.!?…])[\"”’)]*\s+(?=[\"“‘(]?[A-ZÇĞİÖŞÜ0-9])")


def cumleler(paragraf):
    parcalar, biriken = [], ""
    for parca in CUMLE_SINIRI.split(paragraf.strip()):
        biriken = (biriken + " " + parca).strip() if biriken else parca.strip()
        if KISALTMA.search(biriken):
            continue
        if biriken:
            parcalar.append(biriken)
        biriken = ""
    if biriken:
        parcalar.append(biriken)
    return [c for c in parcalar if re.search(r"\w", c)]


def paragraflar(metin):
    return [p for p in re.split(r"\n\s*\n", metin) if re.search(r"\w", p)]


def sozcuk_sayisi(cumle):
    return len(re.findall(r"[^\W_]+(?:['’][^\W_]+)?", cumle))


# ---------------------------------------------------------------- kurallar

# (kimlik, ad, desen, akademik/resmî metinde olağan mı)
# Desenler küçük harfe çevrilmiş metin üzerinde çalışır.
SOZLUK_KURALLARI = [
    ("YAPI-04", "Gereksiz edilgen yapı",
     r"\btaraf[ıi]m[ıi]zca\b|\btaraf[ıi]m[ıi]zdan\b|\b(?:ekibimiz|şirketimiz|firmamız|kurumumuz) tarafından\b", True),
    ("YAPI-06", "\"Sadece X değil, aynı zamanda Y\" kalıbı",
     r"\b(?:sadece|yalnızca|yalnız)\b[^.!?\n]{1,80}?\bdeğil,?\s+(?:aynı zamanda|ayrıca)\b"
     r"|\bolmakla kalm[ıa]\w*|\bolmanın (?:çok )?ötesinde\b", False),
    ("YAPI-07", "Kendi sorup kendi cevaplama",
     r"(?:^|(?<=[.!?…]\s))peki[, ][^.!?\n]{0,90}\?|\bsonuç mu\?|\bcevap mı\?|\bişin sırrı mı\?", False),
    ("YAPI-08", "Özet cümlesiyle kapanış",
     r"\bbu da (?:açıkça )?göster(?:iyor|mektedir|ir) ki\b|\bkısacası\b|\bözetle(?:mek gerekirse)?\b"
     r"|\btoparlamak gerekirse\b|\bson tahlilde\b|\bbunu bir kez daha okuyun\b|\büzerinde düşünmeye değer\b"
     r"|(?:^|(?<=[.!?…]\s))ne [^.!?\n]{1,30}\.\s+ne [^.!?\n]{1,30}\.", False),
    ("YAPI-10", "Kimseyle tartışma",
     r"\byanlış anlaşılmasın\b|\bşunu (?:söylemiyorum|demiyorum)\b|\b(?:demek|söylemek) istemiyorum\b"
     r"|\bkimileri [^.!?\n]{1,80}?diyebilir\b|\bakla ilk gelen (?:çözüm|yöntem|yol|seçenek)\w*"
     r"|\bdiyenler (?:çıkacaktır|olabilir|çıkabilir)\b", False),
    ("SOZ-01", "\"Önemli bir rol oynamaktadır\" ailesi",
     r"\b(?:önemli|kritik|büyük|kilit|hayati|merkezi|belirleyici) (?:bir )?rol (?:oyna|üstlen)\w*"
     r"|\b(?:büyük|hayati|kritik) (?:bir )?önem (?:taşı|arz et)\w*"
     r"|\b(?:kritik|hayati|büyük) (?:bir )?öneme sahip\w*"
     r"|\bvazgeçilmez (?:bir )?(?:unsur|parça)\w*|\bayrılmaz (?:bir )?parça\w*", False),
    ("SOZ-02", "Geçiş ve bağlam klişeleri",
     r"\bbu (?:bağlamda|çerçevede|doğrultuda|kapsamda)\b|\bsöz konusu\b"
     r"|\bgöz önünde bulundurulduğunda\b|\bdikkate alındığında\b|\bsonuç olarak\b", True),
    ("SOZ-02", "Geçiş ve bağlam klişeleri",
     r"\bgünümüz(?:de|ün)\b|\bhızla (?:gelişen|değişen|ilerleyen|dijitalleşen)\b"
     r"|\bhızla (?:geliştiği|değiştiği|ilerlediği) günümüz\w*|\bçağımızda\b", False),
    ("SOZ-03", "Pekiştirme şişirmesi",
     r"\bson derece\b|\bbüyük ölçüde\b|\beşsiz\b|\bbenzersiz\b|\bmuazzam\b|\binanılmaz\b"
     r"|\bdevrim niteliğinde\b|\bçığır açan\b|\byadsınamaz\b|\bkusursuz\b", False),
    ("SOZ-04", "\"olarak\" ve \"-mekte olup\" fazlalığı",
     r"\b(?:şirket|ekip|kurum|firma|genel|temel|aktif) olarak\b|\w+m[ae]kte olup\b|\w+m[ıiuü]ş olup\b", False),
    ("SOZ-06", "Gösterişli mecaz öbekleri",
     r"\byeni bir boyut kazan\w*|\bkapı(?:lar)?ını arala\w*|\bdönüşüm yolculu\w+|\byolculuğa çık\w*"
     r"|\byeni bir sayfa aç\w*|\bufuk açıcı\b|\bçıtayı yüksel\w*|\bpotansiyelini (?:açığa|ortaya) çıkar\w*"
     r"|\bbir (?:üst|sonraki) seviyeye taşı\w*|\bgeniş (?:bir )?yelpaze\w*", False),
    ("SOZ-08", "Derin görünen vecize",
     r"\bmeselenin özü\w*|\basıl soru(?:,| şu)\b|\basıl mesele\b|\bişin özü(?:nde)?\b|\byeni petrol\w*", False),
    ("SOZ-09", "Kaynaksız otorite",
     r"\buzmanlara göre\b|\buzmanlar\w*,? [^.!?\n]{0,60}?hemfikir\w*|\baraştırmalar(?:ın)? göster(?:iyor|mektedir|di) ki\b"
     r"|\b(?:pek çok|birçok|sayısız) (?:araştırma|çalışma)\w* [^.!?\n]{0,40}?(?:ortaya koy|göster)\w*"
     r"|\bbilim insanları uyarıyor\b", True),
    ("SOZ-07", "Adlaştırma zinciri ve boş yardımcı fiil",
     r"\w+m[ae]s[ıi]n[ıi]n sağlanması\b|\w+m[ae]s[ıi] (?:gerekmektedir|sağlanmalıdır|gerçekleştirilmiştir)"
     r"|\b(?:gerçekleştirilm|icra edilm)\w*|\bgerçekleştirm\w*", False),
    ("CEV-01", "Çeviri deyimler",
     r"\bgünün sonunda\b|\bderinlemesine (?:dal|in)\w*|\boyunun kurallarını değiştir\w*|\bmasaya getir\w*"
     r"|\baynı sayfada ol\w*|\bkutunun dışında\b|\bkazan-kazan\b|\bbuzdağının görünen\b|\bbüyük resm\w+", False),
    ("CEV-02", "\"-e sahip olmak\" fazlalığı",
     r"\b\w+[ae] sahip(?:tir| olup| olan| olmak| olduğu\w*)?\b", False),
    ("CEV-05", "\"bir şekilde\" zarfları",
     r"\b\w+ bir (?:şekilde|biçimde)\b", False),
    ("NOK-01", "Cümle içinde uzun çizgi (—)", r"(?<=\S)[^\S\n]*—", False),
    ("NOK-02", "\"ve\"den önce virgül", r",\s+(?:ve|veya|ya da|yahut)\b", False),
    ("NOK-03", "İngilizce sayı ve yüzde biçimi", r"\b\d+(?:[.,]\d+)?\s?%(?!\w)", False),
    ("DOL-01", "Açılış dolguları",
     r"\bharika bir soru\b|\bçok güzel bir soru\b|\bbu e-posta sizi iyi bul\w*"
     r"|\bbu (?:yazıda|makalede|rehberde)\b[^.!?\n]{0,80}?\b(?:ele alacağız|inceleyeceğiz|göz atacağız|keşfedeceğiz)"
     r"|^(?:elbette|tabii ki|kesinlikle)[!,]|\bgelin (?:birlikte )?(?:bakalım|inceleyelim|göz atalım)\b"
     r"|\bhadi başlayalım\b|\blafı uzatmadan\b|\bişin aslı şu\b|\baçık konuşalım\b"
     r"|\bbilmeniz gerekenler şunlar\b|\bişte işin püf noktası\b", False),
    ("DOL-02", "Kapanış dolguları",
     r"\bumarım (?:bu )?[^.!?\n]{0,40}?yardımcı ol\w*|\bçekinmeyin\b|\bçekinmeden sor\w*"
     r"|\bbaşka (?:bir )?soru(?:nuz|n) olursa\b|\bunutmayın[, ]", False),
    ("DOL-03", "Model notu: bilgi sınırı ve tahmin",
     r"\bbilgi kesim tarih\w*|\beğitim verilerim\w*|\berişebildiğim (?:kaynak|bilgi)\w*|\bmevcut bilgilere göre\b"
     r"|\bkamuya açık [^.!?\n]{0,40}?bilgi bulun(?:ma|mu)\w*|\bsınırlı bilgi bulunmaktadır\b", False),
    ("BIC-04", "Metnin kendini anlatması",
     r"\başağıdaki tablo\w* [^.!?\n]{0,60}?(?:karşılaştırmaktadır|göstermektedir|özetlemektedir|sunmaktadır)"
     r"|\bbu bölüm(?:de)? [^.!?\n]{0,60}?(?:ele alınmaktadır|düzenlenmiştir|karşılaştırılmaktadır)"
     r"|\bderlenmiş olup\b|\bdoğrulanamayan bilgiler işaretlenmiştir\b", True),
    ("YAZ-01", "Bağlaç de/da", r"\b(?:bende|sende|bizde|sizde) (?:gel|gid|bil|iste|düşün|katıl|yap)\w*", False),
    ("YAZ-02", "ki", r"\bdemekki\b|\bhalbuki\b|\b(?:yarın|bugün|dün|masada|evde|burada|orada) ki\b", False),
    ("YAZ-06", "Sık yazım hataları",
     r"\bbirşey\w*|\bherşey\w*|\bhiç bir\b|\bbir çok\b|\bbir kaç\b|\bpekçok\b|\byada\b|\byanlız\w*|\bherkez\b", False),
]

# Satır başına bakan, ham metin (biçim işaretleri duruyorken) üzerinde çalışan kurallar.
BICIM_KURALLARI = [
    ("BIC-02", "Kalın etiketli madde", r"^\s*(?:[-*+•]|\d+[.)])\s+\*\*[^*\n]{1,40}:\*\*|^\s*(?:[-*+•]|\d+[.)])\s+\*\*[^*\n]{1,40}\*\*:"),
]

# Cümle sonundaki ayraçlı not ("... göstermektedir (p<0,05).") yüklemi gizlemesin.
MEKTEDIR = re.compile(r"m[ae]kt[ae](?:d[ıi]r(?:l[ae]r)?|y[ıi]z|y[ıi]m|s[ıi]n[ıi]z)(?:\s*\([^()]*\))?[\"”’)]*[.!?…]*$")
BU_ACILISI = re.compile(r"^bu (?:durum\w*|da|sayede|noktada|nedenle|yüzden)\b")
UCLU = re.compile(r"\b[^\W\d_]+, [^\W\d_]+ ve [^\W\d_]+\b")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆✅]")
TEKEL = {"ve": 3, "ama": 2, "çünkü": 2}
LISTE_SATIRI = re.compile(r"^\s*(?:[-*+•]|\d+[.)])\s+", re.M)


def _satir(metin, konum):
    return metin.count("\n", 0, konum) + 1


def _kesit(metin, bas, son, pay=28):
    a, b = max(0, bas - pay), min(len(metin), son + pay)
    parca = re.sub(r"\s+", " ", metin[a:b]).strip()
    return ("…" if a > 0 else "") + parca + ("…" if b < len(metin) else "")


class Rapor:
    def __init__(self):
        self.bulgular = {}

    def ekle(self, kimlik, ad, satir, kesit, olagan=False):
        # Aynı örüntünün olağan sayılan ve sayılmayan yerleri ayrı tutulur.
        kayit = self.bulgular.setdefault((kimlik, olagan), {"kimlik": kimlik, "ad": ad, "olagan": olagan, "yerler": []})
        kayit["yerler"].append({"satir": satir, "kesit": kesit})

    def liste(self):
        return [dict(k, sayi=len(k["yerler"])) for _, k in sorted(self.bulgular.items())]


def ritim(metin):
    """Cümle uzunluğu dağılımı. YAPI-01 için sayısal dayanak."""
    uzunluklar = [sozcuk_sayisi(c) for p in paragraflar(duzyazi(metin)) for c in cumleler(p)]
    uzunluklar = [u for u in uzunluklar if u > 0]
    sonuc = {"cumle": len(uzunluklar), "sozcuk": sum(uzunluklar)}
    if len(uzunluklar) >= 2:
        ort = statistics.mean(uzunluklar)
        sonuc.update(
            ortalama=round(ort, 1),
            en_kisa=min(uzunluklar),
            en_uzun=max(uzunluklar),
            # Değişim katsayısı: standart sapma / ortalama. Düşükse cümleler birbirine yakın.
            degisim=round(statistics.pstdev(uzunluklar) / ort, 2) if ort else 0.0,
            # Katalogdaki "güvenli orta" bant: 14-22 sözcük.
            orta_bant=round(sum(14 <= u <= 22 for u in uzunluklar) / len(uzunluklar), 2),
        )
    return sonuc


def tara(metin, register="gundelik"):
    """Metni tarar, {"ritim": ..., "bulgular": [...]} döndürür."""
    resmi = register == "akademik"
    rapor = Rapor()
    temiz = kodsuz(metin)
    kucuk = kucult(temiz)

    for kimlik, ad, desen, resmide_olagan in SOZLUK_KURALLARI:
        for e in re.finditer(desen, kucuk, re.M):
            rapor.ekle(kimlik, ad, _satir(temiz, e.start()), _kesit(temiz, e.start(), e.end()),
                       olagan=resmi and resmide_olagan)
    for kimlik, ad, desen in BICIM_KURALLARI:
        for e in re.finditer(desen, temiz, re.M):
            rapor.ekle(kimlik, ad, _satir(temiz, e.start()), _kesit(temiz, e.start(), e.end(), pay=0))

    # Paragraf ve cümle düzeyindeki sayımlar düzyazı üzerinde yapılır.
    duz = duzyazi(temiz)
    konum = 0
    for paragraf in re.split(r"(\n\s*\n)", duz):
        bas, konum = konum, konum + len(paragraf)
        if not re.search(r"\w", paragraf):
            continue
        satir = _satir(duz, bas + len(paragraf) - len(paragraf.lstrip()))
        p_kucuk = kucult(paragraf)
        cumle_listesi = cumleler(paragraf)

        sozcukler = Counter(re.findall(r"[^\W\d_]+", p_kucuk))
        asan = [f"{s} ×{sozcukler[s]}" for s, sinir in TEKEL.items() if sozcukler[s] > sinir]
        if asan:
            rapor.ekle("YAPI-02", "ve/ama/çünkü tekeli", satir, "Bu paragrafta: " + ", ".join(asan))

        ekli = [c for c in cumle_listesi if MEKTEDIR.search(kucult(c))]
        if len(ekli) >= 2:
            # Akademik ve resmî metinde ek olağandır, iz olan yığılmadır.
            yigilma = len(ekli) >= 3 and len(ekli) / len(cumle_listesi) >= 0.5
            rapor.ekle("YAPI-03", "-mektedir/-maktadır yığılması", satir,
                       f"{len(cumle_listesi)} cümleden {len(ekli)}'i bu ekle bitiyor",
                       olagan=resmi and not yigilma)

        bu_ile = [c for c in cumle_listesi if BU_ACILISI.match(kucult(c))]
        if len(bu_ile) >= 2:
            rapor.ekle("SOZ-05", "\"Bu durum\" / \"Bu da\" ile açılış", satir,
                       f"{len(bu_ile)} cümle böyle başlıyor: " + " / ".join(" ".join(c.split()[:3]) + "…" for c in bu_ile[:3]))

        if p_kucuk.count("tarafından") >= 2:
            rapor.ekle("CEV-03", "\"tarafından\" ve \"için\" yığılması", satir,
                       f"Bu paragrafta \"tarafından\" ×{p_kucuk.count('tarafından')}", olagan=resmi)

    # YAPI-11: Liste içermeyen paragraflarda aynı sözcükle başlayan cümleler.
    konum = 0
    for paragraf in re.split(r"(\n\s*\n)", temiz):
        bas, konum = konum, konum + len(paragraf)
        if not re.search(r"\w", paragraf) or LISTE_SATIRI.search(paragraf) or BASLIK.search(paragraf):
            continue
        ilkler = Counter()
        for c in cumleler(duzyazi(paragraf)):
            ilk = re.match(r"[^\W\d_]+", kucult(c))
            if ilk and ilk.group(0) not in ("bu", "ve"):
                ilkler[ilk.group(0)] += 1
        tekrar = [f"\"{s}\" ×{n}" for s, n in ilkler.items() if n >= 3]
        if tekrar:
            rapor.ekle("YAPI-11", "Aynı sözcükle başlayan cümleler",
                       _satir(temiz, bas + len(paragraf) - len(paragraf.lstrip())),
                       "Bu paragrafta cümle başı: " + ", ".join(tekrar))

    # BIC-03: Başlığın altındaki ilk cümle başlığı tekrar ediyor.
    for e in BASLIK.finditer(temiz):
        baslik = re.findall(r"[^\W\d_]+", kucult(e.group(0)))
        sonrasi = temiz[e.end():].lstrip()
        if not baslik or not sonrasi or sonrasi.startswith("#"):
            continue
        ilk_paragraf = re.split(r"\n\s*\n|\n(?=\s{0,3}#)", sonrasi, maxsplit=1)[0]
        cumle_listesi = cumleler(duzyazi(ilk_paragraf).replace("\n", " "))
        if not cumle_listesi:
            continue
        ilk = cumle_listesi[0]
        kok = baslik[0][:max(4, len(baslik[0]) - 2)]
        devam = len(cumle_listesi) > 1 or len(sonrasi.strip()) > len(ilk_paragraf.strip())
        # "Güvenlik, her sistemin en önemli parçasıdır." gibi: başlık sözcüğü, virgül, -dır'lı yargı.
        tanim = re.match(re.escape(kok) + r"[^\W\d_]*,\s.*(?:d|t)[ıiuü]r\.$", kucult(ilk))
        if devam and tanim and sozcuk_sayisi(ilk) <= 12:
            rapor.ekle("BIC-03", "Başlığı ilk cümlede tekrarlama", _satir(temiz, e.start()),
                       e.group(0).strip() + " → " + ilk)

    uclular = list(UCLU.finditer(kucult(duz)))
    if len(uclular) >= 2:
        for e in uclular:
            rapor.ekle("YAPI-05", "Üçlü sıralama alışkanlığı", _satir(duz, e.start()), duz[e.start():e.end()])

    unlem, emoji = temiz.count("!"), len(EMOJI.findall(temiz))
    if unlem > 2 or emoji > 1:
        rapor.ekle("NOK-04", "Ünlem ve emoji bolluğu", 1, f"{unlem} ünlem, {emoji} emoji")

    r = ritim(temiz)
    if r["cumle"] >= 5 and (r["orta_bant"] >= 0.7 or r["degisim"] < 0.3):
        rapor.ekle("YAPI-01", "Tekdüze dizilim ve eşit cümle uzunluğu", 1,
                   f"{r['cumle']} cümlenin %{round(r['orta_bant'] * 100)}'i 14-22 sözcük arasında, "
                   f"değişim katsayısı {str(r['degisim']).replace('.', ',')}")
    return {"register": register, "ritim": r, "bulgular": rapor.liste()}


# ---------------------------------------------------------------- kaynakla karşılaştırma

SAYI = re.compile(r"\d+(?:[.,:]\d+)*")
OZEL_AD = re.compile(r"(?<![.!?…:]\s)(?<!^)(?<!\n)\b[A-ZÇĞİÖŞÜ][\w.-]*[^\W_]")
TEMKIN = re.compile(
    r"\w+[ae]bil(?:ir|iyor|ecek|mekte|diği|eceği)\w*|\bmuhtemelen\b|\bgaliba\b|\bsanırım\b|\bbelki\b"
    r"|\bgörünüyor\b|\bgörünmektedir\b|\bişaret et\w*|\böne sür\w*|\bbazı\b|\bkimi\b|\bçoğu zaman\b"
    r"|\bgenellikle\b|\byaklaşık\b|\bolası\b"
)


def _sayilar(metin):
    # Biçim farkı (25% / %25, 3.5 / 3,5, 14:30 / 14.30) değer farkı sayılmaz.
    return Counter(re.sub(r"[.,:]", "", s) for s in SAYI.findall(metin))


def karsilastir(kaynak, yeni):
    """Yeniden yazılmış metinde kaynaktaki sayı, adres, özel ad ve temkinleri arar."""
    k_sayi, y_sayi = _sayilar(kodsuz(kaynak)), _sayilar(kodsuz(yeni))
    sonuc = {
        "eksik_sayilar": sorted(set(k_sayi) - set(y_sayi)),
        "yeni_sayilar": sorted(set(y_sayi) - set(k_sayi)),
        "eksik_adresler": sorted(set(ADRES.findall(kaynak)) - set(ADRES.findall(yeni))),
    }
    eksik_adlar = []
    for ad in dict.fromkeys(OZEL_AD.findall(duzyazi(kodsuz(kaynak)))):
        # Ek ve kesme değişebilir ("Üniversitesi'ne" → "Üniversitesine"): köke bakılır.
        kok = ad if len(ad) < 6 else ad[:-2]
        if kok not in yeni and kucult(kok) not in kucult(yeni):
            eksik_adlar.append(ad)
    sonuc["eksik_adlar"] = eksik_adlar
    k_temkin = len(TEMKIN.findall(kucult(kaynak)))
    y_temkin = len(TEMKIN.findall(kucult(yeni)))
    sonuc["temkin"] = {"kaynak": k_temkin, "yeni": y_temkin}
    sonuc["temiz"] = not (sonuc["eksik_sayilar"] or sonuc["yeni_sayilar"] or sonuc["eksik_adresler"]
                          or eksik_adlar or y_temkin < k_temkin)
    return sonuc


# ---------------------------------------------------------------- çıktı


def yazdir(sonuc, karsilastirma=None, cikti=sys.stdout):
    p = lambda *a: print(*a, file=cikti)  # noqa: E731
    r = sonuc["ritim"]
    p(f"Register: {sonuc['register']} · {r['cumle']} cümle, {r['sozcuk']} sözcük")
    if "ortalama" in r:
        p(f"Cümle uzunluğu: ortalama {r['ortalama']}, en kısa {r['en_kisa']}, en uzun {r['en_uzun']}, "
          f"değişim katsayısı {r['degisim']}, 14-22 bandında %{round(r['orta_bant'] * 100)}")
    izler = [b for b in sonuc["bulgular"] if not b["olagan"]]
    olaganlar = [b for b in sonuc["bulgular"] if b["olagan"]]
    p()
    if not izler:
        p("Katalogdaki sayılabilir örüntülerden hiçbiri bulunmadı.")
    for b in izler:
        p(f"{b['kimlik']} · {b['ad']} ({b['sayi']})")
        for yer in b["yerler"][:3]:
            p(f"    satır {yer['satir']}: {yer['kesit']}")
        if b["sayi"] > 3:
            p(f"    … ve {b['sayi'] - 3} yer daha")
    if olaganlar:
        p()
        p("Bu registerda olağan (bilgi için, dokunmak gerekmeyebilir):")
        for b in olaganlar:
            p(f"    {b['kimlik']} · {b['ad']} ({b['sayi']})")
    if karsilastirma is not None:
        k = karsilastirma
        p()
        p("Kaynakla karşılaştırma")
        etiketler = [
            ("eksik_sayilar", "Kaynakta olup yeni metinde olmayan sayılar"),
            ("yeni_sayilar", "Kaynakta olmayıp yeni metinde olan sayılar"),
            ("eksik_adresler", "Eksik URL ya da e-posta adresi"),
            ("eksik_adlar", "Yeni metinde bulunamayan özel adlar"),
        ]
        for anahtar, etiket in etiketler:
            if k[anahtar]:
                p(f"    ! {etiket}: {', '.join(k[anahtar])}")
        t = k["temkin"]
        if t["yeni"] < t["kaynak"]:
            p(f"    ! Temkin bildiren ifade azalmış ({t['kaynak']} → {t['yeni']}). "
              "\"-ebilir\", \"bazı\", \"muhtemelen\" gibi sözlerin korunduğunu denetleyin.")
        if k["temiz"]:
            p("    Sayılar, adresler, özel adlar ve temkin ifadeleri yerinde görünüyor.")
        p("    (Bu denetim sözcük düzeyindedir. Anlamı okuyarak da karşılaştırın.)")


def _oku(yol):
    return sys.stdin.read() if yol == "-" else Path(yol).read_text(encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Türkçe metinde katalogdaki örüntüleri sayar.")
    ap.add_argument("dosya", help="taranacak metin dosyası, standart girdi için '-'")
    ap.add_argument("--register", choices=REGISTERLAR, default="gundelik",
                    help="gundelik: blog/sosyal, is: e-posta/ürün metni, akademik: akademik/resmî (varsayılan: gundelik)")
    ap.add_argument("--kaynak", metavar="DOSYA",
                    help="yeniden yazımın kaynağı: sayı, adres, özel ad ve temkin ifadeleri karşılaştırılır")
    ap.add_argument("--json", action="store_true", help="JSON çıktısı")
    a = ap.parse_args(argv)
    try:
        metin = _oku(a.dosya)
        kaynak = _oku(a.kaynak) if a.kaynak else None
    except OSError as hata:
        print(f"Dosya okunamadı: {hata}", file=sys.stderr)
        return 2
    sonuc = tara(metin, a.register)
    karsilastirma = karsilastir(kaynak, metin) if kaynak is not None else None
    if a.json:
        if karsilastirma is not None:
            sonuc["karsilastirma"] = karsilastirma
        json.dump(sonuc, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        yazdir(sonuc, karsilastirma)
    return 0


if __name__ == "__main__":
    sys.exit(main())
