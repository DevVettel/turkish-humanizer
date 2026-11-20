# Yapay zeka araçları için rehber

Bu dosya, depoda çalışan kodlama ajanları (Claude Code, Codex, Cursor ve diğerleri) ve onları kullanan katkıcılar içindir. Skill'i bozmadan nasıl değiştireceğinizi anlatır.

## Depo neyi içerir?

turkish-humanizer, Markdown ile yazılmış bir agent skill'idir. Ürün `turkish-humanizer/SKILL.md` ve onun okuduğu `references/` dosyalarıdır. Derleme adımı yoktur. `dist/` dosyaları script ile üretilir.

Skill'i taşınabilir tutun. Talimatları tek bir araca bağlamayın. "Kod çalıştırabiliyorsan" gibi koşullu yazın.

## Önemli dosyalar

- `turkish-humanizer/SKILL.md`: skill'in kendisi. Her kullanımda baştan sona okunur.
- `turkish-humanizer/references/ai-oruntuleri.md`: örüntü kataloğu. Her blok aynı şablonu kullanır ve bir güç etiketi taşır.
- `turkish-humanizer/scripts/tara.py`: sayılabilir örüntüleri bulan tarayıcı. Yalnızca standart kitaplık.
- `turkish-humanizer/agents/openai.yaml`: Codex ve OpenAI uyumlu ajanlar için görünen ad ve varsayılan istem.
- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`: Claude Code eklentisi ve marketplace.
- `.cursor-plugin/plugin.json`: Cursor eklentisi.
- `package.json`: pi paketi. `version` alanı eklemeyin, pi git üzerinden kurar.
- `scripts/tek-dosya-olustur.py`: `dist/` altındaki zip ve tek dosya sürümünü üretir.
- `scripts/paket-dogrula.py`: sürüm, açıklama ve katalog tutarlılığını denetler.
- `CHANGELOG.md`: sürüm notları, en yenisi üstte.

## Değişiklik kuralları

- **Örüntü eklerken** önce var olan bir bloğa katılıp katılamayacağına bakın. Yeni blok gerekiyorsa şablonu kullanın, yedi alanı doldurun, dizine güç etiketiyle ekleyin. Güçlü ya da tek başına zayıf bir örüntü eklediyseniz SKILL.md'deki **Güç** paragrafını da güncelleyin. Doğrulayıcı bu listeleri katalogla karşılaştırır.
- **Örnekler özgün olmalı.** Başka projelerden, kitaplardan ya da sitelerden metin çevirmeyin. "Sonra" örnekleri anlamı, sayıları ve özel isimleri korumalı ve tarayıcıdan temiz çıkmalı.
- **Sürüm:** Davranış değişikliğinde SKILL.md `metadata.version`, `CHANGELOG.md` başlığı ve iki eklenti manifestindeki `version` birlikte artar.
- **Açıklama:** Manifestlerdeki açıklama, SKILL.md açıklamasının ilk cümlesidir.
- **Uzunluk:** SKILL.md'nin sözcük bütçesi 3.000. Her eklenen cümle yerini hak etmeli. Ayrıntı ve örnekler `references/` dosyalarına gider.
- **Kısa talimat:** `dist/kisa-talimat.txt` elle yazılır ve 1.500 karakteri aşmamalı.

## Yayımlamadan önce

```bash
python3 -m unittest discover -s tests
python3 scripts/paket-dogrula.py
python3 scripts/tek-dosya-olustur.py
claude plugin validate .        # Claude Code kuruluysa
```

## Yazım üslubu

Depodaki her metin (dokümantasyon, kod yorumu, hata mesajı) skill'in kendi kurallarına uyar: cümle içinde uzun çizgi yok, "ve"den önce virgül yok, -mektedir yığılması yok, TDK yazımı. Kısa cümle, etken çatı, tek kavram için tek terim.
