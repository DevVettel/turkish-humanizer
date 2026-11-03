# turkish-humanizer

Türkçe metinleri yapay zeka izlerinden arındıran bir [Claude skill'i](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

*[English summary below](#english)*

## Neden?

İngilizce için yazılmış "humanizer" araçları *delve*, *crucial*, *tapestry* gibi sözcükleri avlar. Türkçede bunların neredeyse hiçbir karşılığı yok, çünkü Türkçede yapay zeka izi sözcükten çok **yapıda** görülür:

- Her cümle aynı dizilimde ve benzer uzunlukta.
- Bağlaç olarak hep "ve, ama, çünkü".
- Yüklemler hep "-mektedir, -maktadır".
- "Önemli bir rol oynamaktadır", "bu bağlamda", "günümüzde".
- Çeviri kokan kalıplar: "günün sonunda", "derinlemesine dalmak", "-e sahip olmak".
- İngilizce noktalama: cümle içinde uzun çizgi (—), "ve"den önce virgül, *25%*.

turkish-humanizer bu örüntüleri yakalar ve metni yeniden yazar. Bunu yaparken **anlamı, sayıları, terimleri ve özel isimleri olduğu gibi korur**, bilgi eklemez ve çıkarmaz. Akademik bir metin akademik kalır.

## Önce / sonra

> **Önce:** Teknolojinin hızla geliştiği günümüzde, yapay zeka birçok sektörü dönüştürmektedir. Bu bağlamda, söz konusu dönüşüm göz önünde bulundurulduğunda şirketlerin hazırlıklı olması gerekmektedir.
>
> **Sonra:** Yapay zeka birçok sektörü dönüştürüyor ve şirketlerin buna hazırlanması gerekiyor.

Beş metin türü için tam örnekler [`turkish-humanizer/examples/`](turkish-humanizer/examples/) klasöründe.

## Kurulum

**Claude Code:**

```bash
git clone https://github.com/<kullanici>/turkish-humanizer.git
cp -r turkish-humanizer/turkish-humanizer ~/.claude/skills/
```

**Claude.ai:** `turkish-humanizer/` klasörünü zip'leyip *Ayarlar → Yetenekler (Capabilities) → Skills* bölümünden yükleyin.

## Kullanım

Claude'a bir Türkçe metin verip şunlardan birini söyleyin:

- "Bu metni **insanlaştır**"
- "**Doğallaştır**, yapay zeka gibi durmasın"
- "**Türkçeleştir**"

Varsayılan çıktı yalnızca düzeltilmiş metindir. Neyin neden değiştiğini görmek isterseniz "değişiklik özetini de ver" demeniz yeterli.

## Depo yapısı

```
turkish-humanizer/          ← skill'in kendisi (kurulan klasör)
├── SKILL.md                ← tetikleyici ve çalışma adımları
├── references/
│   ├── ai-oruntuleri.md    ← örüntü kataloğu (katkıların ana adresi)
│   ├── cumle-turleri.md    ← cümle çeşitliliği araç kutusu
│   ├── baglaclar.md        ← bağlaç alternatifleri ve register etiketleri
│   └── noktalama.md        ← TDK'ya dayalı noktalama ve yazım denetimi
├── examples/               ← 5 metin türü için önce/sonra çiftleri
└── evals/                  ← test vakaları
kaynaklar/                  ← ayrıntılı kaynak belgeler ve kaynakça
```

## Katkı

En değerli katkı, **yeni bir yapay zeka örüntüsü** eklemektir. [`ai-oruntuleri.md`](turkish-humanizer/references/ai-oruntuleri.md) dosyasındaki her örüntü aynı şablonla yazılmış bağımsız bir bloktur. Yeni bir örüntü eklemek için bir bloğu kopyalamanız yeterli.

Skill'in bir metinde anlamı değiştirdiğini fark ettiyseniz bu da çok değerli: lütfen "Anlam kayması" şablonuyla bir issue açın.

Ayrıntılar için: [CONTRIBUTING.md](CONTRIBUTING.md)

## Doğrulama ve sınırlar

Noktalama ve yazım kuralları TDK *Yazım Kılavuzu* ve *Güncel Türkçe Sözlük* ile doğrulandı. Kılavuzda açık bir hükmü bulunmayan maddeler `kaynaklar/` dosyalarında **[DOĞRULANMADI]** etiketiyle işaretli. Bunları doğrulamak da iyi bir ilk katkı olur.

Bu skill bir üslup aracıdır, bir yapay zeka tespit aracını atlatma aracı değildir. Amaç, metni okuyan **insan** için daha iyi hale getirmektir.

## Lisans

[MIT](LICENSE)

---

<a id="english"></a>
## English

**turkish-humanizer** is a Claude skill that removes AI-writing patterns from Turkish text.

Existing humanizer skills target English tells like *delve* or *crucial*, which barely exist in Turkish. In Turkish, AI text shows itself through **structure**: uniform subject-object-verb sentences of equal length, a monopoly of *ve/ama/çünkü* (and/but/because), stacked *-mektedir* verb endings, calqued English idioms (*günün sonunda* = "at the end of the day"), and English punctuation habits (em dashes, Oxford commas, *25%*).

The skill rewrites the text while preserving meaning, numbers, terminology and proper nouns exactly, and it keeps the original register: academic text stays academic.

- **Install (Claude Code):** copy the inner `turkish-humanizer/` folder to `~/.claude/skills/`.
- **Use:** give Claude Turkish text and say *"insanlaştır"*, *"doğallaştır"* or *"humanize this"*.
- **Contribute:** the pattern catalog in `turkish-humanizer/references/ai-oruntuleri.md` uses one copy-paste template per pattern. See [CONTRIBUTING.md](CONTRIBUTING.md) (in Turkish). Issues and PRs in English are welcome too.

License: MIT.
