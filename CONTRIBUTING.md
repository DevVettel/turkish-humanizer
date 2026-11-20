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
| Tarayıcıya yeni kural | `turkish-humanizer/scripts/tara.py` ve `tests/` | Orta |
| SKILL.md davranış değişikliği | `turkish-humanizer/SKILL.md` | Önce issue açın |

## Yeni örüntü eklemek

1. `ai-oruntuleri.md` dosyasının sonundaki **şablonu** kopyalayın.
2. Uygun kategoriyi seçin ve o kategorideki sıradaki numarayı verin:
   `YAPI` yapı · `SOZ` klişe/sözcük · `CEV` çeviri kokusu · `NOK` noktalama · `BIC` biçim · `DOL` sohbet ve model artığı · `OKU` okur ve bağlam · `YAZ` yazım · `ASI` aşırı düzeltme
3. Bloğu kategorisinin sonuna ekleyin ve dosyanın başındaki **Dizin**e güç etiketiyle bir satır ekleyin.
4. Yedi alanın hepsini doldurun. **Dokunma** alanı zorunludur. Her örüntünün meşru olduğu bir bağlam vardır, onu düşünmek skill'in aşırıya kaçmasını önler.
5. **Güç** alanını seçin: `güçlü` (dikkatli bir yazar neredeyse hiç bilerek kullanmaz, tek görülüş yeter), `orta`, `tek başına zayıf` (insanlar da sık yazar, ancak başka izlerle birlikte düzeltilir) ya da `kural` (yazım ve noktalama hatası). Güçlü ya da zayıf bir örüntü eklediyseniz `SKILL.md`'deki **Güç** paragrafına da ekleyin.

Yeni blok açmadan önce var olan bir bloğa katılıp katılamayacağına bakın. Aynı izin başka bir biçimi çoğu zaman var olan bloğun **Belirti** satırına aittir.

### İyi bir örüntü bloğunun özellikleri

- **Gözleme dayanır.** Gerçek yapay zeka çıktılarında tekrar tekrar gördüğünüz bir şeydir. Tek seferlik bir tuhaflık değildir.
- **Türkçeye özgüdür.** İngilizce humanizer listelerinin çevirisi değildir.
- **Örnekleri özgündür.** Bir yerden kopyalanmamış, sizin yazdığınız cümlelerdir.
- **"Sonra" örneği anlamı korur.** Sayılar, özel isimler ve iddiaların gücü aynı kalır, yeni bilgi eklenmez. İnceleme sırasında en çok buna bakacağız.
- **Yasak listesi değildir.** "X kullanma" yerine "X şu durumda yapay durur, şu durumda doğaldır" der.

### Aşırı düzeltme örüntüleri (`ASI`)

Skill'in çıktısında tekrar tekrar gördüğünüz bir tik de (her cümleye eklenen bir "aslında", silinen kalıbın yerine kurulan benzeri) bir örüntüdür. Bunlar `ASI` kategorisine girer ve önce/sonra yerine **Kaynak**, **Aşırı düzeltme** ve **Yerinde düzeltme** alanlarını kullanır.

### Tarayıcıya kural eklemek

`tara.py` yalnızca düz metinden güvenle sayılabilen örüntüleri arar. Yeni bir kural eklerken:

- Kural katalogdaki bir bloğun kimliğini taşımalı. Katalogda olmayan bir şeyi script yakalamaz.
- Desen küçük harfe çevrilmiş metin üzerinde çalışır. Türkçe karakterleri doğrudan yazın.
- Yanlış alarm, kaçırılan bulgudan daha kötüdür. Emin olmadığınız bir kalıbı eklemeyin.
- `tests/test_tara.py` dosyasına kuralı yakalayan bir örnek ekleyin. Olağan bir kullanımı yakalamadığını gösteren bir örnek daha iyi olur.

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

- [ ] Yeni örüntü şablona uygun, yedi alan da dolu, güç etiketi seçildi
- [ ] Dizine satır eklendi
- [ ] "Sonra" örneği anlamı, sayıları ve özel isimleri koruyor
- [ ] Örnekler özgün
- [ ] Skill değiştiyse `dist/` yeniden üretildi
- [ ] `python3 -m unittest discover -s tests` ve `python3 scripts/paket-dogrula.py` geçiyor
- [ ] Davranış değiştiyse `CHANGELOG.md`'ye not düşüldü
- [ ] Kendi yazdığınız açıklamalarda cümle içinde uzun çizgi (—) yok 🙂

## Test

Değişikliğinizin skill'in davranışını nasıl etkilediğini görmek isterseniz `turkish-humanizer/evals/` altındaki test vakalarını kullanabilirsiniz. Bu vakalar `claude plugin eval` formatında yazıldı. Her vaka klasöründe bir `prompt.md`, beklenen sonucu anlatan bir `case.yaml` ve kontrol edilen ölçütleri içeren `graders/` var. Yeni bir vaka eklerken var olan bir klasörü kopyalayabilirsiniz.

`tests/` klasöründeki testler ise yapay zeka gerektirmez. Tarayıcının kurallarını ve katalogdaki her bloğun dizinde yer aldığını denetler:

```bash
python3 -m unittest discover -s tests
```

## Kör karşılaştırma

Skill'in gerçekten daha iyi metin üretip üretmediğini en iyi, hangisinin hangisi olduğunu bilmeyen okurlar söyler:

```bash
python3 scripts/kor-test-olustur.py                        # examples/ klasöründeki altı çift
python3 scripts/kor-test-olustur.py --cift eski.md yeni.md # kendi metinleriniz
```

Script `kor-test/form.md` (okurlara verilecek) ve `kor-test/anahtar.md` (cevaplar) dosyalarını yazar. Formu birkaç kişiye ayrı ayrı okutun, sonucu "Kör karşılaştırma sonucu" şablonuyla bir issue'da paylaşın. Olumsuz sonuçlar da değerlidir.

## Davranış kuralları

Bu projede [Davranış Kuralları](CODE_OF_CONDUCT.md) geçerlidir. Dil tartışmaları hararetli olabilir. Lütfen fikirleri tartışın, kişileri değil.
