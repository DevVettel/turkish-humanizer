"""tara.py için testler. Çalıştırmak için: python3 -m unittest discover -s tests"""
import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "turkish-humanizer" / "scripts"))

import tara  # noqa: E402


def kimlikler(metin, register="gundelik", olagan=False):
    return {b["kimlik"] for b in tara.tara(metin, register)["bulgular"] if b["olagan"] == olagan}


class Hazirlik(unittest.TestCase):
    def test_kucult_turkce_harfleri_ve_uzunlugu_korur(self):
        self.assertEqual(tara.kucult("IŞIK İÇİN"), "ışık için")
        self.assertEqual(len(tara.kucult("İİİ")), 3)

    def test_kisaltma_cumleyi_bolmez(self):
        self.assertEqual(len(tara.cumleler("Dr. Aylin Hanım geldi. Toplantı başladı.")), 2)

    def test_saat_cumleyi_bolmez(self):
        self.assertEqual(len(tara.cumleler("Kesinti 02.15'te başladı. 04.40'ta bitti.")), 2)

    def test_kod_ve_adres_taranmaz(self):
        metin = "Komut:\n\n```\necho 'a — b, ve c'\n```\n\nAyrıntı için `x — y` ve https://ornek.example/a—b adresine bakın."
        self.assertEqual(kimlikler(metin), set())


