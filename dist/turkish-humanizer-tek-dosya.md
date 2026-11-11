# Turkish Humanizer: tek dosya sürümü

> Bu dosya, turkish-humanizer Claude skill'inin ChatGPT, Gemini ve benzeri
> yapay zeka araçlarında kullanılabilmesi için tek dosyada birleştirilmiş
> hâlidir. Otomatik üretilir, elle düzenlemeyin
> (`scripts/tek-dosya-olustur.py`).
>
> **Yapay zekaya not:** Aşağıda `references/...` diye anılan dosyaların
> hepsi bu belgenin içinde, aynı adı taşıyan "Ek" başlıkları altında yer
> alır. Kullanıcı bir Türkçe metni insanlaştırmanı, doğallaştırmanı ya da
> Türkçeleştirmeni istediğinde bu belgedeki kurallara göre çalış.


# Turkish Humanizer

Türkçede yapay zeka izi sözcüklerden çok **yapıda** görülür: tekdüze dizilim, eşit cümle uzunlukları, "ve/ama/çünkü" tekeli, "-mektedir" yığılması, çeviri kokan kalıplar ve İngilizce noktalama. Bu skill'in işi, bir Türkçe metni bu izlerden arındırırken **söylediği hiçbir şeyi değiştirmemektir.**

## Değişmez kurallar

Bu kurallar üslupla ilgili her karardan önce gelir. Daha "doğal" bir cümle kurmak için bunlardan birini çiğnemek, skill'in amacını boşa çıkarır. Kullanıcı bu metni bir yere gönderecek ya da yayımlayacak, yanlış bir sayı ya da uydurulmuş bir iddia ona zarar verir.

1. **Anlamı değiştirme.** İddiaların gücünü de koru: "olabilir" "olur"a, "bazı" "birçok"a, "artırabilir" "artırır"a dönüşmesin.
2. **Sayıları, tarihleri, birimleri, terimleri, özel isimleri, alıntıları, URL'leri ve kodu aynen koru.** Yalnızca sayıların **biçimini** TDK'ya uydurabilirsin (*25%* → *%25*), ama değerin ne olduğundan emin değilsen dokunma.
3. **Bilgi ekleme.** Kaynakta olmayan bir örnek, gerekçe, sonuç, rakam ya da özne uydurma. Edilgen bir cümleyi etkene çevirirken eylemi yapan metinde açıkça yoksa edilgen bırak.
4. **Bilgi çıkarma.** Yalnızca gerçekten boş olan dolguları sil (klişe açılış ve kapanışlar, tekrar eden özet cümleleri, aynı şeyi söyleyen eş anlamlı sıfatlar). Bir maddeyi düzyazıya çevirdiğinde içindeki her bilgi yerinde kalmalı.
5. **Registerı koru.** Akademik metin akademik, resmi yazışma resmi kalır. Hitap biçimi (siz/sen) ve kişi (biz/ben/edilgen) değişmez.

## Çalışma adımları

### 1. Metni tanı

- **Register:** akademik/resmi · iş yazışması · blog/deneme · pazarlama/ürün · sosyal medya. Kararsızsan daha resmi olanı seç. Resmi bir metni gündelikleştirmek, gündelik bir metni biraz resmi bırakmaktan daha büyük bir hatadır.
- **Kullanıcının kendi sesi:** Kullanıcı kendi yazdığı bir örnek verdiyse ya da metnin bir bölümü belirgin biçimde onun elinden çıkmışsa ölçün odur. Cümle uzunluğu, bağlaç tercihi, hitap ve yazım alışkanlıkları için bu dosyadaki genel önerilerden önce o örneğe bak.
- **Korunacaklar listesi:** Metindeki bütün sayıları, tarihleri, özel isimleri, terimleri, alıntıları ve iddiaların kesinlik derecesini zihninde (ya da uzun metinde not olarak) çıkar. Son adımda bu listeyle karşılaştıracaksın.

### 2. Örüntüleri bul

`references/ai-oruntuleri.md` dosyasını oku. Örüntü kataloğu ve her biri için önce/sonra örneği orada. Metinde hangilerinin bulunduğunu belirle. Her örüntünün **Dokunma** satırına dikkat et: Aynı kalıp bir registerda iz, ötekinde olağan dildir.

Gerektiğinde şu dosyalara uzan:
- `references/cumle-turleri.md`: Tekdüze bir paragrafı hangi yapılarla kırabileceğini ve hangi yapının hangi registerda yerinde olduğunu gösterir.
- `references/baglaclar.md`: ve/ama/çünkü tekeline alternatifler, register etiketleri ve anlam tuzakları.
- `references/noktalama.md`: TDK'ya dayalı noktalama ve yazım denetimi (uzun çizgi, de/da, ki, mi, kesme, büyük harf, sayılar).

### 3. Yeniden yaz

- **Ölçülü ol.** Hedef, iyi bir Türk yazarın bu metni nasıl yazacağıdır. Her cümleyi değiştirmek hedef değildir. İyi bir cümleye dokunma. Cümlelerin çoğu yine kurallı ve orta uzunlukta kalabilir, yalnızca aralarına doğal kırılmalar girer.
- **Önce sadeleştir, sonra çeşitlendir.** En etkili düzeltme çoğu zaman silmektir (klişe, pekiştirme, boş geçiş sözü). Ardından birleştir (zarf-fiil, sıfat-fiil), en son bağlaç ve dizilimle oyna.
- **Devrik ve eksiltili cümleyi ancak bağlam isterse kullan.** Blog ve sosyal medyada bir iki tanesi metne ses katar. Akademik, resmi ve iş yazışmasında kullanma. Metne "insan" süsü vermek için eklenen bir devrik cümle, düzeltilen tekdüzelik kadar yapay durur.
- **Bağlaçları dağıtma, seç.** "ama" yerine sırayla "oysa, ne var ki, buna karşın" koymak da bir örüntüdür. Her ilişki için en uygun bağlacı seç, çoğu zaman da bağlacı tamamen kaldır.
- **Biçimi metne uydur.** Kısa bir e-postadaki başlıkları ve madde işaretlerini düzyazıya çevir. Gerçek adım listelerini ve taranacak bilgileri koru.
- **Noktalama ve yazımı düzelt.** Cümle içindeki uzun çizgiyi (—) kaldır, "ve"den önceki virgülü sil, de/da, ki, mi ve kesme işaretini TDK'ya göre düzelt.

### 4. Denetle

Önce **anlam.** Teslim etmeden önce yeni metni korunacaklar listesiyle karşılaştır:
- Her sayı, tarih ve özel isim yerinde ve aynı mı?
- Her iddia aynı kesinlikte mi? Kaynakta olmayan bir özne, gerekçe ya da sonuç eklendi mi?
- Silinen her şey gerçekten boş muydu?
- Register ve hitap aynı mı?

Bir şüphe varsa kaynaktaki hâline dön. Anlamca güvenli ama biraz daha az akıcı bir metin, akıcı ama yanlış bir metinden her zaman iyidir.

Sonra **kendi izin.** Bir kalıbı silerken yerine yenisini koymak en sık yapılan hatadır. Çıktıyı `references/ai-oruntuleri.md` dosyasındaki "Aşırı düzeltme" bölümüyle (ASI-01 ile ASI-05 arası) oku:
- **Silme testi:** Metne senin eklediğin her bağlacı, söylem sözcüğünü ("aslında", "açıkçası", "yani") ve devrik cümleyi tek tek sil. Anlamdan ve tondan bir şey eksilmiyorsa geri koyma.
- Sildiğin kalıbın yerine aynı iskeletin başka bir biçimini kurdun mu ("sadece X değil" yerine "X'ten çok Y")?
- Kaynakta olmayan bir samimiyet, anı ya da okura seslenme ekledin mi?
- Yaşayan bir sözcüğü ya da terimi "daha Türkçe" olsun diye değiştirdin mi?

Kod çalıştırabiliyorsan ve metin uzunsa `scripts/tara.py` ikinci bir göz olur: `python3 scripts/tara.py yeni.md --kaynak eski.md --register is` komutu yeni metinde kalan sayılabilir örüntüleri listeler, kaynaktaki sayıların, adreslerin, özel adların ve temkin ifadelerinin yerinde olup olmadığını da denetler. Script yalnızca sözcük düzeyinde bakar. Çıktısı bir aday listesidir, senin okumanın yerini tutmaz ve bulduğu her şeyi düzeltmek zorunda değilsin.

## Çıktı

Varsayılan olarak **yalnızca düzeltilmiş metni** ver: önsöz yok, "İşte düzeltilmiş metin:" yok, kapanış yok. Kaynak metnin biçimini (paragraf bölümleri, gerçek listeler, imza bloğu) koru.

İki durumda metnin altına kısa bir not ekle:
- Kullanıcı değişiklikleri, özeti ya da gerekçeyi isterse.
- Anlamdan emin olamadığın için bir şeye dokunmadıysan (ör. "1,500"ün binlik mi ondalık mı olduğu belirsiz) ya da metinde bir olgu hatası fark ettiysen. Olguyu sen düzeltme, yalnızca belirt.

Özet istendiğinde şu biçimi kullan (en çok 5-7 madde):

```
**Değişiklik özeti**
- YAPI-03: "-mektedir" ile biten 6 yüklemin 4'ü geniş zaman ve şimdiki zamana çevrildi.
- NOK-01: 3 uzun çizgi kaldırıldı (2'si virgül, 1'i iki nokta oldu).
- SOZ-02: "Bu bağlamda", "günümüzde" silindi.
- Dokunulmayanlar: "1,500" (binlik mi ondalık mı belirsiz).
```

## Yalnızca denetim

Kullanıcı metnin yeniden yazılmasını değil incelenmesini istiyorsa ("yapay zeka gibi mi duruyor", "nerelerinde iz var", "denetle", "sadece sorunları göster") **metni yeniden yazma.** 1. ve 2. adımı uygula, bulduklarını raporla:

```
**Denetim** (register: iş yazışması)

Belirgin izler
- NOK-01: 3 yerde cümle içi uzun çizgi. "…tek bir konu konuşuldu — bütçe."
- YAPI-03: 7 cümlenin 6'sı "-mektedir" ile bitiyor.

Daha hafif olanlar
- SOZ-02: "Bu bağlamda" (2. paragraf), "söz konusu" (3. paragraf).

Bu registerda olağan, dokunmazdım
- "tarafından" (1 kez, kurum adıyla).
```

