#!/usr/bin/env python3
"""Paketin ve kataloğun tutarlılığını denetler.

Kullanım:  python3 scripts/paket-dogrula.py

Denetlenenler:
- Sürüm: SKILL.md metadata.version, CHANGELOG.md'nin ilk sürüm başlığı ve
  eklenti manifestleri aynı.
- Açıklama: Manifestlerdeki açıklama, SKILL.md açıklamasının ilk cümlesi.
- SKILL.md: üst bilgi alanları, ad biçimi, açıklama uzunluğu, sözcük bütçesi.
- Katalog: kimlikler tekil, her blok dizinde ve güç etiketi dizinle aynı,
  zorunlu alanlar dolu, SKILL.md'deki güçlü/zayıf listeleri katalogla aynı.
- Atıflar: Depoda anılan her örüntü kimliği katalogda var.
- Dağıtım: kısa talimat 1.500 karakteri aşmıyor, eklenti yolları skill'e
  çıkıyor, eval vakaları eksiksiz.

Yalnızca standart kitaplığı kullanır. Hata varsa hepsini yazar ve 1 ile çıkar.
"""
import json
import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
SKILL_KLASORU = KOK / "turkish-humanizer"
SKILL_ADI = "turkish-humanizer"
SOZCUK_BUTCESI = 3000
KISA_TALIMAT_SINIRI = 1500
GUCLER = {"güçlü", "orta", "tek başına zayıf", "kural"}
ALANLAR = ["Belirti", "Neden yapay", "Ne yapmalı", "Dokunma", "Güç", "Önce", "Sonra"]
ASI_ALANLARI = ["Belirti", "Neden yapay", "Ne yapmalı", "Dokunma", "Kaynak", "Aşırı düzeltme", "Yerinde düzeltme"]
UST_BILGI_ALANLARI = {"name", "description", "license", "metadata", "allowed-tools", "compatibility"}
KIMLIK = re.compile(r"\b(YAPI|SOZ|CEV|NOK|BIC|DOL|OKU|YAZ|ASI)-(\d\d)\b")

hatalar = []


def hata(mesaj):
    hatalar.append(mesaj)


def oku(yol):
    try:
        return (KOK / yol).read_text(encoding="utf-8")
    except OSError:
        hata(f"{yol} okunamadı")
        return ""


def json_oku(yol):
    try:
        return json.loads(oku(yol) or "{}")
    except json.JSONDecodeError as e:
        hata(f"{yol} geçerli JSON değil: {e}")
        return {}


# ---------------------------------------------------------------- SKILL.md

skill = oku("turkish-humanizer/SKILL.md")
ust = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
if not ust:
    hata("SKILL.md bir YAML üst bilgisiyle başlamalı")
    ust_bilgi, govde = "", skill
else:
    ust_bilgi, govde = ust.group(1), skill[ust.end():]

anahtarlar = set(re.findall(r"(?m)^([a-z][\w-]*):", ust_bilgi))
if anahtarlar - UST_BILGI_ALANLARI:
    hata(f"SKILL.md üst bilgisinde bilinmeyen alan: {sorted(anahtarlar - UST_BILGI_ALANLARI)}")

ad = re.search(r"(?m)^name: (.+)$", ust_bilgi)
if not ad or ad.group(1).strip() != SKILL_ADI:
    hata(f"SKILL.md name alanı '{SKILL_ADI}' olmalı ve klasör adıyla aynı kalmalı")

aciklama_eslesme = re.search(r"(?m)^description: (.+)$", ust_bilgi)
aciklama = aciklama_eslesme.group(1).strip() if aciklama_eslesme else ""
if not aciklama:
    hata("SKILL.md description alanı tek satırda yazılmalı")
elif len(aciklama) > 1024:
    hata(f"SKILL.md açıklaması 1.024 karakteri aşıyor ({len(aciklama)})")
ilk_cumle = re.split(r"(?<=\.)\s", aciklama, maxsplit=1)[0]

skill_surumu = re.search(r'(?m)^\s+version:\s*"?(\d+\.\d+\.\d+)"?\s*$', ust_bilgi)
if not skill_surumu:
    hata("SKILL.md üst bilgisine metadata.version ekleyin (ör. \"1.2.0\")")

sozcuk = len(govde.split())
if sozcuk > SOZCUK_BUTCESI:
    hata(f"SKILL.md {sozcuk} sözcük, bütçe {SOZCUK_BUTCESI}. Her kullanımda baştan sona okunur, kısaltın.")

# ---------------------------------------------------------------- sürüm ve manifestler