class Kurallar(unittest.TestCase):
    def test_uzun_cizgi_cumle_icinde_yakalanir(self):
        self.assertIn("NOK-01", kimlikler("Tek bir konu konuşuldu — bütçe."))

    def test_diyalog_cizgisi_yakalanmaz(self):
        self.assertNotIn("NOK-01", kimlikler("— Geldin mi?\n— Geldim."))

    def test_veden_once_virgul(self):
        self.assertIn("NOK-02", kimlikler("Tasarım, geliştirme, ve test bitti."))
        self.assertNotIn("NOK-02", kimlikler("Tasarım, geliştirme ve test bitti."))

    def test_yuzde_bicimi(self):
        self.assertIn("NOK-03", kimlikler("Satışlar 12.5% arttı."))
        self.assertNotIn("NOK-03", kimlikler("Satışlar %12,5 arttı."))

    def test_sozluk_oruntuleri(self):
        ornekler = {
            "SOZ-01": "Uyku, başarıda önemli bir rol oynamaktadır.",
            "SOZ-03": "Bu son derece yararlı bir araç.",
            "SOZ-07": "Verilerin yedeklenmesinin sağlanması gerekmektedir.",
            "CEV-01": "Günün sonunda karar sizin.",
            "CEV-02": "Ekibimiz geniş bir deneyime sahip.",
            "CEV-05": "Dosyaları hızlı bir şekilde paylaşın.",
            "YAPI-06": "Bu sadece bir not defteri değil, aynı zamanda bir asistan.",
            "YAPI-07": "Peki bu ne anlama geliyor? Daha hızlı bir uygulama.",
            "DOL-01": "Umarım bu e-posta sizi iyi bulur.",
            "DOL-02": "Sorunuz olursa sormaktan çekinmeyin.",
            "YAZ-06": "Herşey yolunda.",
            "YAPI-10": "Yanlış anlaşılmasın, toplantılara karşı değilim.",
            "SOZ-08": "Meselenin özünde kurum kültürü yatıyor.",
            "SOZ-09": "Uzmanlara göre ekran süresi dikkati etkiliyor.",
            "DOL-03": "Bilgi kesim tarihim itibarıyla şirket hakkında bilgi yok.",
            "BIC-04": "Aşağıdaki tablo üç paketi karşılaştırmaktadır.",
        }
        for kimlik, metin in ornekler.items():
            with self.subTest(kimlik=kimlik):
                self.assertIn(kimlik, kimlikler(metin))

    def test_sahneli_giris(self):
        for metin in ("Lafı uzatmadan konuya girelim.", "İşin aslı şu: önbellek üç katmanlı.",
                      "Gelin birlikte bakalım."):
            with self.subTest(metin=metin):
                self.assertIn("DOL-01", kimlikler(metin))

    def test_kesik_parca_zinciri(self):
        self.assertIn("YAPI-08", kimlikler("Yeni sistem geldi. Ne bekleme kaldı. Ne kuyruk. Ne de evrak."))

    def test_ne_sorusu_kesik_parca_sayilmaz(self):
        self.assertNotIn("YAPI-08", kimlikler("Ne zaman geliyorsun? Ne getireceksin?"))

    def test_ayni_sozcukle_baslayan_cumleler(self):
        metin = ("Ekibimiz depoyu mart ayında açtı. Ekibimiz teslim süresini kısalttı. "
                 "Ekibimiz şimdi iade sürecini yeniliyor.")
        self.assertIn("YAPI-11", kimlikler(metin))

    def test_liste_maddeleri_ayni_baslangic_sayilmaz(self):
        metin = "- Kullanıcı giriş yapar.\n- Kullanıcı formu doldurur.\n- Kullanıcı gönderir."
        self.assertNotIn("YAPI-11", kimlikler(metin))

    def test_basligi_tekrarlayan_ilk_cumle(self):
        metin = "## Güvenlik\n\nGüvenlik, her sistemin en önemli parçasıdır. Veriler şifrelenir.\n"
        self.assertIn("BIC-03", kimlikler(metin))

    def test_baslik_sozcuguyle_baslayan_bilgi_cumlesi_sayilmaz(self):
        metin = "## ChatGPT\n\nChatGPT, skill dosyalarını doğrudan yükleyemez. Talimat kutusunu kullanın.\n"
        self.assertNotIn("BIC-03", kimlikler(metin))

    def test_kaynakli_atif_akademikte_olagan(self):
        metin = "Yapılan pek çok çalışma bu etkiyi ortaya koymuştur (Kaya, 2019)."
        self.assertIn("SOZ-09", kimlikler(metin, "akademik", olagan=True))

    def test_buyuk_harfle_baslayan_kalip_da_yakalanir(self):
        self.assertIn("SOZ-02", kimlikler("İşler yolunda. Bu Bağlamda yeni bir plan yaptık."))

    def test_temiz_metin_bulgu_uretmez(self):
        metin = ("2015'te İzmir'de kurulduk. Yazılım geliştirmede uzmanlaşmış ekibimizle müşterilerimize "
                 "uçtan uca çözümler sunuyoruz. Projelerde çevik yöntemlerle çalışıyoruz.")
        self.assertEqual(kimlikler(metin), set())

    def test_baglac_tekeli_paragraf_basina_sayilir(self):
        self.assertIn("YAPI-02", kimlikler("Hızlı ve kolay ve ucuz ve sağlam ve hafif bir ürün."))
        self.assertNotIn("YAPI-02", kimlikler("Elma ve armut aldım.\n\nÇay ve kahve içtik."))

    def test_mektedir_yigilmasi(self):
        metin = "Şirket büyümektedir. Ekip genişlemektedir. Gelir artmaktadır."
        self.assertIn("YAPI-03", kimlikler(metin))

    def test_kalin_etiketli_madde(self):
        self.assertIn("BIC-02", kimlikler("- **Hız:** Sayfalar çabuk açılır.\n- **Güvenlik:** Veriler şifrelenir."))

    def test_tekduze_ritim(self):
        cumle = "Ekibimiz bu yıl boyunca yeni ürünün geliştirilmesi için çok yoğun bir çalışma yürüttü ve hedeflere ulaştı."
        self.assertIn("YAPI-01", kimlikler(" ".join([cumle] * 6)))


class Register(unittest.TestCase):
    METIN = "Söz konusu sözleşme incelenmiştir. Bu bağlamda ek süre verilmiştir."

    def test_gundelikte_iz(self):
        self.assertIn("SOZ-02", kimlikler(self.METIN))

    def test_akademikte_olagan(self):
        self.assertNotIn("SOZ-02", kimlikler(self.METIN, "akademik"))
        self.assertIn("SOZ-02", kimlikler(self.METIN, "akademik", olagan=True))

    def test_gunumuzde_akademikte_de_izdir(self):
        self.assertIn("SOZ-02", kimlikler("Günümüzde hava kirliliği artmaktadır.", "akademik"))

    def test_akademikte_yigilma_yine_izdir(self):
        metin = "Kirlilik artmaktadır. Veriler bunu göstermektedir (p<0,05). Önlemler yetersiz kalmaktadır."
        self.assertIn("YAPI-03", kimlikler(metin, "akademik"))


