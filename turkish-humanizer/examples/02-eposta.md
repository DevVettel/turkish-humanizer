# Örnek 2: İş e-postası

**Register:** iş yazışması (yarı resmi) · **Hitap:** siz · **Kişi:** biz

## Önce

> **Konu:** Proje Teslim Tarihi Hakkında Bilgilendirme
>
> Merhaba Selin Hanım,
>
> Umarım bu e-posta sizi iyi bulur.
>
> Bu e-postayı, Lodos Lojistik projesinin teslim tarihi ile ilgili olarak sizi bilgilendirmek amacıyla yazmaktayım. Ekibimiz tarafından yapılan değerlendirmeler sonucunda, entegrasyon aşamasında bazı teknik zorluklarla karşılaşıldığı tespit edilmiştir.
>
> **Mevcut Durum:**
> - API entegrasyonu %80 oranında tamamlanmıştır.
> - Test süreci henüz başlamamıştır.
> - Ödeme modülünde beklenmedik bir uyumsuzluk tespit edilmiştir.
>
> Bu bağlamda, söz konusu zorluklar göz önünde bulundurulduğunda, teslim tarihinin 14 Kasım'dan 28 Kasım'a ertelenmesinin uygun olacağı değerlendirilmektedir. Bu durumun yaratacağı olası aksaklıklar için şimdiden özür dileriz.
>
> Konuyu daha detaylı bir şekilde görüşmek için bu hafta içinde kısa bir toplantı ayarlayabilirsek çok memnun oluruz. Herhangi bir sorunuz olması durumunda lütfen benimle iletişime geçmekten çekinmeyin.
>
> Saygılarımla,
> Kerem Aydın
> Proje Yöneticisi

## Sonra

> **Konu:** Lodos Lojistik projesinde teslim tarihi
>
> Merhaba Selin Hanım,
>
> Lodos Lojistik projesinin teslim tarihiyle ilgili sizi bilgilendirmek istiyorum. Ekibimizin değerlendirmesine göre entegrasyon aşamasında bazı teknik zorluklar çıktı. API entegrasyonunun %80'i tamamlandı, ama test süreci henüz başlamadı. Ödeme modülünde de beklenmedik bir uyumsuzluk tespit ettik.
>
> Bu nedenle teslim tarihini 14 Kasım'dan 28 Kasım'a ertelemenin uygun olacağını düşünüyoruz. Bunun yaratabileceği aksaklıklar için şimdiden özür dileriz.
>
> Konuyu ayrıntılı konuşmak için bu hafta kısa bir toplantı ayarlayabilirsek çok seviniriz. Sorularınız için bana her zaman yazabilirsiniz.
>
> Saygılarımla,
> Kerem Aydın
> Proje Yöneticisi

## Düzeltilen örüntüler

| ID | Ne değişti |
|---|---|
| DOL-01 | "Umarım bu e-posta sizi iyi bulur." silindi (*I hope this email finds you well* çevirisi) |
| SOZ-04 | "ile ilgili olarak ... amacıyla yazmaktayım" → "ile ilgili sizi bilgilendirmek istiyorum" |
| YAPI-04 / CEV-03 | "Ekibimiz tarafından yapılan değerlendirmeler sonucunda ... tespit edilmiştir" → "Ekibimizin değerlendirmesine göre ... çıktı" |
| BIC-01 | "Mevcut Durum" başlığı ve üç madde düzyazıya çevrildi. Üç bilginin üçü de korundu |
| SOZ-02 | "Bu bağlamda, söz konusu ... göz önünde bulundurulduğunda" → "Bu nedenle" |
| YAPI-03 | "değerlendirilmektedir" → "düşünüyoruz" (konuşan belli: ekip) |
| DOL-02 | "iletişime geçmekten çekinmeyin" kalıbı sade bir kapanışa çevrildi |
| NOK-03 | "%80 oranında" → "%80'i" (biçim, değer aynı) |

## Bilinçli olarak korunanlar

- **Selamlama, imza, unvan:** E-posta biçiminin parçası.
- **"siz" hitabı ve özür cümlesi:** Ton ve içerik.
- **Tarihler (14 Kasım, 28 Kasım), "%80", "Lodos Lojistik", "API":** aynen.
- **"uygun olacağını düşünüyoruz":** Kaynakta bu bir karar değil, bir öneriydi ("uygun olacağı değerlendirilmektedir"). "Teslim tarihini 28 Kasım'a erteliyoruz" yazmak iddianın gücünü değiştirirdi.
- **Edilgen → etken dönüşümü** yalnızca öznenin metinde açıkça bulunduğu yerde yapıldı ("Ekibimiz").

## Not

"tespit edilmiştir" → "tespit ettik": Öznenin "biz" (ekip) olduğu kaynakta açık, bu yüzden güvenli bir dönüşüm. Konu satırı da kısaltıldı. Bilgi ("teslim tarihi", proje adı) korundu, "Hakkında Bilgilendirme" dolgusu çıkarıldı.