changelog = oku("CHANGELOG.md")
changelog_surumu = re.search(r"(?m)^## (\d+\.\d+\.\d+)\b", changelog)
if not changelog_surumu:
    hata("CHANGELOG.md'de '## 1.2.0' biçiminde bir sürüm başlığı olmalı")

eklenti = json_oku(".claude-plugin/plugin.json")
pazar = json_oku(".claude-plugin/marketplace.json")
cursor = json_oku(".cursor-plugin/plugin.json")
paket = json_oku("package.json")

surumler = {
    "SKILL.md": skill_surumu.group(1) if skill_surumu else None,
    "CHANGELOG.md": changelog_surumu.group(1) if changelog_surumu else None,
    ".claude-plugin/plugin.json": eklenti.get("version"),
    ".cursor-plugin/plugin.json": cursor.get("version"),
}
if len(set(surumler.values())) != 1:
    hata("Sürüm her yerde aynı olmalı: " + ", ".join(f"{k}={v}" for k, v in surumler.items()))
if "version" in paket:
    hata("package.json'a version eklemeyin, pi git üzerinden kurar")

aciklamalar = {
    ".claude-plugin/plugin.json": eklenti.get("description"),
    ".cursor-plugin/plugin.json": cursor.get("description"),
    "package.json": paket.get("description"),
    **{f"marketplace.json/{p.get('name')}": p.get("description") for p in pazar.get("plugins", [])},
}
for yer, deger in aciklamalar.items():
    if deger != ilk_cumle:
        hata(f"{yer} açıklaması SKILL.md açıklamasının ilk cümlesi olmalı: {ilk_cumle!r}")

for yer, veri in ((".claude-plugin/plugin.json", eklenti), (".cursor-plugin/plugin.json", cursor)):
    if veri.get("name") != SKILL_ADI:
        hata(f"{yer} name alanı '{SKILL_ADI}' olmalı")
if [p.get("name") for p in pazar.get("plugins", [])] != [SKILL_ADI]:
    hata("marketplace.json tek bir 'turkish-humanizer' eklentisi listelemeli")


def skill_bulunur(yol):
    """Yol ya bir skill klasörü ya da skill klasörlerini içeren bir klasör olmalı."""
    klasor = (KOK / yol).resolve()
    return (klasor / "SKILL.md").is_file() or (klasor / SKILL_ADI / "SKILL.md").is_file()


yollar = {
    ".claude-plugin/plugin.json skills": eklenti.get("skills", []),
    ".cursor-plugin/plugin.json skills": cursor.get("skills", []),
    "package.json pi.skills": paket.get("pi", {}).get("skills", []),
}
for yer, liste in yollar.items():
    liste = [liste] if isinstance(liste, str) else liste
    if not liste:
        hata(f"{yer} tanımlı değil")
    for yol in liste:
        if not skill_bulunur(yol):
            hata(f"{yer}: '{yol}' yolundan skill'e ulaşılamıyor")

openai = oku("turkish-humanizer/agents/openai.yaml")
for alan in ("display_name", "short_description", "default_prompt"):
    if not re.search(rf"(?m)^\s+{alan}: \".+\"$", openai):
        hata(f"agents/openai.yaml: {alan} eksik")
kisa = re.search(r'(?m)^\s+short_description: "(.+)"$', openai)
if kisa and not 25 <= len(kisa.group(1)) <= 64:
    hata("agents/openai.yaml: short_description 25-64 karakter olmalı")
if f"${SKILL_ADI}" not in openai:
    hata(f"agents/openai.yaml: default_prompt skill'i ${SKILL_ADI} diye anmalı")

# ---------------------------------------------------------------- katalog

katalog = oku("turkish-humanizer/references/ai-oruntuleri.md")
dizin_satirlari = dict(re.findall(r"(?m)^- \[([A-Z]+-\d\d) [^\]]+\]\(#[a-z]+-\d\d\)(?: · (.+))?$", katalog))
bloklar = {}
for blok in re.split(r"(?m)^(?=<a id=)", katalog):
    baslik = re.search(r"^### ([A-Z]+-\d\d) · ", blok, re.M)
    if not baslik:
        continue
    kimlik = baslik.group(1)
    if kimlik in bloklar:
        hata(f"Katalog: {kimlik} iki kez kullanılmış")
    bloklar[kimlik] = blok
    if f'<a id="{kimlik.lower()}"></a>' not in blok:
        hata(f"Katalog: {kimlik} bloğunun çapası eksik ya da yanlış")
    alanlar = ASI_ALANLARI if kimlik.startswith("ASI") else ALANLAR
    for alan in alanlar:
        if not re.search(rf"(?m)^- \*\*{re.escape(alan)}(?: \([^)]*\))?:\*\*\s*\S", blok):
            hata(f"Katalog: {kimlik} bloğunda '{alan}' alanı eksik")
    guc = re.search(r"(?m)^- \*\*Güç:\*\* (.+)$", blok)
    if guc and guc.group(1) not in GUCLER:
        hata(f"Katalog: {kimlik} güç değeri '{guc.group(1)}' geçersiz, seçenekler: {sorted(GUCLER)}")
    if kimlik not in dizin_satirlari:
        hata(f"Katalog: {kimlik} dizinde yok")
    elif guc and dizin_satirlari[kimlik] != guc.group(1):
        hata(f"Katalog: {kimlik} dizindeki güç etiketi bloktakiyle aynı değil")