class Karsilastirma(unittest.TestCase):
    KAYNAK = ("Satışlar 2024'te 12.5% artabilir. Rapor için Lodos Lojistik ekibine "
              "destek@ornek.example adresinden ulaşın.")

    def test_bicim_degisikligi_fark_sayilmaz(self):
        yeni = "Satışlar 2024'te %12,5 artabilir. Rapor için Lodos Lojistik ekibine destek@ornek.example adresinden ulaşın."
        self.assertTrue(tara.karsilastir(self.KAYNAK, yeni)["temiz"])

    def test_degisen_sayi_yakalanir(self):
        yeni = self.KAYNAK.replace("12.5%", "%15")
        sonuc = tara.karsilastir(self.KAYNAK, yeni)
        self.assertEqual(sonuc["eksik_sayilar"], ["125"])
        self.assertEqual(sonuc["yeni_sayilar"], ["15"])

    def test_dusen_ad_ve_adres_yakalanir(self):
        sonuc = tara.karsilastir(self.KAYNAK, "Satışlar 2024'te %12,5 artabilir.")
        self.assertIn("Lodos", sonuc["eksik_adlar"])
        self.assertEqual(sonuc["eksik_adresler"], ["destek@ornek.example"])

    def test_ek_degisse_de_ad_bulunur(self):
        sonuc = tara.karsilastir("Başvuru Ankara Üniversitesi'ne yapılacak.", "Başvuru Ankara Üniversitesine yapılacak.")
        self.assertEqual(sonuc["eksik_adlar"], [])

    def test_guclenen_iddia_yakalanir(self):
        sonuc = tara.karsilastir(self.KAYNAK, self.KAYNAK.replace("artabilir", "artacak"))
        self.assertFalse(sonuc["temiz"])
        self.assertLess(sonuc["temkin"]["yeni"], sonuc["temkin"]["kaynak"])


class KomutSatiri(unittest.TestCase):
    def test_json_ciktisi(self):
        ornek = KOK / "turkish-humanizer" / "examples" / "02-eposta.md"
        tampon = io.StringIO()
        with redirect_stdout(tampon):
            kod = tara.main([str(ornek), "--json", "--register", "is"])
        self.assertEqual(kod, 0)
        veri = json.loads(tampon.getvalue())
        self.assertEqual(veri["register"], "is")
        self.assertTrue(veri["bulgular"])

    def test_olmayan_dosya(self):
        self.assertEqual(tara.main(["yok-boyle-bir-dosya.md"]), 2)


class Katalog(unittest.TestCase):
    def test_kural_kimlikleri_katalogda_var(self):
        katalog = (KOK / "turkish-humanizer" / "references" / "ai-oruntuleri.md").read_text(encoding="utf-8")
        kullanilan = {k[0] for k in tara.SOZLUK_KURALLARI} | {k[0] for k in tara.BICIM_KURALLARI}
        kullanilan |= {"YAPI-01", "YAPI-02", "YAPI-03", "YAPI-05", "YAPI-11", "SOZ-05", "CEV-03", "NOK-04", "BIC-03"}
        for kimlik in sorted(kullanilan):
            with self.subTest(kimlik=kimlik):
                self.assertIn(f"### {kimlik} ·", katalog)

    def test_her_blok_dizinde(self):
        import re
        katalog = (KOK / "turkish-humanizer" / "references" / "ai-oruntuleri.md").read_text(encoding="utf-8")
        for kimlik in re.findall(r"^### ([A-Z]+-\d\d) ·", katalog, re.M):
            with self.subTest(kimlik=kimlik):
                self.assertIn(f"- [{kimlik} ", katalog)
                self.assertIn(f'<a id="{kimlik.lower()}"></a>', katalog)


    def test_sonra_ornekleri_temiz(self):
        # Katalogdaki düzeltilmiş örnekler, tarayıcının yakaladığı hiçbir izi taşımamalı.
        import re
        katalog = (KOK / "turkish-humanizer" / "references" / "ai-oruntuleri.md").read_text(encoding="utf-8")
        for blok in re.split(r"(?m)^(?=<a id=)", katalog):
            baslik = re.search(r"^### ([A-Z]+-\d\d)", blok, re.M)
            if not baslik:
                continue
            for alan, metin in re.findall(r"^- \*\*(Sonra[^:]*|Yerinde düzeltme):\*\* \*(.+?)\*", blok, re.M):
                with self.subTest(kimlik=baslik.group(1), alan=alan):
                    # YAPI-01 tek cümlelik örneklerde anlamsızdır.
                    self.assertEqual(kimlikler(metin) - {"YAPI-01"}, set())


if __name__ == "__main__":
    unittest.main()
