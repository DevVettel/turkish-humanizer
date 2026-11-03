# Katkı rehberi

turkish-humanizer, Türkçe yazan herkesin gözlemleriyle büyüyen bir proje. Bir dil bilimci olmanız gerekmiyor. "Bu cümle yapay zeka yazmış gibi duruyor, çünkü ..." diyebiliyorsanız katkı yapabilirsiniz.

## Katkı türleri

| Ne | Nereye | Zorluk |
|---|---|---|
| Yeni yapay zeka örüntüsü | `turkish-humanizer/references/ai-oruntuleri.md` | Kolay |
| Var olan örüntüye daha iyi örnek | aynı dosya | Kolay |
| Anlam kayması bildirimi | Issue: "Anlam kayması" şablonu | Kolay |
| [DOĞRULANMADI] etiketli bir kuralı TDK'dan doğrulama | `kaynaklar/*.md` | Orta |
| Yeni önce/sonra örnek metni | `turkish-humanizer/examples/` | Orta |
| Yeni test vakası | `turkish-humanizer/evals/` | Orta |
| SKILL.md davranış değişikliği | `turkish-humanizer/SKILL.md` | Önce issue açın |

## Yeni örüntü eklemek

1. `ai-oruntuleri.md` dosyasının sonundaki **şablonu** kopyalayın.
2. Uygun kategoriyi seçin ve o kategorideki sıradaki numarayı verin:
   `YAPI` yapı · `SOZ` klişe/sözcük · `CEV` çeviri kokusu · `NOK` noktalama · `BIC` biçim · `DOL` dolgu · `YAZ` yazım
3. Bloğu kategorisinin sonuna ekleyin ve dosyanın başındaki **Dizin**e bir satır ekleyin.
4. Altı alanın hepsini doldurun. **Dokunma** alanı zorunludur. Her örüntünün meşru olduğu bir bağlam vardır, onu düşünmek skill'in aşırıya kaçmasını önler.

### İyi bir örüntü bloğunun özellikleri

- **Gözleme dayanır.** Gerçek yapay zeka çıktılarında tekrar tekrar gördüğünüz bir şeydir. Tek seferlik bir tuhaflık değildir.
- **Türkçeye özgüdür.** İngilizce humanizer listelerinin çevirisi değildir.
- **Örnekleri özgündür.** Bir yerden kopyalanmamış, sizin yazdığınız cümlelerdir.
- **"Sonra" örneği anlamı korur.** Sayılar, özel isimler ve iddiaların gücü aynı kalır, yeni bilgi eklenmez. İnceleme sırasında en çok buna bakacağız.
- **Yasak listesi değildir.** "X kullanma" yerine "X şu durumda yapay durur, şu durumda doğaldır" der.

## Anlam kayması bildirmek

Skill bir metni yeniden yazarken bir sayıyı değiştirdiyse, bir bilgi eklediyse ya da çıkardıysa, bir iddiayı güçlendirdiyse veya zayıflattıysa bu en önemli hata türüdür. Issue açarken şunları ekleyin:

- Kaynak metin (gizli bilgileri çıkarın)
- Skill'in çıktısı
- Hangi kısmın anlamı değişti ve nasıl

## Kuralları doğrulamak

`kaynaklar/` altındaki belgelerde **[DOĞRULANMADI]** etiketli maddeler var. Bir maddeyi TDK'nın resmî kaynaklarından (tdk.gov.tr, sozluk.gov.tr) doğrulayabilirseniz:

1. Etiketi kaldırın.
2. Kuralı kendi cümlenizle yazın. **Kılavuz metnini birebir kopyalamayın.**
3. Kaynakçaya sayfa adını ve erişim tarihini ekleyin.

Bir maddenin yanlış olduğunu bulursanız düzeltin ve PR açıklamasında kaynağınızı gösterin.

## Telif

- Tüm örnek cümleler **özgün** olmalı. Kitaplardan, haberlerden ve başka sitelerden metin kopyalamayın.
- Gerçek kişileri ve şirketleri örnek metinlerde kullanmayın. Kurgusal adlar seçin.
- Gerçek bir yapay zeka çıktısını örnek olarak kullanacaksanız kişisel ve gizli bilgilerden arındırın.

## dist/ klasörü

`dist/` altındaki zip ve tek dosya sürümü skill dosyalarından üretilir. Skill'de bir şey değiştirdiyseniz PR'dan önce şunu çalıştırın:

```bash
python3 scripts/tek-dosya-olustur.py
```

`dist/kisa-talimat.txt` elle yazılır. SKILL.md'deki temel kuralları değiştirdiyseniz bu metni de güncelleyin (ChatGPT'nin talimat sınırı nedeniyle en çok 1.500 karakter).

## Pull request kontrol listesi

- [ ] Yeni örüntü şablona uygun, altı alan da dolu
- [ ] Dizine satır eklendi
- [ ] "Sonra" örneği anlamı, sayıları ve özel isimleri koruyor
- [ ] Örnekler özgün
- [ ] Skill değiştiyse `dist/` yeniden üretildi
- [ ] Kendi yazdığınız açıklamalarda cümle içinde uzun çizgi (—) yok 🙂

## Test

Değişikliğinizin skill'in davranışını nasıl etkilediğini görmek isterseniz `turkish-humanizer/evals/` altındaki test vakalarını kullanabilirsiniz. Bu vakalar `claude plugin eval` formatında yazıldı. Her vaka klasöründe bir `prompt.md`, beklenen sonucu anlatan bir `case.yaml` ve kontrol edilen ölçütleri içeren `graders/` var. Yeni bir vaka eklerken var olan bir klasörü kopyalayabilirsiniz.

## Davranış kuralları

Bu projede [Davranış Kuralları](CODE_OF_CONDUCT.md) geçerlidir. Dil tartışmaları hararetli olabilir. Lütfen fikirleri tartışın, kişileri değil.