- Her bulguyu örüntü kimliğiyle ve metinden kısa bir alıntıyla ver. Alıntısız genel yargı ("metin biraz resmi") işe yaramaz.
- Önem sırasına koy: önce yapı ve çeviri kokusu, sonra sözcük klişeleri, en sonda yazım ve noktalama.
- "Dokunma" satırına göre olağan saydığın kullanımları ayrı listele. Kullanıcı neye dokunulmayacağını da görmek ister.
- Metni kimin yazdığı hakkında hüküm verme. "Bu metni yapay zeka yazmış" ya da "%80 yapay zeka" gibi bir sonuca bu yöntemle varılamaz. Söyleyebileceğin, metinde hangi örüntülerin bulunduğudur. İnsanlar da bu kalıplarla yazar.
- Metin temizse bunu söyle, bulgu üretmek için zorlama.
- Kod çalıştırabiliyorsan `python3 scripts/tara.py metin.md` sayımları çıkarır. Raporu yine sen yazarsın: Script yapıyı ve anlamı okuyamaz.

## Özel durumlar

- **Metin zaten doğalsa** küçük düzeltmelerle (yazım, noktalama) yetin ve bunu bir cümleyle söyle. Yapacak bir şey yokken değişiklik üretme.
- **Metin Türkçe değilse ve kullanıcı "Türkçeleştir" diyorsa** metni Türkçeye çevir. Çeviriyi baştan bu dosyadaki ilkelere uygun yaz, kelime kelime çeviri yapma. Çeviri olduğunu belirt.
- **Kullanıcı sıfırdan Türkçe bir metin yazmanı istiyorsa** (bir konu, taslak ya da madde listesi verip "yaz" diyorsa) aynı ilkelerle yaz: Katalogdaki örüntüleri baştan kurma, cümleyi İngilizce düşünüp çevirme. Değişmez kuralların karşılığı burada kullanıcının verdiği bilgilerdir: Vermediği sayıyı, örneği ve iddiayı sen ekleme, eksik olan somut bilgiyi sor ya da metinde açıkça boş bırak.
- **Karışık dil (Türkçe metin içinde İngilizce terim)** varsa terimlere dokunma. Yerleşik bir Türkçe karşılığı olsa bile terim kullanıcının tercihidir.
- **Kod blokları, alıntılar, yasal metinden aktarılan maddeler** olduğu gibi kalır.
- **Uzun metinlerde** paragraf paragraf ilerle. Her paragraftan sonra korunacaklar listesini kontrol et.
- **Kullanıcının bilinçli üslubu** (edebi bir devrik dil, kasıtlı plaza dili, markanın emoji kullanımı) belirginse onu koru. Yalnızca yapay zekadan gelen katmanı temizle.

## Örnekler

`examples/` klasöründe altı metin türü için (blog, e-posta, akademik paragraf, ürün açıklaması, LinkedIn gönderisi, teknik doküman) tam önce/sonra çiftleri var. Her dosya hangi örüntülerin düzeltildiğini ve nelerin bilinçli olarak korunduğunu da gösterir. Bir türle ilk kez karşılaştığında ilgili örneğe bakmak ölçüyü tutturmana yardım eder.


---

# Ek: references/ai-oruntuleri.md

## Türkçe yapay zeka örüntüleri

Bu dosya, Türkçe metinlerde yapay zeka izi bırakan örüntülerin kataloğudur. Her örüntü aynı şablonu kullanan bağımsız bir bloktur. Yeni bir örüntü eklemek için en alttaki şablonu kopyalayıp doldurmanız yeterli. Ayrıntılı katkı kuralları için deponun `CONTRIBUTING.md` dosyasına bakın.

**Okuma notu (skill için):** Bu bir yasak listesi değildir. "Bu bağlamda" sözü tek başına yanlış değildir. Sorun, bu tür kalıpların yığılması ve metni içi boş bir resmiyetle doldurmasıdır. Her bloktaki **Dokunma** satırı, örüntünün meşru olduğu durumları gösterir. Bir örüntüyü kaldırırken anlamın, sayıların, terimlerin ve özel isimlerin aynen korunması şarttır.

### Kategoriler

| Önek | Kategori |
|---|---|
| `YAPI` | Cümle ve paragraf yapısı |
| `SOZ` | Klişe ve şişirilmiş sözcük seçimi |
| `CEV` | İngilizceden çeviri kokan ifadeler |
| `NOK` | Noktalama ve tipografi |
| `BIC` | Biçim ve düzen (başlık, madde, kalın yazı) |
| `DOL` | Açılış ve kapanış dolguları |
| `YAZ` | Yazım hataları |
| `ASI` | Aşırı düzeltme (düzeltirken bırakılan yeni izler) |

### Dizin

