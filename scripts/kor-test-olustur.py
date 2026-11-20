#!/usr/bin/env python3
"""Kör karşılaştırma formu üretir.

Her örnek dosyasındaki "Önce" (kaynak) ve "Sonra" (skill çıktısı) metinlerini
rastgele A/B sırasıyla bir forma yazar. Okur hangisinin daha doğal ve daha
açık olduğunu, hangisinin hangisi olduğunu bilmeden seçer. Cevap anahtarı
ayrı bir dosyaya yazılır.

Kullanım:
    python3 scripts/kor-test-olustur.py                 # examples/ klasöründen
    python3 scripts/kor-test-olustur.py --tohum 7       # aynı karışık sırayı yeniden üret
    python3 scripts/kor-test-olustur.py --cift kaynak.md cikti.md --cift ...

Çıktılar (varsayılan klasör: kor-test/):
    form.md    okurlara verilecek form
    anahtar.md hangi seçeneğin skill çıktısı olduğu (okurlara vermeyin)

Sonuçları bir issue'da paylaşın: kaç okur, kaç karşılaştırma, kaçında skill
çıktısı seçildi. Okurların metinleri kendi başlarına, birbirleriyle konuşmadan
değerlendirmesi gerekir.
"""
import argparse
import random
import re
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
ORNEKLER = KOK / "turkish-humanizer" / "examples"


def alinti(bolum):
    """Bir bölümdeki '>' ile başlayan satırları düz metne çevirir."""
    satirlar = [re.sub(r"^>\s?", "", s) for s in bolum.splitlines() if s.startswith(">")]
    return "\n".join(satirlar).strip()


def ornekten_cift(yol):
    metin = yol.read_text(encoding="utf-8")
    once = re.search(r"^## Önce\s*\n(.*?)(?=^## )", metin, re.S | re.M)
    sonra = re.search(r"^## Sonra\s*\n(.*?)(?=^## |\Z)", metin, re.S | re.M)
    if not (once and sonra):
        return None
    baslik = re.search(r"^# (.+)$", metin, re.M)
    return (baslik.group(1) if baslik else yol.stem), alinti(once.group(1)), alinti(sonra.group(1))


def main(argv=None):
    ap = argparse.ArgumentParser(description="Kör karşılaştırma formu üretir.")
    ap.add_argument("--cift", nargs=2, action="append", metavar=("KAYNAK", "CIKTI"),
                    help="examples/ yerine kendi kaynak ve çıktı dosyalarınız (birden çok kez verilebilir)")
    ap.add_argument("--tohum", type=int, default=None, help="rastgele sıra için tohum")
    ap.add_argument("--cikti", default="kor-test", help="çıktı klasörü (varsayılan: kor-test)")
    a = ap.parse_args(argv)

    if a.cift:
        ciftler = [(Path(c).stem, Path(k).read_text(encoding="utf-8").strip(), Path(c).read_text(encoding="utf-8").strip())
                   for k, c in a.cift]
    else:
        ciftler = [c for c in (ornekten_cift(y) for y in sorted(ORNEKLER.glob("*.md"))) if c]

    rastgele = random.Random(a.tohum)
    rastgele.shuffle(ciftler)
    form = ["# Kör karşılaştırma", "",
            "Her soruda aynı içeriğin iki yazılışı var. Hangisini bir insanın yazmış olma olasılığı daha yüksek, "
            "hangisi daha açık? Her soru için **A** ya da **B** yazın. Metinleri başkalarıyla konuşmadan değerlendirin.", ""]
    anahtar = ["# Cevap anahtarı", "", "Okurlara vermeyin.", "", "| Soru | Örnek | Skill çıktısı |", "|---|---|---|"]
    for no, (ad, kaynak, cikti) in enumerate(ciftler, 1):
        cikti_a = rastgele.random() < 0.5
        a_metin, b_metin = (cikti, kaynak) if cikti_a else (kaynak, cikti)
        form += [f"## Soru {no}", "", "**A**", "", a_metin, "", "**B**", "", b_metin, "",
                 "Seçiminiz (A/B): ____", "", "---", ""]
        anahtar.append(f"| {no} | {ad} | {'A' if cikti_a else 'B'} |")

    klasor = Path(a.cikti)
    klasor.mkdir(parents=True, exist_ok=True)
    (klasor / "form.md").write_text("\n".join(form), encoding="utf-8")
    (klasor / "anahtar.md").write_text("\n".join(anahtar) + "\n", encoding="utf-8")
    print(f"{len(ciftler)} karşılaştırma: {klasor / 'form.md'} ve {klasor / 'anahtar.md'} yazıldı.")


if __name__ == "__main__":
    main()
