---
name: turkish-humanizer
description: Türkçe metinleri yapay zeka izlerinden arındırıp doğal bir insan yazısına dönüştürür. Anlamı, sayıları, terimleri ve özel isimleri olduğu gibi korur. Kullanıcı "Türkçeleştir", "insanlaştır", "doğallaştır", "yapay zeka gibi durmasın", "daha doğal yaz", "robot gibi olmuş", "AI kokuyor", "humanize" dediğinde ya da bir Türkçe metnin (blog, e-posta, akademik paragraf, ürün açıklaması, LinkedIn gönderisi, rapor) üslubunu düzeltmek, akıcılaştırmak veya ChatGPT/Claude çıktısı gibi durmaktan çıkarmak istediğinde bu skill'i mutlaka kullan. Türkçe bir metni "yeniden yaz", "elden geçir", "redakte et" isteklerinde de, "bu metin yapay zeka gibi mi duruyor", "nerelerinde iz var", "denetle" gibi yeniden yazım istemeyen inceleme isteklerinde de kullan. Use for any request to humanize or de-AI Turkish text.
---

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
