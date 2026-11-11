# Örnek 6: Teknik doküman

**Register:** teknik doküman (iş yazışmasına yakın, yalın) · **Hitap:** siz · **Kişi:** edilgen ve emir

## Önce

> ## Kurulum Ve Yapılandırma
>
> Bu bölümde, Kervan API'sinin kurulumunu derinlemesine ele alacağız. Kurulum işleminin gerçekleştirilebilmesi için Node.js 20 veya üzeri bir sürüme sahip olmanız gerekmektedir. Bağımlılıkların yüklenmesinin ardından `.env` dosyasının oluşturulması gerekmektedir.
>
> - **Önbellek:** Yanıtlar Redis'de 15 dakika boyunca saklanmaktadır.
> - **Hız sınırı:** Her anahtar için dakikada 60 istek sınırı uygulanmaktadır.
>
> Sınırı aşan istekler kuyruğa alınmaz — bunun yerine 429 hata kodu döndürülür. Cache'ı temizlemek için `npm run cache:clear` komutunu çalıştırabilirsiniz.
>
> Umarım bu rehber faydalı olmuştur!

## Sonra

> ## Kurulum ve Yapılandırma
>
> Kervan API'sini kurmak için Node.js 20 veya üzeri bir sürüm gerekir. Bağımlılıkları yükledikten sonra `.env` dosyasını oluşturun.
>
> Yanıtlar Redis'te 15 dakika saklanır. Her anahtar için dakikada 60 istek sınırı uygulanır. Sınırı aşan istekler kuyruğa alınmaz, bunun yerine 429 hata kodu döndürülür. Cache'i temizlemek için `npm run cache:clear` komutunu çalıştırabilirsiniz.

## Düzeltilen örüntüler

| ID | Ne değişti |
|---|---|
| DOL-01 / CEV-01 | "Bu bölümde ... derinlemesine ele alacağız" silindi. Bölüm doğrudan ilk gereksinimle başlıyor |
| SOZ-07 | "Kurulum işleminin gerçekleştirilebilmesi için" → "kurmak için"; "yüklenmesinin ardından ... oluşturulması gerekmektedir" → "yükledikten sonra ... oluşturun" |
| CEV-02 | "bir sürüme sahip olmanız gerekmektedir" → "bir sürüm gerekir" |
| YAPI-03 | Dört "-mektedir" yüklemi geniş zamana çevrildi |
| BIC-02 | İki kalın etiketli madde düzyazıya çevrildi. "Önbellek" ve "Hız sınırı" etiketleri cümlelerin konusu zaten |
| NOK-01 | Uzun çizgi virgül oldu |
| CEV-06 | "Redis'de" → "Redis'te", "Cache'ı" → "Cache'i" |
| YAZ-05 | Başlıkta "Ve" → "ve" |
| DOL-02 | "Umarım bu rehber faydalı olmuştur!" silindi |

## Bilinçli olarak korunanlar

- **Kod ve dosya adları:** `.env`, `npm run cache:clear` aynen.
- **Sayılar ve adlar:** "Node.js 20", "15 dakika", "dakikada 60 istek", "429", "Kervan API", "Redis".
- **Terimler:** "cache" ve "önbellek" kaynakta ikisi de geçiyor. Birini ötekine çevirmek yazarın terim tercihine karışmak olurdu (bkz. ASI-04).
- **"veya üzeri":** "ya da" ile değiştirmek için bir neden yok.
- **"çalıştırabilirsiniz":** Kaynak bunu bir zorunluluk olarak değil bir olanak olarak sunuyor. "Çalıştırın" yazmak kipi değiştirirdi. `.env` cümlesinde ise kaynak zaten zorunluluk bildiriyordu ("gerekmektedir"), emir kipi onu karşılıyor.
- **Edilgen yüklemler:** "saklanır", "uygulanır", "döndürülür". Eylemi yapan sistem. Teknik dokümanda edilgen olağandır, özne uydurmaya gerek yok.
- **Başlık:** Başlık kaldırılmadı, çünkü bu bir dokümanın bölümü. Yalnızca bağlacın büyük harfi düzeltildi.

## Not

Teknik dokümanda devrik cümle, söylem sözcüğü ve kısa vurgu cümlesi kullanılmadı. Buradaki iş neredeyse tamamen silmek ve yüklemi sadeleştirmek. Cümle uzunlukları birbirine yakın kaldı. Adım adım okunan bir kurulum metninde bu bir kusur değildir (bkz. YAPI-01, Dokunma).