for kimlik in dizin_satirlari:
    if kimlik not in bloklar:
        hata(f"Katalog: dizindeki {kimlik} için blok yok")

guc_haritasi = {k: re.search(r"(?m)^- \*\*Güç:\*\* (.+)$", b).group(1)
                for k, b in bloklar.items() if re.search(r"(?m)^- \*\*Güç:\*\* (.+)$", b)}
guc_paragrafi = re.search(r"(?m)^\*\*Güç:\*\* (.+)$", govde)
if not guc_paragrafi:
    hata("SKILL.md'de '**Güç:**' ile başlayan paragraf yok")
else:
    metin = guc_paragrafi.group(1)
    guclu_kismi = re.search(r"\*\*Güçlü\*\*(.*?)\*\*Tek başına zayıf\*\*", metin)
    zayif_kismi = re.search(r"\*\*Tek başına zayıf\*\*(.*?)\*\*Kural\*\*", metin)
    for etiket, kisim in (("güçlü", guclu_kismi), ("tek başına zayıf", zayif_kismi)):
        if not kisim:
            hata(f"SKILL.md güç paragrafında '{etiket}' listesi bulunamadı")
            continue
        anilan = {"-".join(e) for e in KIMLIK.findall(kisim.group(1))}
        beklenen = {k for k, g in guc_haritasi.items() if g == etiket}
        if anilan != beklenen:
            hata(f"SKILL.md '{etiket}' listesi katalogla aynı değil. "
                 f"Fazla: {sorted(anilan - beklenen)}, eksik: {sorted(beklenen - anilan)}")

# ---------------------------------------------------------------- atıflar

taranacak = [KOK / "README.md", KOK / "CONTRIBUTING.md", KOK / "dist" / "kisa-talimat.txt"]
taranacak += sorted(SKILL_KLASORU.rglob("*.md")) + sorted(SKILL_KLASORU.rglob("*.py"))
taranacak += sorted((KOK / "tests").glob("*.py"))
for dosya in taranacak:
    if not dosya.is_file():
        continue
    for on, no in set(KIMLIK.findall(dosya.read_text(encoding="utf-8"))):
        if f"{on}-{no}" not in bloklar:
            hata(f"{dosya.relative_to(KOK)}: {on}-{no} katalogda yok")

oruntu_sayisi = sum(not k.startswith("ASI") for k in bloklar)
asi_sayisi = sum(k.startswith("ASI") for k in bloklar)
readme = oku("README.md")
beklenen_ifade = f"{oruntu_sayisi} örüntü ve {asi_sayisi} aşırı düzeltme örüntüsü"
if beklenen_ifade not in readme:
    hata(f"README.md katalog boyutunu '{beklenen_ifade}' diye anmalı")

# ---------------------------------------------------------------- dağıtım ve eval

kisa_talimat = oku("dist/kisa-talimat.txt").strip()
if len(kisa_talimat) > KISA_TALIMAT_SINIRI:
    hata(f"dist/kisa-talimat.txt {len(kisa_talimat)} karakter, sınır {KISA_TALIMAT_SINIRI}")

for vaka in sorted((SKILL_KLASORU / "evals").iterdir()):
    if not vaka.is_dir():
        continue
    eksik = [ad for ad in ("case.yaml", "prompt.md") if not (vaka / ad).is_file()]
    if not list((vaka / "graders").glob("*.md")):
        eksik.append("graders/*.md")
    if eksik:
        hata(f"evals/{vaka.name}: eksik {', '.join(eksik)}")

if hatalar:
    print(f"{len(hatalar)} sorun bulundu:", file=sys.stderr)
    for h in hatalar:
        print(f"  - {h}", file=sys.stderr)
    sys.exit(1)
print(f"Paket tutarlı: sürüm {surumler['SKILL.md']}, {oruntu_sayisi} örüntü + {asi_sayisi} aşırı düzeltme, "
      f"SKILL.md {sozcuk} sözcük, kısa talimat {len(kisa_talimat)} karakter.")