- [YAPI-01 Tekdüze dizilim ve eşit cümle uzunluğu](#yapi-01)
- [YAPI-02 ve/ama/çünkü tekeli](#yapi-02)
- [YAPI-03 -mektedir/-maktadır yığılması](#yapi-03)
- [YAPI-04 Gereksiz edilgen yapı](#yapi-04)
- [YAPI-05 Üçlü sıralama alışkanlığı](#yapi-05)
- [YAPI-06 "Sadece X değil, aynı zamanda Y" kalıbı](#yapi-06)
- [YAPI-07 Kendi sorup kendi cevaplama](#yapi-07)
- [YAPI-08 Her paragrafı özet cümlesiyle bitirme](#yapi-08)
- [YAPI-09 Yarık cümle ve arkadan eklenen açıklama](#yapi-09)
- [SOZ-01 "Önemli bir rol oynamaktadır" ailesi](#soz-01)
- [SOZ-02 Geçiş ve bağlam klişeleri](#soz-02)
- [SOZ-03 Pekiştirme şişirmesi](#soz-03)
- [SOZ-04 "olarak" ve "-mekte olup" fazlalığı](#soz-04)
- [SOZ-05 "Bu durum" / "Bu da" ile açılış](#soz-05)
- [SOZ-06 Gösterişli mecaz öbekleri](#soz-06)
- [SOZ-07 Adlaştırma zinciri ve boş yardımcı fiil](#soz-07)
- [CEV-01 Çeviri deyimler](#cev-01)
- [CEV-02 "-e sahip olmak" fazlalığı](#cev-02)
- [CEV-03 "tarafından" ve "için" yığılması](#cev-03)
- [CEV-04 Gereksiz iyelik zamiri ve "bir"](#cev-04)
- [CEV-05 "bir şekilde" zarfları](#cev-05)
- [CEV-06 Okunuşa uymayan ek](#cev-06)
- [NOK-01 Cümle içinde uzun çizgi (—)](#nok-01)
- [NOK-02 "ve"den önce virgül](#nok-02)
- [NOK-03 İngilizce sayı ve yüzde biçimi](#nok-03)
- [NOK-04 Ünlem ve emoji bolluğu](#nok-04)
- [BIC-01 Gereksiz başlık, madde işareti ve kalın yazı](#bic-01)
- [BIC-02 Kalın etiketli madde](#bic-02)
- [DOL-01 Açılış dolguları](#dol-01)
- [DOL-02 Kapanış dolguları](#dol-02)
- [YAZ-01 Bağlaç de/da](#yaz-01)
- [YAZ-02 ki](#yaz-02)
- [YAZ-03 Soru eki mi](#yaz-03)
- [YAZ-04 Kesme işareti](#yaz-04)
- [YAZ-05 Büyük harf](#yaz-05)
- [YAZ-06 Sık yazım hataları](#yaz-06)
- [ASI-01 Yedek sözcük tiki](#asi-01)
- [ASI-02 Kılık değiştiren kalıp](#asi-02)
- [ASI-03 Sahte samimiyet](#asi-03)
- [ASI-04 Arı Türkçe merakı](#asi-04)
- [ASI-05 Aşırı gömme](#asi-05)

---

<a id="yapi-01"></a>
#### YAPI-01 · Tekdüze dizilim ve eşit cümle uzunluğu

- **Belirti:** Paragraftaki cümlelerin neredeyse hepsi özne + tümleç + nesne + yüklem sırasında ve 14-22 sözcük arasında. Cümle başları birbirine benziyor.
- **Neden yapay:** İnsan yazısında uzunluk dalgalanır. Kısa bir cümle vurgu yapar, uzun bir cümle bağlamı açar. Dil modelleri ise "güvenli" orta uzunlukta toplanır.
- **Ne yapmalı:** Bir iki cümleyi birleştirin (zarf-fiil, sıfat-fiil), birini kısaltın, bir iki cümlede öğe sırasını değiştirin. Araçlar için bkz. `cumle-turleri.md`.
- **Dokunma:** Teknik talimat, sözleşme maddesi ve adım adım kılavuzda düzenli yapı bir erdemdir.
- **Önce:** *Şirketimiz 2015 yılında İzmir'de kurulmuştur. Ekibimiz yazılım geliştirme alanında uzmanlaşmış kişilerden oluşmaktadır. Müşterilerimize uçtan uca çözümler sunmaktayız. Projelerimizde çevik yöntemleri benimsemekteyiz.*
- **Sonra:** *2015'te İzmir'de kurulduk. Yazılım geliştirmede uzmanlaşmış ekibimizle müşterilerimize uçtan uca çözümler sunuyoruz. Projelerde çevik yöntemlerle çalışıyoruz.*

<a id="yapi-02"></a>
#### YAPI-02 · ve/ama/çünkü tekeli

- **Belirti:** Bir paragrafta "ve" üçten çok, "ama" ya da "çünkü" ikiden çok geçiyor. Cümleler hep bu üç bağlaçla bağlanıyor.
- **Neden yapay:** Türkçede iki cümleyi bağlamanın en doğal yolu çoğu zaman bağlaç değil, ektir (-ıp, -ınca, -dığı için). Ayrıca karşıtlık ve sebep için çok zengin bir bağlaç envanteri vardır. Modeller İngilizcedeki *and/but/because* düzenini taşır.
- **Ne yapmalı:** Önce bağlacı silmeyi deneyin (nokta, virgül, zarf-fiil, "da/de"). Gerekiyorsa ilişkiye en uygun bağlacı seçin. Bkz. `baglaclar.md`.
- **Dokunma:** Sayılan öğeler arasındaki "ve" ("elma ve armut") doğaldır. Tek bir "ama" ya da "çünkü" sorun değildir.
- **Önce:** *Uygulama hızlı ve kullanımı kolay ama bazı özellikler eksik çünkü ekip küçük ve kaynaklar sınırlı.*
- **Sonra:** *Uygulama hızlı, kullanımı da kolay. Yine de bazı özellikler eksik: Ekip küçük, kaynaklar sınırlı.*

<a id="yapi-03"></a>
#### YAPI-03 · -mektedir/-maktadır yığılması

- **Belirti:** Art arda cümleler "-mektedir, -maktadır, -ilmektedir, -mekteyiz" ile bitiyor.
- **Neden yapay:** Bu çekim resmi yazıda yerindedir, ama her cümlede kullanıldığında metin bürokratik ve ağır bir hal alır. İnsanlar resmi yazıda bile geniş zamanı (-ır/-ar), şimdiki zamanı (-yor) ve -dır'lı isim cümlesini karıştırarak kullanır.
- **Ne yapmalı:** Gündelik ve yarı resmi metinde çoğunu "-yor" ya da geniş zamana çevirin. Akademik ve resmi metinde bir kısmını koruyun, ama hepsini aynı ekle bitirmeyin: biri geniş zaman, biri isim cümlesi olabilir.
- **Dokunma:** Resmi yazışmada, mevzuat dilinde ve akademik metinde bu çekim registerin parçasıdır. Tamamen kaldırmayın, yalnızca yoğunluğunu azaltın.
- **Önce:** *Proje kapsamında veriler toplanmaktadır. Toplanan veriler analiz edilmektedir. Analiz sonuçları raporlanmaktadır.*
- **Sonra (gündelik):** *Projede önce verileri topluyoruz, sonra analiz edip raporluyoruz.*
- **Sonra (akademik):** *Proje kapsamında toplanan veriler analiz edilerek raporlanmaktadır.*

<a id="yapi-04"></a>
#### YAPI-04 · Gereksiz edilgen yapı

- **Belirti:** Eylemi yapan belli olduğu hâlde edilgen kullanılıyor: "tarafımızca incelenmiştir", "kararlaştırılmıştır", "tavsiye edilmektedir".
- **Neden yapay:** Edilgen yapı nesnellik görüntüsü verir. Ancak eylemi yapan biliniyorsa metni dolaylı ve kaçamak gösterir.
- **Ne yapmalı:** Özne metinde açıkça varsa ya da konuşan belliyse etken yapıya çevirin. Özne belli değilse uydurmayın.
- **Dokunma:** Akademik yöntem bölümleri ("Örneklem rastgele seçilmiştir.") ve öznenin önemsiz olduğu durumlar.
- **Önce:** *Talebiniz tarafımızca incelenmiş olup gerekli düzenlemelerin yapılmasına karar verilmiştir.*
- **Sonra:** *Talebinizi inceledik ve gerekli düzenlemeleri yapmaya karar verdik.*

<a id="yapi-05"></a>
#### YAPI-05 · Üçlü sıralama alışkanlığı

- **Belirti:** Sıfatlar, örnekler ve maddeler hep üçlü geliyor: "hızlı, güvenilir ve ölçeklenebilir", "verimlilik, şeffaflık ve sürdürülebilirlik".
- **Neden yapay:** Üçlü dizi retorikte güçlü bir kalıptır, ama modeller bunu bir refleks gibi her yerde kullanır. Üçüncü öğe çoğu zaman bilgi taşımaz, ritmi tamamlamak için eklenmiştir.
- **Ne yapmalı:** Gerçekten üç ayrı bilgi varsa koruyun. Biri ötekilerin tekrarıysa ya da boşsa (ve kaldırmak bilgi kaybına yol açmıyorsa) çıkarın ya da sayıyı değiştirin. **Dikkat:** Kaynakta somut bilgi taşıyan öğeyi silmek bilgi çıkarmaktır, yasaktır.
- **Dokunma:** Teknik özellik listeleri ve kaynakta gerçekten üç olgu sayılan cümleler.
- **Önce:** *Yeni panelimiz sezgisel, kullanıcı dostu ve kolay anlaşılır bir arayüz sunuyor.*
- **Sonra:** *Yeni panelin arayüzü kolay anlaşılıyor.* (Üç sıfat aynı şeyi söylüyor.)

<a id="yapi-06"></a>
#### YAPI-06 · "Sadece X değil, aynı zamanda Y" kalıbı

- **Belirti:** "Bu sadece bir X değil, aynı zamanda bir Y", "Bu bir X değil, bir Y" kalıbı metinde tekrar ediyor.
- **Neden yapay:** İngilizce *not just X, but Y* kalıbının çevirisidir. Bir kez etkili olabilir. Tekrarlandığında yapay bir dramatiklik yaratır.
- **Ne yapmalı:** Doğrudan söyleyin. İki bilgi de önemliyse "hem ... hem" ya da iki ayrı cümle kullanın.
- **Dokunma:** Gerçek bir yanlış anlamayı düzelten tek bir kullanım ("Bu bir hata değil, bilinçli bir tercih.").
- **Önce:** *Bu uygulama sadece bir not defteri değil, aynı zamanda kişisel bir verimlilik asistanı.*
- **Sonra:** *Uygulama not almanın yanında verimliliğinizi artırmanıza da yardım ediyor.*

<a id="yapi-07"></a>
#### YAPI-07 · Kendi sorup kendi cevaplama

- **Belirti:** "Peki bu ne anlama geliyor?", "Peki neden?", "Sonuç mu? ..." gibi sorular ve hemen ardından cevapları.
- **Neden yapay:** Okurun aklından geçmeyen bir soruyu sahnelemek, metne sahte bir konuşma havası verir.
- **Ne yapmalı:** Soruyu silip cevabı doğrudan söyleyin.
- **Dokunma:** Gerçekten okurun soracağı bir soruysa (SSS bölümü, öğretici bir blog) ve metinde bir kez geçiyorsa.
- **Önce:** *Peki bu değişiklik kullanıcılar için ne anlama geliyor? Kısacası, daha hızlı bir deneyim.*
- **Sonra:** *Değişiklikten sonra uygulama kullanıcılar için daha hızlı çalışıyor.*

<a id="yapi-08"></a>
#### YAPI-08 · Her paragrafı özet cümlesiyle bitirme

- **Belirti:** Paragraflar az önce söyleneni tekrar eden bir cümleyle bitiyor: "Bu da gösteriyor ki ...", "Kısacası ...", "Dolayısıyla X büyük önem taşımaktadır."
- **Neden yapay:** Modeller her bölümü kapatma eğilimindedir. Okur ise aynı bilgiyi ikinci kez okumaya ihtiyaç duymaz.
- **Ne yapmalı:** Yeni bilgi taşımayan kapanış cümlesini silin. Yeni bilgi taşıyorsa (bir çıkarım, sonuç) yalnızca o kısmı tutun.
- **Dokunma:** Uzun raporların ve akademik makalelerin sonuç bölümü.
- **Önce:** *Kargo süresi 5 günden 2 güne indi, iade oranı %8'den %3'e düştü. Bu da müşteri memnuniyetinin ne kadar önemli olduğunu açıkça göstermektedir.*
- **Sonra:** *Kargo süresi 5 günden 2 güne indi, iade oranı %8'den %3'e düştü.*

<a id="yapi-09"></a>
#### YAPI-09 · Yarık cümle ve arkadan eklenen açıklama

- **Belirti:** "Bunu mümkün kılan şey ...", "Asıl önemli olan şey ...-dır", "Dikkat çeken nokta şu ki ..." gibi vurguyu yapay bir özneyle kuran cümleler. Bir de adı söyleyip niteliğini ardından ayrı cümleyle ekleyen çiftler: "Bir rapor hazırladık. Bu rapor geçen yılın satışlarını gösteriyor."
- **Neden yapay:** İkisi de İngilizce cümle sırasının izidir (*what makes this possible is ...*, *a report that shows ...*). Türkçe vurguyu yüklemin hemen önüne gelen öğeyle verir, niteleyeni de adın önüne koyar.
- **Ne yapmalı:** Vurgulanan öğeyi yüklemin önüne alın, "şey"i atın. Arkadan gelen açıklamayı sıfat-fiille adın önüne taşıyın. Araçlar için bkz. `cumle-turleri.md`.
- **Dokunma:** Gerçek bir karşıtlık kuruluyorsa ("Bizi geciktiren bütçe değil, onay süreciydi."). Akademik metinde tanım cümleleri.
- **Önce:** *Teslimatı hızlandıran şey yeni depo oldu. Bir takip ekranı da ekledik. Bu ekran siparişin nerede olduğunu gösteriyor.*
- **Sonra:** *Teslimatı yeni depo hızlandırdı. Siparişin nerede olduğunu gösteren bir takip ekranı da ekledik.*

---

<a id="soz-01"></a>
#### SOZ-01 · "Önemli bir rol oynamaktadır" ailesi

- **Belirti:** önemli bir rol oynamaktadır, büyük önem taşımaktadır, kritik bir öneme sahiptir, vazgeçilmez bir unsurdur, ayrılmaz bir parçasıdır, hayati önem arz etmektedir.
- **Neden yapay:** Bu kalıplar bir şeyin önemli olduğunu söyler ama neden önemli olduğunu söylemez. Yerini somut bir yükleme bırakmalıdır.
- **Ne yapmalı:** Önemin ne olduğunu söyleyen fiili bulun ("etkiler", "belirler", "sağlar", "düşürür"). Kaynakta bu bilgi yoksa daha sade bir ifadeye indirin ("önemlidir"). Bilgi uydurmayın.
- **Dokunma:** Akademik metinde ölçülü ve tek kullanım.
- **Önce:** *Düzenli uyku, öğrencilerin akademik başarısında önemli bir rol oynamaktadır.*
- **Sonra:** *Düzenli uyku, öğrencilerin akademik başarısını etkiler.*

<a id="soz-02"></a>
#### SOZ-02 · Geçiş ve bağlam klişeleri

- **Belirti:** bu bağlamda, bu çerçevede, söz konusu, göz önünde bulundurulduğunda, dikkate alındığında, günümüzde, son yıllarda, hızla gelişen dünyada, teknolojinin hızla ilerlediği günümüzde, sonuç olarak.
- **Neden yapay:** Bu sözler cümleler arasında bir bağ varmış izlenimi verir ama çoğu zaman hiçbir şey bağlamaz. "Günümüzde" ile başlayan açılış, yapay zekanın en tanıdık imzalarından biridir.
- **Ne yapmalı:** Silin ve cümlenin hâlâ ayakta durup durmadığına bakın. Çoğu zaman durur. "Söz konusu X"i "bu X" ya da yalnızca "X" yapın.
- **Dokunma:** Resmi yazışmada "söz konusu" belirli bir belgeyi işaret ediyorsa ("söz konusu sözleşme") kalabilir.
- **Önce:** *Teknolojinin hızla geliştiği günümüzde, yapay zeka birçok sektörü dönüştürmektedir. Bu bağlamda, söz konusu dönüşüm göz önünde bulundurulduğunda şirketlerin hazırlıklı olması gerekmektedir.*
- **Sonra:** *Yapay zeka birçok sektörü dönüştürüyor ve şirketlerin buna hazırlanması gerekiyor.*

<a id="soz-03"></a>
#### SOZ-03 · Pekiştirme şişirmesi

- **Belirti:** oldukça, son derece, büyük ölçüde, son derece önemli, kritik, kilit, eşsiz, benzersiz, muazzam, inanılmaz, devrim niteliğinde.
- **Neden yapay:** Her şey "son derece" önemli olunca hiçbir şey önemli olmaz. Modeller tarafsız bilgiyi pekiştirmelerle süsler.
- **Ne yapmalı:** Pekiştirmeyi silin. Gerçek bir derece bilgisi varsa sayı ya da somut karşılaştırmayla verin (kaynakta varsa).
- **Dokunma:** Kaynakta ölçülebilir bir karşılığı olan tek bir pekiştirme.
- **Önce:** *Bu son derece kritik güncelleme, sistemin performansını büyük ölçüde artırarak eşsiz bir deneyim sunuyor.*
- **Sonra:** *Bu güncelleme sistemin performansını artırıyor.*

<a id="soz-04"></a>
#### SOZ-04 · "olarak" ve "-mekte olup" fazlalığı

- **Belirti:** "şirket olarak", "ekip olarak", "genel olarak", "temel olarak", "aktif olarak", "düzenli olarak"; "-mekte olup", "-miş olup".
- **Neden yapay:** "Olarak" çoğu yerde bilgi taşımaz. "-mekte olup" ise iki cümleyi resmi yazışma havasında yapıştırır.
- **Ne yapmalı:** "Olarak"ı silin ya da ekle karşılayın ("düzenli olarak" → "düzenli"). "-mekte olup"u iki cümleye bölün ya da zarf-fiil kullanın.
- **Dokunma:** "Şirket olarak" konuşanın kurum adına konuştuğunu vurgulamak için bir kez kullanılabilir.
- **Önce:** *Şirket olarak müşterilerimizle aktif olarak iletişim kurmakta olup geri bildirimleri düzenli olarak değerlendirmekteyiz.*
- **Sonra:** *Müşterilerimizle sürekli iletişim kuruyor, geri bildirimleri düzenli değerlendiriyoruz.*

<a id="soz-05"></a>
#### SOZ-05 · "Bu durum" / "Bu da" ile açılış

- **Belirti:** Art arda cümleler "Bu durum ...", "Bu da ...", "Bu sayede ...", "Bu noktada ..." ile başlıyor.
- **Neden yapay:** Cümleler arasında bağ kurmak için modeller önceki cümlenin tamamını "bu" ile işaret eder. Sık tekrarlanınca metin zincirleme bir hâl alır.
- **Ne yapmalı:** İki cümleyi birleştirin (sıfat-fiil, zarf-fiil) ya da "bu"nun neyi işaret ettiğini adıyla söyleyin.
- **Dokunma:** Bir paragrafta bir kez.
- **Önce:** *Sunucular yeni veri merkezine taşındı. Bu durum gecikmeyi azalttı. Bu da kullanıcı deneyimini iyileştirdi.*
- **Sonra:** *Sunucuların yeni veri merkezine taşınmasıyla gecikme azaldı, kullanıcı deneyimi iyileşti.*

<a id="soz-06"></a>
#### SOZ-06 · Gösterişli mecaz öbekleri

- **Belirti:** yeni bir boyut kazandırmak, kapılarını aralamak, dönüşüm yolculuğu, yolculuğa çıkmak, yeni bir sayfa açmak, köprü kurmak, ufuk açıcı, çıtayı yükseltmek, potansiyelini açığa çıkarmak.
- **Neden yapay:** Somut bir bilgi yerine duygu yükü taşıyan genel mecazlar kullanılır. Kurumsal ve pazarlama metinlerinde yapay zekanın en bariz izidir.
- **Ne yapmalı:** Mecazın arkasındaki somut iddiayı yazın. Kaynakta somut bir iddia yoksa düz ve sade bir ifadeye indirin.
- **Dokunma:** Edebi metin ve kullanıcının bilinçli üslubu.
- **Önce:** *Bu iş birliği, eğitimde dijital dönüşüm yolculuğumuza yeni bir boyut kazandıracak.*
- **Sonra:** *Bu iş birliğiyle eğitimde dijitalleşme çalışmalarımızı genişleteceğiz.*

<a id="soz-07"></a>
#### SOZ-07 · Adlaştırma zinciri ve boş yardımcı fiil

- **Belirti:** Eylemin ada çevrilip başka bir fiile yüklendiği zincirler: "yedeklenmesinin sağlanması gerekmektedir", "incelemesinin yapılması", "ödemenin gerçekleştirilmesi". Asıl işi ad taşır, "gerçekleştirmek", "sağlamak", "yapmak", "icra etmek" yalnızca çekim eki taşır.
- **Neden yapay:** Bürokratik yazının alışkanlığıdır ve modeller "resmi" görünmek için buna yaslanır. Okur eylemi bulmak için zinciri sondan başa çözmek zorunda kalır.
- **Ne yapmalı:** Addaki eylemi yeniden fiil yapın ve doğrudan çekimleyin: "ödemenin gerçekleştirilmesi" → "ödemek", "yapılması gerekmektedir" → "yapılmalı". Eylemi kimin yaptığı kaynakta belli değilse edilgen bırakın, özne uydurmayın.
- **Dokunma:** Yerleşik birleşik fiiller ("katkıda bulunmak", "yardım etmek", "karar vermek") boş fiil değildir. Mevzuat ve sözleşme dilinde zincir kalıbın parçası olabilir.
- **Önce:** *Verilerin haftalık olarak yedeklenmesinin sağlanması gerekmektedir. Geçiş işlemi cumartesi günü gerçekleştirilecektir.*
- **Sonra:** *Veriler haftada bir yedeklenmeli. Geçiş cumartesi günü yapılacak.*

---

<a id="cev-01"></a>
#### CEV-01 · Çeviri deyimler

- **Belirti:** günün sonunda (*at the end of the day*), derinlemesine dalmak (*deep dive*), oyunun kurallarını değiştiren (*game-changer*), masaya getirmek (*bring to the table*), bir adım öne çıkmak (*step up*), aynı sayfada olmak (*be on the same page*), kutunun dışında düşünmek (*think outside the box*), ileriye dönük (*going forward*), kazan-kazan.
- **Neden yapay:** İngilizce deyimlerin sözcük sözcük çevirisidir. Türkçe okur bunları ya yadırgar ya da "plaza dili" olarak algılar.
- **Ne yapmalı:** Türkçe karşılığını ya da düz anlamını kullanın: günün sonunda → sonuçta / nihayetinde; derinlemesine dalmak → ayrıntılı incelemek; oyunun kurallarını değiştiren → alışılmış düzeni değiştiren / çığır açan (ölçülü); masaya getirmek → katmak, sunmak; aynı sayfada olmak → aynı fikirde olmak, uzlaşmak.
- **Dokunma:** Kullanıcı bilinçli olarak plaza dili ya da ironik bir dil kullanıyorsa.
- **Önce:** *Bu yazıda yapay zekanın eğitimdeki rolüne derinlemesine dalacağız. Günün sonunda, bu teknoloji oyunun kurallarını değiştiren bir güç.*
- **Sonra:** *Bu yazıda yapay zekanın eğitimdeki yerini ayrıntılı olarak inceliyoruz. Sonuçta bu teknoloji, öğretimin alışılmış düzenini değiştiriyor.*

<a id="cev-02"></a>
#### CEV-02 · "-e sahip olmak" fazlalığı

- **Belirti:** "geniş bir deneyime sahip", "yüksek bir performansa sahiptir", "üç odaya sahip", "önemli bir yere sahiptir".
- **Neden yapay:** İngilizce *have/has* yapısının çevirisidir. Türkçe bunu çoğu zaman "-lı/-li", "var" ya da doğrudan sıfatla söyler.
- **Ne yapmalı:** "-lı/-li" ekini, "var/yok" yapısını ya da isim cümlesini kullanın.
- **Dokunma:** Mülkiyet ya da hak vurgusu ("şirketin %51'ine sahip", "telif hakkına sahip").
- **Önce:** *Ekibimiz geniş bir deneyime sahip olup ürünümüz yüksek bir performansa sahiptir.*
- **Sonra:** *Ekibimiz deneyimli, ürünümüz de yüksek performanslı.*

<a id="cev-03"></a>
#### CEV-03 · "tarafından" ve "için" yığılması

- **Belirti:** "X tarafından geliştirilen Y tarafından kullanılan", "bu, kullanıcılar için önemlidir", "işletmeler için faydalı olmak".
- **Neden yapay:** İngilizce *by* ve *for* yapılarının çevirisidir. Türkçede etken çatı ve yönelme durumu daha doğaldır.
- **Ne yapmalı:** "X tarafından yapılan" → "X'in yaptığı". "Y için önemli" → bağlama göre "Y'yi ilgilendirir", "Y'nin işine yarar".
- **Dokunma:** Resmi yazışmada ve akademik metinde tek bir "tarafından". Kurum adı geçen resmi bildirimler.
- **Önce:** *Ekibimiz tarafından geliştirilen bu araç, küçük işletmeler için oldukça faydalı olacaktır.*
- **Sonra:** *Ekibimizin geliştirdiği bu araç küçük işletmelerin işine yarayacak.*

<a id="cev-04"></a>
#### CEV-04 · Gereksiz iyelik zamiri ve "bir"

- **Belirti:** "bizim ekibimiz", "sizin hesabınız", "onun fikri" (iyelik eki zaten varken). "Bir" sözcüğünün belirsiz tanımlık (*a/an*) gibi her ada eklenmesi: "harika bir fırsat sunan bir platform".
- **Neden yapay:** Türkçede iyelik eki kişiyi zaten gösterir. Zamir yalnızca vurgu için kullanılır. "Bir" ise İngilizcedeki tanımlık refleksiyle çoğalır.
- **Ne yapmalı:** Vurgu yoksa zamiri silin. Fazladan "bir"leri ayıklayın.
- **Dokunma:** Karşıtlık vurgusu ("Bizim ekibimiz değil, onların ekibi yaptı.").
- **Önce:** *Bizim ekibimiz sizin projeniz için harika bir çözüm sunan bir yaklaşım geliştirdi.*
- **Sonra:** *Ekibimiz projeniz için yeni bir yaklaşım geliştirdi.* ("harika" bilgi taşımıyor. "çözüm sunan" ise "yaklaşım"ın tekrarı.)

<a id="cev-05"></a>
#### CEV-05 · "bir şekilde" zarfları

- **Belirti:** "hızlı bir şekilde", "etkili bir biçimde", "sorunsuz bir şekilde", "güvenli bir şekilde", "detaylı bir şekilde".
- **Neden yapay:** İngilizce *-ly* zarflarının sözcük sözcük karşılığıdır. Türkçede sıfat çoğu zaman olduğu gibi zarf olur ("hızlı yürüdü") ya da "-ca/-ce" ekini alır.
- **Ne yapmalı:** "bir şekilde"yi silip sıfatı yalın bırakın ya da "-ca/-ce", "-arak" kullanın. Zarf bilgi taşımıyorsa ("sorunsuz bir şekilde çalışır") tamamen atın.
- **Dokunma:** Belirsizlik bildiren gerçek kullanım ("bir şekilde hallettik", "öyle ya da böyle" anlamında).
- **Önce:** *Dosyalarınızı güvenli bir şekilde saklar, ekibinizle hızlı bir şekilde paylaşmanıza olanak tanır.*
- **Sonra:** *Dosyalarınızı güvenle saklar, ekibinizle hızlıca paylaşmanızı sağlar.*

<a id="cev-06"></a>
#### CEV-06 · Okunuşa uymayan ek

- **Belirti:** Yabancı sözcüğe ya da kısaltmaya gelen ekin okunuşa değil yazılışa göre seçilmesi: "cache'ı", "Slack'de", "Chrome'yi", "TDK'ya".
- **Neden yapay:** Model eki sözcüğün son harfine bakarak seçer. Türkçe yazan biri sözcüğü nasıl okuyorsa eki ona göre getirir.
- **Ne yapmalı:** Eki okunuşa uydurun: "cache'i" (keş), "Slack'te" (silek), "Chrome'u" (krom). Kısaltmalarda kural TDK'dandır, yabancı sözcüklerde yerleşik uygulamadır. Bkz. `noktalama.md` §5. Terimin kendisine dokunmayın.
- **Dokunma:** Okunuşu kişiden kişiye değişen sözcükler ("SQL": es-kü-el ya da sikıl). Metindeki tercih tutarlıysa kalır.
- **Önce:** *Yayına almadan önce cache'ı temizleyip durumu Slack'de duyurduk.*
- **Sonra:** *Yayına almadan önce cache'i temizleyip durumu Slack'te duyurduk.*

---

<a id="nok-01"></a>
#### NOK-01 · Cümle içinde uzun çizgi (—)

- **Belirti:** Cümle içinde ara söz, açıklama ya da ani dönüş için "—" kullanılıyor.
- **Neden yapay:** TDK'ya göre uzun çizgi yalnızca satır başındaki konuşmaları gösterir. Cümle içindeki kullanım İngilizce tipografiden gelir ve yapay zeka metinlerinin en kolay fark edilen izidir.
- **Ne yapmalı:** Ara söz için virgül, -kısa çizgi- ya da ayraç. Açıklama için iki nokta. Ani dönüş için nokta ve yeni cümle. Bkz. `noktalama.md` §1.
- **Dokunma:** Satır başındaki diyalog çizgisi. Kullanıcının açıkça korumak istediği tipografi.
- **Önce:** *Toplantıda tek bir konu konuşuldu — bütçe. Herkes — finans ekibi de dahil — şaşırdı.*
- **Sonra:** *Toplantıda tek bir konu konuşuldu: bütçe. Finans ekibi de dâhil herkes şaşırdı.*

<a id="nok-02"></a>
#### NOK-02 · "ve"den önce virgül

- **Belirti:** Sıralamada son öğeden önce "..., ve ..." (Oxford virgülü).
- **Neden yapay:** İngilizce noktalama kuralıdır. TDK'ya göre "ve, veya, ya da" öncesine virgül konmaz.
- **Ne yapmalı:** Virgülü silin.
- **Dokunma:** —
- **Önce:** *Tasarım, geliştirme, ve test aşamaları tamamlandı.*
- **Sonra:** *Tasarım, geliştirme ve test aşamaları tamamlandı.*

<a id="nok-03"></a>
#### NOK-03 · İngilizce sayı ve yüzde biçimi

- **Belirti:** *25%*, *3.5 milyon*, *1,200 kişi*.
- **Neden yapay:** Türkçede yüzde işareti önde (*%25*), ondalık ayırıcı virgül (*3,5*), binlik ayırıcı noktadır (*1.200*).
- **Ne yapmalı:** Biçimi düzeltin, **değeri asla değiştirmeyin.** "1,200" ifadesinin binlik mi ondalık mı olduğu bağlamdan net değilse dokunmayın ve özette belirtin.
- **Dokunma:** Kod, sürüm numarası (*v2.5*), IP adresi, ürün kodu, alıntılanmış İngilizce veri.
- **Önce:** *Satışlar 12.5% artarak 3,400 adede ulaştı.*
- **Sonra:** *Satışlar %12,5 artarak 3.400 adede ulaştı.*

<a id="nok-04"></a>
#### NOK-04 · Ünlem ve emoji bolluğu

- **Belirti:** Her paragraf ünlemle bitiyor. Madde başlarında 🚀 ✅ 💡 gibi emojiler var.
- **Neden yapay:** Sosyal medya için üretilmiş yapay zeka metninin tipik süslemesidir.
- **Ne yapmalı:** Ünlemleri metin başına en fazla bire indirin. Emojileri, kullanıcı açıkça istemedikçe kaldırın ya da bire indirin.
- **Dokunma:** Kullanıcının kendi markasının bilinçli sosyal medya dili.
- **Önce:** *Büyük haber! 🚀 Yeni ürünümüz yayında! Hemen deneyin! 💡*
- **Sonra:** *Yeni ürünümüz yayında. Hemen deneyebilirsiniz!*

---

<a id="bic-01"></a>
#### BIC-01 · Gereksiz başlık, madde işareti ve kalın yazı

- **Belirti:** Üç paragraflık bir e-postada başlıklar, her cümlenin madde işaretine dönüşmesi, cümle ortalarında **kalın** yazılmış sözcükler.
- **Neden yapay:** Modeller her metni bir rapor gibi yapılandırır. Akıcı bir metin parçalanınca okur bağlantıları kendisi kurmak zorunda kalır.
- **Ne yapmalı:** Kısa metinde başlıkları kaldırın. Birbiriyle ilişkili maddeleri düzyazıya çevirin. Kalın yazıyı yalnızca gerçekten taranacak bilgi (tarih, son gün) için bırakın. **İçerik aynen korunmalıdır:** Maddedeki her bilgi düzyazıda da yer almalıdır.
- **Dokunma:** Adım adım talimatlar, gerçekten taranacak listeler, kullanıcının belirlediği şablon.
- **Önce:**
  ```
  **Konu:** Toplantı
  **Tarih:** Perşembe
  - Toplantı perşembe günü yapılacaktır.
  - Gündem bütçe planlamasıdır.
  - Katılım önemlidir.
  ```
- **Sonra:** *Perşembe günü bütçe planlamasını konuşmak için toplanıyoruz. Katılımınız önemli.*

<a id="bic-02"></a>
#### BIC-02 · Kalın etiketli madde

- **Belirti:** Her maddenin kalın bir etiket ve iki noktayla başladığı listeler: "**Hız:** Sayfalar daha çabuk açılır.", "**Güvenlik:** Veriler şifrelenir." Çoğu zaman etiket, ardından gelen cümlenin bir sözcüğünü tekrar eder.
- **Neden yapay:** Sohbet modellerinin en tanıdık cevap şablonudur. Düz bir paragrafla söylenebilecek iki üç bilgiyi sunum slaytına çevirir.
- **Ne yapmalı:** Madde sayısı azsa düzyazıya çevirin. Liste gerçekten gerekiyorsa etiketi kaldırıp maddeyi yalın bir cümle olarak yazın. Etiketteki bilgi cümlede yoksa cümleye taşıyın, kaybetmeyin.
- **Dokunma:** Sözlükçe, özellik tablosu, SSS gibi etiketin gerçekten aranacak bir başlık olduğu listeler. Kullanıcının şablonu.
- **Önce:**
  ```
  - **Hız:** Yeni sürümde sayfalar daha hızlı açılır.
  - **Güvenlik:** Bütün veriler şifrelenerek saklanır.
  ```
- **Sonra:** *Yeni sürümde sayfalar daha hızlı açılır, bütün veriler de şifrelenerek saklanır.*

---

<a id="dol-01"></a>
#### DOL-01 · Açılış dolguları

- **Belirti:** "Harika bir soru!", "Elbette!", "Tabii ki, işte ...", "Bu yazıda ... ele alacağız", "Merhaba! Bugün sizlerle ... paylaşmak istiyorum".
- **Neden yapay:** Sohbet modelinin cevap refleksidir. Metne bilgi katmaz.
- **Ne yapmalı:** Silin, metin doğrudan konuyla başlasın.
- **Dokunma:** Mektup ve e-postadaki olağan selamlama ("Merhaba Ayşe Hanım,").
- **Önce:** *Harika bir soru! Bu yazıda uzaktan çalışmanın avantajlarını ele alacağız.*
- **Sonra:** *Uzaktan çalışmanın birkaç avantajı var.*

<a id="dol-02"></a>
#### DOL-02 · Kapanış dolguları

- **Belirti:** "Umarım yardımcı olur!", "Başka sorunuz olursa çekinmeden sorun.", "Bu konuda daha fazla bilgi almak isterseniz ...", "Unutmayın, ...".
- **Neden yapay:** Sohbet modelinin kapanış refleksidir.
- **Ne yapmalı:** Silin. E-postada gerçek bir iletişim daveti gerekiyorsa sade bir kapanış bırakın ("Sorunuz olursa yazabilirsiniz.").
- **Dokunma:** E-postanın imza bloğu ve olağan kapanışı ("Saygılarımla,").
- **Önce:** *Umarım bu bilgiler size yardımcı olur! Başka bir sorunuz olursa çekinmeden sormaktan lütfen çekinmeyin.*
- **Sonra:** *(silinir)*

---

<a id="yaz-01"></a>
#### YAZ-01 · Bağlaç de/da

- **Belirti:** "bende geliyorum", "Ali'de biliyor", "gidip te".
- **Neden yapay:** Yapay zekadan çok insan hatasıdır, ama metin düzeltilirken yakalanmalıdır.
- **Ne yapmalı:** Bağlaç de/da'yı ayırın, kesmeyi kaldırın, "te/ta"yı "de/da" yapın. Bkz. `noktalama.md` §4.
- **Dokunma:** Bulunma eki (-de/-da/-te/-ta) bitişik kalır.
- **Önce:** *Bende bu toplantıya katılacağım, Elif'te gelecek.*
- **Sonra:** *Ben de bu toplantıya katılacağım, Elif de gelecek.*

<a id="yaz-02"></a>
#### YAZ-02 · ki

- **Belirti:** "demekki", "halbuki" (TDK: hâlbuki), "yarın ki toplantı", "masada ki kitap".
- **Ne yapmalı:** Bağlaç "ki"yi ayırın (yedi kalıplaşmış söz hariç: belki, çünkü, hâlbuki, mademki, meğerki, oysaki, sanki). Ek olan "-ki"yi bitiştirin.
- **Dokunma:** —
- **Önce:** *Yarın ki toplantıda konuşacağız, demekki karar ertelendi.*
- **Sonra:** *Yarınki toplantıda konuşacağız, demek ki karar ertelendi.*

<a id="yaz-03"></a>
#### YAZ-03 · Soru eki mi

- **Belirti:** "gelecekmisin", "doğrumu", "biliyormusun".
- **Ne yapmalı:** Soru ekini ayırın. Sonraki ekleri soru ekine bitiştirin.
- **Dokunma:** —
- **Önce:** *Raporu yarına yetiştirebilecekmisiniz?*
- **Sonra:** *Raporu yarına yetiştirebilecek misiniz?*

<a id="yaz-04"></a>
#### YAZ-04 · Kesme işareti

- **Belirti:** Kurum adlarına kesme ("Türk Dil Kurumu'na"), yapım ekine kesme ("Türkiye'li"), kısaltmaya yanlış ünlü ("TDK'ya").
- **Ne yapmalı:** Kurum adlarında kesmeyi kaldırın, yapım ekinde ayırmayın, kısaltmaya gelen eki okunuşa uydurun. Bkz. `noktalama.md` §5.
- **Dokunma:** Kullanıcının marka adı yazımı (marka kendi adını kesmeyle yazıyorsa). [Tartışmalı, bkz. CONTRIBUTING.]
- **Önce:** *Başvurular Ankara Üniversitesi'ne yapılacak, sonuçlar TDK'ya bildirilecek.*
- **Sonra:** *Başvurular Ankara Üniversitesine yapılacak, sonuçlar TDK'ye bildirilecek.*

<a id="yaz-05"></a>
#### YAZ-05 · Büyük harf

- **Belirti:** "Kasım ayında" (genel zaman), "Türk Lirası" (para birimi), "İstanbul İli", iki noktadan sonra öbeğin büyük harfle başlaması.
- **Ne yapmalı:** Bkz. `noktalama.md` §3 ve §6.
- **Dokunma:** Başlıkların büyük harf düzeni (metin içinde tutarlıysa).
- **Önce:** *Fiyatlar Kasım ayında 500 Türk Lirası'na çıkacak. Üç seçenek var: Aylık, yıllık ve ömür boyu.*
- **Sonra:** *Fiyatlar kasım ayında 500 Türk lirasına çıkacak. Üç seçenek var: aylık, yıllık ve ömür boyu.*

<a id="yaz-06"></a>
#### YAZ-06 · Sık yazım hataları

- **Belirti:** "birşey", "herşey", "hiç bir", "bir çok", "bir kaç", "pekçok", "yada", "yanlız".
- **Neden yapay:** Yapay zekadan çok insan hatasıdır, ama metin düzeltilirken yakalanmalıdır.
- **Ne yapmalı:** Doğru yazımı kullanın: bir şey, her şey, hiçbir, birçok, birkaç, pek çok, ya da, yalnız. Liste için bkz. `noktalama.md` §8.
- **Dokunma:** Alıntılar ve kullanıcının olduğu gibi aktardığı mesajlar.
- **Önce:** *Bir çok kullanıcı herşeyin yolunda olduğunu yada hiç bir sorun yaşamadığını söyledi.*
- **Sonra:** *Birçok kullanıcı her şeyin yolunda olduğunu ya da hiçbir sorun yaşamadığını söyledi.*

---

### Aşırı düzeltme

Bu bölümdeki örüntüler kaynak metinde değil, **düzeltilmiş metinde** aranır. Bir izi silerken yerine yenisini koymak, izi bırakmaktan daha kötüdür: Metin hem değişmiş hem de yine yapay kalmış olur. Yeniden yazımı bitirdikten sonra çıktıyı bu beş soruyla okuyun. Buradaki bloklar önce/sonra yerine kaynak, aşırı düzeltme ve yerinde düzeltme üçlüsünü gösterir.

<a id="asi-01"></a>
#### ASI-01 · Yedek sözcük tiki

- **Belirti:** Silinen klişelerin yerine her seferinde aynı "doğal" sözcük geliyor: "aslında", "açıkçası", "doğrusu", "işin özü", "gerçekten".
- **Neden yapay:** Yasak listesiyle çalışmanın yan etkisidir. Boşalan yere bir şey koyma refleksi, eski tikin yerine yenisini üretir.
- **Ne yapmalı:** Klişeyi sildiğiniz yere hiçbir şey koymadan cümleyi okuyun. Ayakta duruyorsa öyle bırakın.
- **Dokunma:** Kaynak metinde zaten bulunan ve anlam taşıyan söylem sözcükleri.
- **Kaynak:** *Bu bağlamda, yeni panel son derece hızlıdır. Sonuç olarak, kullanıcılar memnundur.*
- **Aşırı düzeltme:** *Aslında yeni panel gerçekten hızlı. Açıkçası kullanıcılar da memnun.*
- **Yerinde düzeltme:** *Yeni panel hızlı, kullanıcılar da memnun.*

<a id="asi-02"></a>
#### ASI-02 · Kılık değiştiren kalıp

- **Belirti:** Bir kalıp silinirken aynı iskeletin başka bir biçimi kuruluyor: "sadece X değil, aynı zamanda Y" yerine "X değil, Y", "X'in ötesinde Y", "X'ten çok Y". Uzun çizgi yerine her yere iki nokta ya da üç nokta konması da aynı hatadır.
- **Neden yapay:** Sözcükler değişir, cümlenin hareketi aynı kalır. Okur kalıbı sözcüklerinden değil ritminden tanır.
- **Ne yapmalı:** Kalıbın arkasındaki bilgiyi çıkarın ve düz söyleyin. Karşıtlığın olumsuz yarısı bilgi taşımıyorsa atın.
- **Dokunma:** Kaynakta gerçek bir yanlış anlamayı düzelten karşıtlık (bkz. YAPI-06, Dokunma).
- **Kaynak:** *Bu sadece bir takvim uygulaması değil, aynı zamanda bir planlama asistanı.*
- **Aşırı düzeltme:** *Bu bir takvim uygulamasından çok, bir planlama asistanı.*
- **Yerinde düzeltme:** *Uygulama takvim tutmanın yanında planlamanıza da yardım ediyor.*

<a id="asi-03"></a>
#### ASI-03 · Sahte samimiyet

- **Belirti:** Metni "insan" göstermek için eklenen ve kaynakta olmayan öğeler: uydurma bir anı, "itiraf edeyim", "hepimizin başına gelmiştir", okura dönük sohbet cümleleri, konuşma dili parçacıkları ("yani", "hani", "işte").
- **Neden yapay:** Bilgi eklemektir, değişmez kuralları çiğner. Kurumsal ya da teknik bir metinde registerı da bozar.
- **Ne yapmalı:** Eklediğiniz her sözcüğü silip okuyun. Anlamdan ve tondan bir şey eksilmiyorsa geri koymayın. Kaynakta olmayan hiçbir deneyim, duygu ya da ayrıntı yazmayın.
- **Dokunma:** Kaynak metindeki gerçek kişisel anlatım. Yazarın kendi anısı ve sesi korunur.
- **Kaynak:** *Yedekleme işlemi her gece 02.00'de otomatik olarak başlamaktadır.*
- **Aşırı düzeltme:** *Hepimiz bir gün dosyalarımızı kaybetmişizdir. İşte bu yüzden yedekleme her gece 02.00'de kendiliğinden başlıyor.*
- **Yerinde düzeltme:** *Yedekleme her gece 02.00'de kendiliğinden başlar.*

<a id="asi-04"></a>
#### ASI-04 · Arı Türkçe merakı

- **Belirti:** Gündelik ve mesleki dilde yaşayan yabancı kökenli sözcüklerin zorlama karşılıklarla değiştirilmesi: "performans" → "başarım", "strateji" → "izlem", "e-posta" → "e-ileti". Meslek içinde İngilizcesiyle kullanılan terimlerin çevrilmesi: "pull request" → "çekme isteği", "middleware" → "ara katman yazılımı".
- **Neden yapay:** Bu skill bir dil arılaştırma aracı değildir. Hedef, okurun yadırgamadığı Türkçedir ve okur "performans" sözcüğünü yadırgamaz. Terim değiştirmek ayrıca değişmez kurallara aykırıdır.
- **Ne yapmalı:** Sözcük seçimine yalnızca çeviri kokan **kalıplarda** (bkz. `CEV` blokları) dokunun. Tek tek sözcüklerin kökenine bakmayın.
- **Dokunma:** Kullanıcı açıkça öz Türkçe bir üslup istiyorsa.
- **Kaynak:** *Yeni strateji, sistemin performansını artırmayı hedeflemektedir.*
- **Aşırı düzeltme:** *Yeni izlem, dizgenin başarımını artırmayı amaçlıyor.*
- **Yerinde düzeltme:** *Yeni strateji sistemin performansını artırmayı hedefliyor.*

<a id="asi-05"></a>
#### ASI-05 · Aşırı gömme

- **Belirti:** Kısa cümleleri birleştirirken bütün bilginin sıfat-fiillerle tek bir adın önüne yığılması. Okur yükleme varana kadar üç dört yan cümleyi aklında tutmak zorunda kalıyor.
- **Neden yapay:** Tekdüzeliği kırmak için yapılan birleştirmenin dozu kaçmıştır. İngilizce iskeletin tersine dönmüş hâli de Türkçe okuru yorar.
- **Ne yapmalı:** Bir adın önünde en çok iki yan cümle bırakın. Fazlasını ayrı cümleye bölün.
- **Dokunma:** Hukuki ve akademik metinde uzun ad öbekleri türün gereği olabilir.
- **Kaynak:** *Bir araç geliştirdik. Araç faturaları tarıyor. Hataları işaretliyor. Geçen ay yayınladık.*
- **Aşırı düzeltme:** *Geçen ay yayınladığımız, faturaları tarayan ve hataları işaretleyen, bizim geliştirdiğimiz aracı kullanabilirsiniz.* (Ayrıca "kullanabilirsiniz" kaynakta yok.)
- **Yerinde düzeltme:** *Faturaları tarayıp hataları işaretleyen bir araç geliştirdik. Geçen ay yayınladık.*

---

### Yeni örüntü şablonu

Aşağıdaki bloğu kopyalayın, uygun kategoriye ekleyin, sıradaki numarayı verin ve dizine bir satır ekleyin.

```markdown
<a id="kat-nn"></a>
#### KAT-NN · Kısa ad

- **Belirti:** Metinde nasıl görünür? Somut sözcükler ya da yapılar.
- **Neden yapay:** İnsan yazısından nasıl ayrışıyor? Kaynağı nedir (çeviri, model refleksi...)?
- **Ne yapmalı:** Hangi dönüşüm uygulanmalı? İlgili referans dosyasına bağlantı verin.
- **Dokunma:** Örüntünün meşru olduğu durumlar. Bu satır zorunludur.
- **Önce:** *Özgün, yapay zeka tarzında bir örnek.*
- **Sonra:** *Anlamı, sayıları ve özel isimleri aynen koruyan düzeltilmiş hali.*
```


---

# Ek: references/cumle-turleri.md

## Cümle çeşitliliği araç kutusu

Ayrıntılı tanımlar ve kaynakça için deponun `kaynaklar/cumle-turleri.md` dosyasına bakın. Bu dosya yalnızca yeniden yazarken lazım olanı içerir: Tekdüze bir paragrafı hangi yapılarla kırabilirsiniz ve her yapı hangi registerda yerindedir?

### Önce teşhis

Tekdüzeliği üç belirtiden tanırsınız:
1. **Uzunluk:** Cümlelerin çoğu 14-22 sözcük arasında ve birbirine yakın.
2. **Başlangıç:** Art arda cümleler aynı öğeyle başlıyor (özne + "ise", "bu" + isim, "-mek" + "için").
3. **Bitiş:** Yüklemler aynı ekle bitiyor (-mektedir, -maktadır, -ilmektedir, -dır).

Bunlardan ikisi bir paragrafta varsa ritim sorunu var demektir. Yalnızca biri varsa ve metin resmiyse dokunmamak da bir seçenektir.

### Araçlar (registera göre)

Sütunlar: G = gündelik/blog/sosyal, İ = iş e-postası/ürün metni, A = akademik/resmi.

| Araç | Ne yapar | G | İ | A |
|---|---|---|---|---|
| **Kısa basit cümle** (3-7 sözcük) | Uzun cümlelerin arasında vurgu yaratır | ✔ | ✔ | ölçülü |
| **Öğe sırasını değiştirme** (kurallı cümle içinde) | Vurguyu yükleme yakın öğeye kaydırır, cümle başlarını çeşitlendirir | ✔ | ✔ | ✔ |
| **Zarf-fiille birleştirme** (-ıp, -ınca, -arak, -dıkça, -madan) | İki "ve"li cümleyi tek ve Türkçe bir cümleye çevirir | ✔ | ✔ | ✔ |
| **Sıfat-fiille gömme** (-an, -dığı, -acak) | "X var. X şunu yapar." çiftini tek cümle yapar | ✔ | ✔ | ✔ |
| **Sıralı cümle** (virgülle) | "ve ... ve ..." zincirini hızlandırır | ✔ | ✔ | noktalı virgülle |
| **Bağlaç çeşitlendirme** | ve/ama/çünkü tekelini kırar (bkz. baglaclar.md) | ✔ | ✔ | ✔ |
| **İsim cümlesi, -dır düşürülmüş** | Ağır fiil cümlelerinin arasında nefes aldırır | ✔ | ✔ | ✘ (-dır korunur) |
| **Ki'li cümle** | Vurguyu başa çeker, sözlü canlılık katar | ✔ | ölçülü | seyrek |
| **Gerçek soru** | Açıklama dizisini kırar | ölçülü | seyrek | çok seyrek |
| **Devrik cümle** | Duygu, vurgu, konuşma tonu katar | paragrafta en çok 1 | seyrek | ✘ |
| **Eksiltili cümle** | Konuşma diline en yakın vurgu | metinde en çok 1-2 | seyrek | ✘ |
| **Doğrudan emir** | "yapılması gerekmektedir" yerine | ✔ | ✔ | resmi yazışmada ölçülü |

### Dönüşüm kalıpları

**1. "ve" ile bağlanmış iki fiil → zarf-fiil**
- Önce: *Kullanıcı formu doldurur ve gönder butonuna basar.*
- Sonra: *Kullanıcı formu doldurup gönder butonuna basar.*

**2. Art arda iki cümlede aynı özne → sıfat-fiil ya da birleştirme**
- Önce: *Yeni uygulama geçen ay yayınlandı. Uygulama şimdiden 10.000 kullanıcıya ulaştı.*
- Sonra: *Geçen ay yayınlanan uygulama şimdiden 10.000 kullanıcıya ulaştı.*

**3. Eşit uzunlukta üç cümle → biri kısa, biri uzun**
- Önce: *Ekip yeni özellik üzerinde yoğun bir şekilde çalışmaktadır. Testler önümüzdeki hafta tamamlanacaktır. Sürümün ay sonunda yayınlanması planlanmaktadır.*
- Sonra: *Ekip yeni özellik üzerinde çalışıyor. Testler gelecek hafta bitince sürümü ay sonunda yayınlamayı planlıyoruz.*
- (Dikkat: Buradaki "planlıyoruz" öznenin "biz" olduğunu varsayar. Kaynak metinde konuşanın kim olduğu belli değilse edilgen kalmalıdır: *...sürümün ay sonunda yayınlanması planlanıyor.*)

**4. Hep aynı başlangıç → öğe sırası değiştirme**
- Önce: *Bu yöntem hızlıdır. Bu yöntem ucuzdur. Bu yöntem kolay uygulanır.*
- Sonra: *Yöntem hem hızlı hem ucuz. Uygulaması da kolay.*

**5. Yarık cümle → vurguyu yüklemin önüne alma**
- Önce: *Satışları artıran şey ücretsiz kargo oldu.*
- Sonra: *Satışları ücretsiz kargo artırdı.*
- (Türkçede vurgu yüklemin hemen önündeki öğededir. "Ücretsiz kargo satışları artırdı." dendiğinde vurgu "satışları"na kayar. Hangisinin vurgulandığını kaynaktan okuyun.)

**6. Ortak eki son yükleme bırakma**
- Önce: *Sistem hızlıdır ve güvenilirdir.*
- Sonra: *Sistem hızlı ve güvenilirdir.*

**7. Adlaştırma zinciri → doğrudan çekim**
- Önce: *Formun doldurulmasının ardından onay işleminin yapılması gerekmektedir.*
- Sonra: *Form doldurulduktan sonra onaylanmalıdır.*

### Uyarılar

- Çeşitlilik bir araçtır, hedef değildir. Her cümleyi farklı bir yapıya sokmak da yapay durur. İyi bir insan yazısında cümlelerin çoğu yine kurallı ve orta uzunluktadır, yalnızca aralarına doğal kırılmalar girer.
- Devrik ve eksiltili cümle, metne "insan" süsü vermek için eklenen kozmetik bir araç olarak kullanılmamalı. Bağlam gerektirmiyorsa kullanmayın.
- Birleştirme yaparken öznenin kim olduğunu ve zaman ilişkisini koruyun. "-ınca" bir zaman sırası, "-ıp" bir ardışıklık ya da eşzamanlılık, "-arak" bir tarz bildirir. Yanlış zarf-fiil anlamı kaydırır.
- Sıfat-fiille gömerken bir adın önüne ikiden çok yan cümle yığmayın. Okur yükleme varana kadar hepsini aklında tutmak zorunda kalır. Fazlasını ayrı cümleye bölün (bkz. `ai-oruntuleri.md`, ASI-05).
- Farklı özneli iki cümleyi "-ıp" ile birleştirmeyin. "-ıp"lı bölümün öznesi ana cümlenin öznesi sayılır: *"Ekip raporu hazırlayıp müdür onayladı."* yanlıştır, *"Ekip raporu hazırladı, müdür onayladı."* doğrudur.


---

# Ek: references/baglaclar.md

## Bağlaç çeşitlendirme rehberi

Tam envanter, TDK türleri ve kaynakça için `kaynaklar/baglaclar.md` dosyasına bakın. Bu dosya, metinde "ve / ama / çünkü / ayrıca / sonuç olarak" tekeli gördüğünüzde hangi alternatife hangi registerda uzanacağınızı gösterir.

**Etiketler:** R = resmi, G = gündelik, E = edebi, N = nötr (her yerde), ESK = eskimiş (kullanmayın)

### Önce: bağlaca gerçekten gerek var mı?

Yapay zeka metinlerinde bağlaçların çoğu gereksizdir. Alternatif aramadan önce şunları deneyin:
- **Bağlacı silin, noktayla bölün.** *"Fiyatı uygun ve kalitesi yüksek ve kargo hızlı."* → *"Fiyatı uygun. Kalitesi yüksek, kargo da hızlı."*
- **Zarf-fiille birleştirin.** *"Dosyayı açtım ve okudum."* → *"Dosyayı açıp okudum."*
- **Virgülle sıralayın.** *"Geldi ve oturdu ve konuşmaya başladı."* → *"Geldi, oturdu, konuşmaya başladı."*
- **"da/de" kullanın.** *"Ayrıca kargo ücretsiz."* → *"Kargo da ücretsiz."*

### Alternatif tablosu

| Tekel | İlişki | Alternatifler (registerla) |
|---|---|---|
| **ve** | ekleme | zarf-fiil (-ıp, -arak) N · virgülle sıralama N · da/de N · hem ... hem N · üstelik N · hatta N · kaldı ki N/E · bir de G |
| **ama** | karşıtlık | fakat N · ancak R · oysa N · hâlbuki N · ne var ki R/E · gelgelelim G/E · buna karşın R · yine de N · -sa da N · -mesine rağmen N · ise (karşılaştırma) N · yalnız G |
| **çünkü** | sebep | zira R/E · -dığı için N · -dığından R · madem(ki) N · ne de olsa G · nitekim R (yalnızca "beklendiği gibi" anlamında) |
| **bu yüzden / bu nedenle** | sonuç | dolayısıyla R · demek ki N · şu hâlde R/E · öyleyse N · böylece N · bu durumda N |
| **ayrıca** | ekleme | da/de N · üstelik N · dahası N · bunun yanı sıra R · bir de G |
| **sonuç olarak / özetle** | toparlama | Önce silmeyi deneyin. Gerekiyorsa: kısacası N · sözün özü G/E · toparlarsak N · uzun lafın kısası G |
| **eğer ... -sa** | koşul | "eğer"i silin, şart eki yeter · -dığı takdirde R · -mesi hâlinde R · yeter ki G |

### Anlam tuzakları

Bağlaç değiştirmek anlamı değiştirebilir. Aşağıdaki çiftler eş anlamlı **değildir**:

- **ama ≠ oysa.** "Oysa" beklentiyle gerçeğin çeliştiğini, çoğu zaman bir yanılgıyı vurgular. *"Pahalı ama iyi."* cümlesinde "oysa" kullanılamaz.
- **çünkü ≠ nitekim.** "Nitekim" bir öngörünün doğrulandığını bildirir, sebep bildirmez.
- **ama ≠ ise.** "İse" iki şeyi karşılaştırır, beklenti çelişkisi bildirmez.
- **bununla birlikte** hem "buna ek olarak" hem "buna rağmen" anlamına gelebilir. Belirsiz kalıyorsa kullanmayın.
- **zira** ve **dolayısıyla** gündelik bir mesajda yapay ve ağır durur.
- **hâlbuki / oysa** suçlama ya da düzeltme tonu taşıyabilir. Nötr bir iş e-postasında "ancak" daha güvenlidir.

### Yazım

- Bitişik yazılan yedi söz: belki, çünkü, hâlbuki, mademki, meğerki, oysaki, sanki. Diğer bağlaç "ki"ler ayrı yazılır: demek ki, kaldı ki, ne var ki.
- TDK yazımı: **hâlbuki**, **şu hâlde**, **o hâlde**, **lakin**.
- "ve, veya, ya da, yahut" öncesine ve sonrasına virgül konmaz. Bağlaç "da/de"den sonra virgül konmaz.

### Dozaj

- Bir paragrafta aynı karşıtlık bağlacını en fazla bir kez kullanın.
- Alternatif bağlaçları sırayla "dağıtmayın". *"Ancak ... Oysa ... Ne var ki ... Buna karşın ..."* dizisi, "ama ... ama ... ama" kadar yapay durur. Amaç çeşitlilik değil, her ilişkiye **en uygun** bağlacı seçmektir.
- ESK etiketli sözleri (binaenaleyh, mamafih, ezcümle, meğerki, velev ki, hakeza) kullanıcının metninde zaten varsa koruyun. Kendiniz eklemeyin.


---

# Ek: references/noktalama.md

## Noktalama ve yazım denetimi

Kuralların gerekçeleri, TDK bağlantıları ve [DOĞRULANMADI] notları için `kaynaklar/noktalama.md` dosyasına bakın. Bu dosya, yeniden yazarken denetlenecek maddeleri sıralar. Her maddenin TDK'ya dayanıp dayanmadığı yanında gösterilir.

### 1. Uzun çizgi (—): en belirgin iz

**TDK:** Uzun çizgi yalnızca satır başındaki konuşmaları gösterir. Cümle içinde kullanımı TDK'da yoktur ve İngilizce tipografiden gelir.

| İşlev | Yerine | Önce → Sonra |
|---|---|---|
| Ara söz | virgül, -kısa çizgi- ya da ayraç | *Proje — tüm gecikmelere rağmen — tamamlandı.* → *Proje, tüm gecikmelere rağmen, tamamlandı.* |
| Açıklama | iki nokta | *Tek bir sorun var — zaman.* → *Tek bir sorun var: zaman.* |
| Ani dönüş | nokta + yeni cümle | *Her şeyi denedik — hiçbiri işe yaramadı.* → *Her şeyi denedik. Hiçbiri işe yaramadı.* |

Satır başındaki diyalog çizgisine dokunmayın.

### 2. Virgül

- **"ve, veya, ya da, yahut"tan önce virgül konmaz (TDK).** *"hız, güvenlik, ve ölçeklenebilirlik"* → *"hız, güvenlik ve ölçeklenebilirlik"*
- Şart ekinden (-sa/-se) ve cümle içi zarf-fiil ekinden (-ıp, -ınca) sonra virgül konmaz (TDK).
- Özne işlevindeki "bu, şu, o"dan sonra virgül konur (TDK): *"Bu, ilk kez oluyor."*
- "Evet, hayır, peki, tamam"dan sonra virgül konur (TDK).
- Yükleminden uzak düşmüş uzun öznenin ardından virgül konur (TDK).

### 3. İki nokta ve büyük harf

- İki noktadan sonra **tam cümle** gelirse büyük, **öbek ya da liste** gelirse küçük harf kullanılır (TDK). *"Sonuç belli: Kazandık."* / *"Üç renk var: kırmızı, mavi, yeşil."*

### 4. de/da, ki, mi

- **Bağlaç da/de ayrı yazılır**, asla "te/ta" olmaz, kesmeyle ayrılmaz (TDK). *"Ali'de geldi"* → *"Ali de geldi"*; *"bende biliyorum"* → *"ben de biliyorum"*.
- **Bağlaç ki ayrı yazılır.** Yedi kalıplaşmış söz bitişiktir: belki, çünkü, hâlbuki, mademki, meğerki, oysaki, sanki (TDK). Ek olan -ki bitişiktir: *masadaki, yarınki, benimki*.
- **Soru eki ayrı yazılır**, sonraki ekler ona bitişir (TDK). *"Gelecekmisin"* → *"Gelecek misin"*.

### 5. Kesme işareti

- Özel adlara, kısaltmalara, rakamlara ve belirli tarih bildiren ay/gün adlarına gelen çekim ekleri kesmeyle ayrılır (TDK): *Ankara'da, TDK'ye, 2026'da, 3 Kasım'da*.
- **Kurum ve kuruluş adlarına gelen ekler ayrılmaz** (TDK): *Türk Dil Kurumuna, İstanbul Üniversitesinde*. Kısaltması kesme alır: *İÜ'de*.
- **Yapım ekleri ve çoğul eki ayrılmaz** (TDK): *Türkçe, İstanbullu, Avrupalılar*.
- Kısaltmaya gelen ek okunuşa uyar (TDK): *TDK'ye* ("te-de-ke"), *NATO'ya*, *ABD'de* ("a-be-de").
- Yabancı özel adlara ve Türkçeleşmemiş terimlere gelen ek de yazılışa değil okunuşa uyar (yerleşik uygulama): *Slack'te*, *cache'i*, *Chrome'u*. Okunuşu kişiden kişiye değişen sözcüklerde metnin kendi içinde tutarlı olmasına bakın.

### 6. Büyük harf

- Ay ve gün adları **belirli bir tarih** bildiriyorsa büyük, genel zaman bildiriyorsa küçük harfle başlar (TDK): *3 Kasım'da* / *kasımda*.
- "il, ilçe, şehir" özel adın parçası değilse küçük harfle başlar (TDK): *İzmir ili*.
- Para birimleri küçük harfle başlar (TDK): *lira, dolar, avro*.
- Yön bildiren "doğu/batı" küçük, kavram bildiren "Doğu/Batı" büyük harfle başlar (TDK).

### 7. Sayılar

**Uyarı:** Sayılar korunacak öğelerdir. Yalnızca **biçimi** düzeltin. Değerin ne olduğundan emin değilseniz dokunmayın ve not düşün.

- Yüzde işareti sayıdan önce gelir (TDK): *25%* → *%25*.
- Ondalık ayırıcı virgül, binlik ayırıcı noktadır (TDK): *3.5* → *3,5*; *1,200,000* → *1.200.000*. (*"1,5"* gibi tek başına duran bir sayının ondalık mı binlik mi olduğu bağlamdan anlaşılmıyorsa dokunmayın.)
- Sıra sayısı ya *5.* ya *5'inci* olur, ikisi bir arada olmaz (TDK).
- Birden çok sözcüklü sayılar ayrı yazılır (TDK): *on beş*.
- Saat ve dakika arasına nokta konur (TDK): *14.30*, *09.15'te*. *14:30* yazımı dijital metinlerde çok yaygındır. Yalnızca akademik ve resmi metinde düzeltin, tabloya, program çıktısına ve ekran görüntüsünden aktarılan değere dokunmayın. Saate gelen ek okunuşa uyar: *17.30'da* (otuzda), *09.15'te* (on beşte).

### 8. Sık yazım hataları

*birşey → bir şey · herşey → her şey · hiç bir → hiçbir · bir çok → birçok · yada → ya da · yanlız → yalnız · halbuki → hâlbuki (TDK sözlüğü)*

Kullanıcının metninde "halbuki", "dahil", "hala" gibi düzeltme işaretsiz yazımlar varsa ve metin bunu tutarlı biçimde yapıyorsa, bu bir üslup tercihi olabilir. Anlam belirsizliği yaratmıyorsa ("hala/hâlâ" yaratır) üslubu koruyun ve özette belirtin.
