# Türkçe yapay zeka örüntüleri

Bu dosya, Türkçe metinlerde yapay zeka izi bırakan örüntülerin kataloğudur. Her örüntü aynı şablonu kullanan bağımsız bir bloktur. Yeni bir örüntü eklemek için en alttaki şablonu kopyalayıp doldurmanız yeterli. Ayrıntılı katkı kuralları için deponun `CONTRIBUTING.md` dosyasına bakın.

**Okuma notu (skill için):** Bu bir yasak listesi değildir. "Bu bağlamda" sözü tek başına yanlış değildir. Sorun, bu tür kalıpların yığılması ve metni içi boş bir resmiyetle doldurmasıdır. Her bloktaki **Dokunma** satırı, örüntünün meşru olduğu durumları gösterir. Bir örüntüyü kaldırırken anlamın, sayıların, terimlerin ve özel isimlerin aynen korunması şarttır.

## Güç

Her blokta bir **Güç** satırı var. Güç, dikkatli bir yazarın o kalıbı bilerek kullanma olasılığının ne kadar düşük olduğunu gösterir:

| Güç | Ne zaman düzeltilir |
|---|---|
| **güçlü** | Tek bir görülüş yeter. Dokunma satırındaki istisnalar dışında düzeltin. |
| **orta** | Metin türüne bakın. Dokunma satırı geçerli değilse düzeltin. |
| **tek başına zayıf** | İnsanlar da sık yazar. Aynı paragrafta başka izler yoksa dokunmayın. |
| **kural** | İz değil yazım ya da noktalama hatası. Güçten bağımsız olarak TDK'ya göre düzeltin. |

## Kategoriler

| Önek | Kategori |
|---|---|
| `YAPI` | Cümle ve paragraf yapısı |
| `SOZ` | Klişe ve şişirilmiş sözcük seçimi |
| `CEV` | İngilizceden çeviri kokan ifadeler |
| `NOK` | Noktalama ve tipografi |
| `BIC` | Biçim ve düzen (başlık, madde, kalın yazı) |
| `DOL` | Sohbet ve model artıkları (açılış, kapanış, model notu) |
| `OKU` | Okuru ve bağlamı yanlış kurmak |
| `YAZ` | Yazım hataları |
| `ASI` | Aşırı düzeltme (düzeltirken bırakılan yeni izler) |

## Dizin

- [YAPI-01 Tekdüze dizilim ve eşit cümle uzunluğu](#yapi-01) · tek başına zayıf
- [YAPI-02 ve/ama/çünkü tekeli](#yapi-02) · orta
- [YAPI-03 -mektedir/-maktadır yığılması](#yapi-03) · orta
- [YAPI-04 Gereksiz edilgen yapı](#yapi-04) · tek başına zayıf
- [YAPI-05 Üçlü sıralama alışkanlığı](#yapi-05) · orta
- [YAPI-06 "Sadece X değil, aynı zamanda Y" kalıbı](#yapi-06) · güçlü
- [YAPI-07 Kendi sorup kendi cevaplama](#yapi-07) · orta
- [YAPI-08 Özet ya da vurucu cümleyle kapanış](#yapi-08) · güçlü
- [YAPI-09 Yarık cümle ve arkadan eklenen açıklama](#yapi-09) · orta
- [YAPI-10 Kimseyle tartışma](#yapi-10) · güçlü
- [YAPI-11 Aynı sözcükle başlayan cümleler](#yapi-11) · tek başına zayıf
- [SOZ-01 "Önemli bir rol oynamaktadır" ailesi](#soz-01) · güçlü
- [SOZ-02 Geçiş ve bağlam klişeleri](#soz-02) · orta
- [SOZ-03 Pekiştirme şişirmesi](#soz-03) · orta
- [SOZ-04 "olarak" ve "-mekte olup" fazlalığı](#soz-04) · tek başına zayıf
- [SOZ-05 "Bu durum" / "Bu da" ile açılış](#soz-05) · tek başına zayıf
- [SOZ-06 Gösterişli mecaz öbekleri](#soz-06) · orta
- [SOZ-07 Adlaştırma zinciri ve boş yardımcı fiil](#soz-07) · orta
- [SOZ-08 Derin görünen vecize](#soz-08) · güçlü
- [SOZ-09 Kaynaksız otorite](#soz-09) · orta
- [CEV-01 Çeviri deyimler](#cev-01) · güçlü
- [CEV-02 "-e sahip olmak" fazlalığı](#cev-02) · orta
- [CEV-03 "tarafından" ve "için" yığılması](#cev-03) · orta
- [CEV-04 Gereksiz iyelik zamiri ve "bir"](#cev-04) · tek başına zayıf
- [CEV-05 "bir şekilde" zarfları](#cev-05) · orta
- [CEV-06 Okunuşa uymayan ek](#cev-06) · kural
- [NOK-01 Cümle içinde uzun çizgi (—)](#nok-01) · güçlü
- [NOK-02 "ve"den önce virgül](#nok-02) · kural
- [NOK-03 İngilizce sayı ve yüzde biçimi](#nok-03) · kural
- [NOK-04 Ünlem ve emoji bolluğu](#nok-04) · orta
- [BIC-01 Gereksiz başlık, madde işareti ve kalın yazı](#bic-01) · orta
- [BIC-02 Kalın etiketli madde](#bic-02) · orta
- [BIC-03 Başlığı ilk cümlede tekrarlama](#bic-03) · orta
- [BIC-04 Metnin kendini anlatması](#bic-04) · orta
- [DOL-01 Açılış dolguları ve sahneli giriş](#dol-01) · güçlü
- [DOL-02 Kapanış dolguları](#dol-02) · güçlü
- [DOL-03 Model notu: bilgi sınırı ve tahmin](#dol-03) · güçlü
- [OKU-01 Okurun bildiğini yeniden anlatma](#oku-01) · orta
- [YAZ-01 Bağlaç de/da](#yaz-01) · kural
- [YAZ-02 ki](#yaz-02) · kural
- [YAZ-03 Soru eki mi](#yaz-03) · kural
- [YAZ-04 Kesme işareti](#yaz-04) · kural
- [YAZ-05 Büyük harf](#yaz-05) · kural
- [YAZ-06 Sık yazım hataları](#yaz-06) · kural
- [ASI-01 Yedek sözcük tiki](#asi-01)
- [ASI-02 Kılık değiştiren kalıp](#asi-02)
- [ASI-03 Sahte samimiyet](#asi-03)
- [ASI-04 Arı Türkçe merakı](#asi-04)
- [ASI-05 Aşırı gömme](#asi-05)

---

<a id="yapi-01"></a>
### YAPI-01 · Tekdüze dizilim ve eşit cümle uzunluğu

- **Belirti:** Paragraftaki cümlelerin neredeyse hepsi özne + tümleç + nesne + yüklem sırasında ve 14-22 sözcük arasında. Cümle başları birbirine benziyor.
- **Neden yapay:** İnsan yazısında uzunluk dalgalanır. Kısa bir cümle vurgu yapar, uzun bir cümle bağlamı açar. Dil modelleri ise "güvenli" orta uzunlukta toplanır.
- **Ne yapmalı:** Bir iki cümleyi birleştirin (zarf-fiil, sıfat-fiil), birini kısaltın, bir iki cümlede öğe sırasını değiştirin. Araçlar için bkz. `cumle-turleri.md`.
- **Dokunma:** Teknik talimat, sözleşme maddesi ve adım adım kılavuzda düzenli yapı bir erdemdir.
- **Güç:** tek başına zayıf
- **Önce:** *Şirketimiz 2015 yılında İzmir'de kurulmuştur. Ekibimiz yazılım geliştirme alanında uzmanlaşmış kişilerden oluşmaktadır. Müşterilerimize uçtan uca çözümler sunmaktayız. Projelerimizde çevik yöntemleri benimsemekteyiz.*
- **Sonra:** *2015'te İzmir'de kurulduk. Yazılım geliştirmede uzmanlaşmış ekibimizle müşterilerimize uçtan uca çözümler sunuyoruz. Projelerde çevik yöntemlerle çalışıyoruz.*

<a id="yapi-02"></a>
### YAPI-02 · ve/ama/çünkü tekeli

- **Belirti:** Bir paragrafta "ve" üçten çok, "ama" ya da "çünkü" ikiden çok geçiyor. Cümleler hep bu üç bağlaçla bağlanıyor.
- **Neden yapay:** Türkçede iki cümleyi bağlamanın en doğal yolu çoğu zaman bağlaç değil, ektir (-ıp, -ınca, -dığı için). Ayrıca karşıtlık ve sebep için çok zengin bir bağlaç envanteri vardır. Modeller İngilizcedeki *and/but/because* düzenini taşır.
- **Ne yapmalı:** Önce bağlacı silmeyi deneyin (nokta, virgül, zarf-fiil, "da/de"). Gerekiyorsa ilişkiye en uygun bağlacı seçin. Bkz. `baglaclar.md`.
- **Dokunma:** Sayılan öğeler arasındaki "ve" ("elma ve armut") doğaldır. Tek bir "ama" ya da "çünkü" sorun değildir.
- **Güç:** orta
- **Önce:** *Uygulama hızlı ve kullanımı kolay ama bazı özellikler eksik çünkü ekip küçük ve kaynaklar sınırlı.*
- **Sonra:** *Uygulama hızlı, kullanımı da kolay. Yine de bazı özellikler eksik: Ekip küçük, kaynaklar sınırlı.*

<a id="yapi-03"></a>
### YAPI-03 · -mektedir/-maktadır yığılması

- **Belirti:** Art arda cümleler "-mektedir, -maktadır, -ilmektedir, -mekteyiz" ile bitiyor.
- **Neden yapay:** Bu çekim resmi yazıda yerindedir, ama her cümlede kullanıldığında metin bürokratik ve ağır bir hal alır. İnsanlar resmi yazıda bile geniş zamanı (-ır/-ar), şimdiki zamanı (-yor) ve -dır'lı isim cümlesini karıştırarak kullanır.
- **Ne yapmalı:** Gündelik ve yarı resmi metinde çoğunu "-yor" ya da geniş zamana çevirin. Akademik ve resmi metinde bir kısmını koruyun, ama hepsini aynı ekle bitirmeyin: biri geniş zaman, biri isim cümlesi olabilir.
- **Dokunma:** Resmi yazışmada, mevzuat dilinde ve akademik metinde bu çekim registerin parçasıdır. Tamamen kaldırmayın, yalnızca yoğunluğunu azaltın.
- **Güç:** orta
- **Önce:** *Proje kapsamında veriler toplanmaktadır. Toplanan veriler analiz edilmektedir. Analiz sonuçları raporlanmaktadır.*
- **Sonra (gündelik):** *Projede önce verileri topluyoruz, sonra analiz edip raporluyoruz.*
- **Sonra (akademik):** *Proje kapsamında toplanan veriler analiz edilerek raporlanmaktadır.*

<a id="yapi-04"></a>
### YAPI-04 · Gereksiz edilgen yapı

- **Belirti:** Eylemi yapan belli olduğu hâlde edilgen kullanılıyor: "tarafımızca incelenmiştir", "kararlaştırılmıştır", "tavsiye edilmektedir".
- **Neden yapay:** Edilgen yapı nesnellik görüntüsü verir. Ancak eylemi yapan biliniyorsa metni dolaylı ve kaçamak gösterir.
- **Ne yapmalı:** Özne metinde açıkça varsa ya da konuşan belliyse etken yapıya çevirin. Özne belli değilse uydurmayın.
- **Dokunma:** Akademik yöntem bölümleri ("Örneklem rastgele seçilmiştir.") ve öznenin önemsiz olduğu durumlar.
- **Güç:** tek başına zayıf
- **Önce:** *Talebiniz tarafımızca incelenmiş olup gerekli düzenlemelerin yapılmasına karar verilmiştir.*
- **Sonra:** *Talebinizi inceledik ve gerekli düzenlemeleri yapmaya karar verdik.*

<a id="yapi-05"></a>
### YAPI-05 · Üçlü sıralama alışkanlığı

- **Belirti:** Sıfatlar, örnekler ve maddeler hep üçlü geliyor: "hızlı, güvenilir ve ölçeklenebilir", "verimlilik, şeffaflık ve sürdürülebilirlik".
- **Neden yapay:** Üçlü dizi retorikte güçlü bir kalıptır, ama modeller bunu bir refleks gibi her yerde kullanır. Üçüncü öğe çoğu zaman bilgi taşımaz, ritmi tamamlamak için eklenmiştir.
- **Ne yapmalı:** Gerçekten üç ayrı bilgi varsa koruyun. Biri ötekilerin tekrarıysa ya da boşsa (ve kaldırmak bilgi kaybına yol açmıyorsa) çıkarın ya da sayıyı değiştirin. **Dikkat:** Kaynakta somut bilgi taşıyan öğeyi silmek bilgi çıkarmaktır, yasaktır.
- **Dokunma:** Teknik özellik listeleri ve kaynakta gerçekten üç olgu sayılan cümleler.
- **Güç:** orta
- **Önce:** *Yeni panelimiz sezgisel, kullanıcı dostu ve kolay anlaşılır bir arayüz sunuyor.*
- **Sonra:** *Yeni panelin arayüzü kolay anlaşılıyor.* (Üç sıfat aynı şeyi söylüyor.)

<a id="yapi-06"></a>
### YAPI-06 · "Sadece X değil, aynı zamanda Y" kalıbı

- **Belirti:** "Bu sadece bir X değil, aynı zamanda bir Y", "Bu bir X değil, bir Y", "X olmakla kalmıyor, Y de", "X'in ötesinde Y" kalıbı. İki cümleye bölünmüş hâli de aynı izdir: "Mesele hız değil. Mesele güven."
- **Neden yapay:** İngilizce *not just X, but Y* kalıbının çevirisidir. Olumsuz yarı kimsenin söylemediği bir şeyi reddeder, olumlu yarı da böylece daha büyük görünür. Cümleye iddia değil ağırlık eklenir.
- **Ne yapmalı:** Doğrudan söyleyin. İki bilgi de önemliyse "hem ... hem" ya da iki ayrı cümle kullanın.
- **Dokunma:** Okurun gerçekten taşıdığı bir yanlış kanıyı düzelten ya da iki yarısı da bilgi taşıyan kullanım ("Bu bir hata değil, bilinçli bir tercih.").
- **Güç:** güçlü
- **Önce:** *Bu uygulama sadece bir not defteri değil, aynı zamanda kişisel bir verimlilik asistanı.*
- **Sonra:** *Uygulama not almanın yanında verimliliğinizi artırmanıza da yardım ediyor.*

<a id="yapi-07"></a>
### YAPI-07 · Kendi sorup kendi cevaplama

- **Belirti:** "Peki bu ne anlama geliyor?", "Peki neden?", "Sonuç mu? ..." gibi sorular ve hemen ardından cevapları.
- **Neden yapay:** Okurun aklından geçmeyen bir soruyu sahnelemek, metne sahte bir konuşma havası verir.
- **Ne yapmalı:** Soruyu silip cevabı doğrudan söyleyin.
- **Dokunma:** Gerçekten okurun soracağı bir soruysa (SSS bölümü, öğretici bir blog) ve metinde bir kez geçiyorsa.
- **Güç:** orta
- **Önce:** *Peki bu değişiklik kullanıcılar için ne anlama geliyor? Kısacası, daha hızlı bir deneyim.*
- **Sonra:** *Değişiklikten sonra uygulama kullanıcılar için daha hızlı çalışıyor.*

<a id="yapi-08"></a>
### YAPI-08 · Özet ya da vurucu cümleyle kapanış

- **Belirti:** Paragraf az önce söyleneni tekrar eden bir cümleyle bitiyor: "Bu da gösteriyor ki ...", "Kısacası ...", "Dolayısıyla X büyük önem taşımaktadır." Aynı aileden: Bir önceki paragrafı tekrar eden tek cümlelik paragraf ("İşte fark tam da burada."), art arda kesik parçalar ("Ne plan vardı. Ne bütçe. Ne de bir hedef."), okura duraklama komutu ("Bunu bir kez daha okuyun.", "Üzerinde düşünmeye değer."), bir örneğin ya da sayının ardından ne gösterdiğini söyleyen cümle ("Bu, sabrın ne kadar önemli olduğunu gösteren bir dersti.").
- **Neden yapay:** Modeller her bölümü kapatma ve önemli görünme eğilimindedir. Okur aynı bilgiyi ikinci kez okumaya ihtiyaç duymaz, vurguyu da yeni bir bilgiden bekler.
- **Ne yapmalı:** Yeni bilgi taşımayan kapanışı silin. Yeni bilgi taşıyorsa (bir çıkarım, sonuç) yalnızca o kısmı tutun. Kesik parçaları, somut bir iddia taşıyan tek cümlede birleştirin.
- **Dokunma:** Uzun raporların ve akademik makalelerin sonuç bölümü. Yeni bir olgu ya da sonuç taşıyan kısa cümle.
- **Güç:** güçlü
- **Önce:** *Kargo süresi 5 günden 2 güne indi, iade oranı %8'den %3'e düştü. Bu da müşteri memnuniyetinin ne kadar önemli olduğunu açıkça göstermektedir.*
- **Sonra:** *Kargo süresi 5 günden 2 güne indi, iade oranı %8'den %3'e düştü.*
- **Önce (kesik parçalar):** *Sonra yeni randevu sistemi geldi. Ne bekleme kaldı. Ne kuyruk. Ne de kaybolan evrak. Her şey değişmişti.*
- **Sonra:** *Yeni randevu sistemiyle bekleme, kuyruk ve kaybolan evrak sorunu ortadan kalktı.*

<a id="yapi-09"></a>
### YAPI-09 · Yarık cümle ve arkadan eklenen açıklama

- **Belirti:** "Bunu mümkün kılan şey ...", "Asıl önemli olan şey ...-dır", "Dikkat çeken nokta şu ki ..." gibi vurguyu yapay bir özneyle kuran cümleler. Bir de adı söyleyip niteliğini ardından ayrı cümleyle ekleyen çiftler: "Bir rapor hazırladık. Bu rapor geçen yılın satışlarını gösteriyor."
- **Neden yapay:** İkisi de İngilizce cümle sırasının izidir (*what makes this possible is ...*, *a report that shows ...*). Türkçe vurguyu yüklemin hemen önüne gelen öğeyle verir, niteleyeni de adın önüne koyar.
- **Ne yapmalı:** Vurgulanan öğeyi yüklemin önüne alın, "şey"i atın. Arkadan gelen açıklamayı sıfat-fiille adın önüne taşıyın. Araçlar için bkz. `cumle-turleri.md`.
- **Dokunma:** Gerçek bir karşıtlık kuruluyorsa ("Bizi geciktiren bütçe değil, onay süreciydi."). Akademik metinde tanım cümleleri.
- **Güç:** orta
- **Önce:** *Teslimatı hızlandıran şey yeni depo oldu. Bir takip ekranı da ekledik. Bu ekran siparişin nerede olduğunu gösteriyor.*
- **Sonra:** *Teslimatı yeni depo hızlandırdı. Siparişin nerede olduğunu gösteren bir takip ekranı da ekledik.*

<a id="yapi-10"></a>
### YAPI-10 · Kimseyle tartışma

- **Belirti:** Metin, kimsenin ileri sürmediği bir itiraza ya da kimsenin önermediği bir seçeneğe cevap veriyor: "Yanlış anlaşılmasın, ...", "Şunu söylemiyorum: ...", "Bu, X'in önemsiz olduğu anlamına gelmiyor.", "Kimileri ... diyebilir, ancak ...", "Akla ilk gelen çözüm ... olabilir, ama ...", "Elbette ... diyenler çıkacaktır."
- **Neden yapay:** Model olası her okura karşı önceden savunma yapar. Metinde karşılığı olmayan itiraz, okura asıl iddiaya varmadan önce bir dolambaç yürütür. Birbiriyle ilgisiz birkaç savunmanın art arda gelmesi tek bir savunmadan daha güçlü bir izdir.
- **Ne yapmalı:** Hayali karşı tarafı silin. Savunmanın içinde yazarın bir tutumu varsa o tutumu tek ve düz bir cümleyle koruyun. Elenen seçenek bir gerekçe taşıyorsa gerekçeyi olumlu bir cümleye taşıyın, kaybetmeyin.
- **Dokunma:** Metnin bir kişiye ya da kaynağa dayandırdığı ve gerçekten cevapladığı itiraz. Tartışma yazısında ve akademik metinde karşı görüşün ele alınması. Okurun gerçekten tartacağı bir seçenek.
- **Güç:** güçlü
- **Önce:** *Yanlış anlaşılmasın, toplantılar gereksiz demiyorum. Kimileri her şeyin e-postayla çözülebileceğini düşünebilir, ama mesele bu değil. Sorun, haftalık toplantının bir saati aşması.*
- **Sonra:** *Toplantılara karşı değilim. Sorun, haftalık toplantının bir saati aşması.*
- **Önce (sahte seçenek):** *Yedekler her gece alınıyor. Akla ilk gelen yöntem sunucuyu durdurup kopyalamak olabilir, ama bu bütün oturumları düşürürdü. Bu yüzden yedek, sistem çalışırken anlık görüntüyle alınıyor.*
- **Sonra:** *Yedekler her gece, oturumlar düşmesin diye sistem çalışırken anlık görüntüyle alınıyor.*

<a id="yapi-11"></a>
### YAPI-11 · Aynı sözcükle başlayan cümleler

- **Belirti:** Bir paragrafta üç ya da daha çok cümle aynı sözcükle başlıyor: "Ekibimiz ... Ekibimiz ... Ekibimiz ...", "Ayrıca ... Ayrıca ...". Ekleme sözlerinin sırayla dizilmesi de aynı izdir: "Bunun yanı sıra ... Ek olarak ... Bunun yanında ...".
- **Neden yapay:** Model her cümleyi bir öncekinden bağımsız kurar ve en güvenli girişi seçer. Türkçede öznenin kişi ekinden anlaşılması ve öğe sırasının serbest olması bu tekrarı kolayca önler.
- **Ne yapmalı:** Kişi ekinden anlaşılan özneyi düşürün, bazı cümleleri birleştirin, bir iki cümlede vurgulanan öğeyi başa alın. Ekleme sözlerinin çoğunu silin, çoğu zaman "da/de" yeter. Bağlaç için bkz. `baglaclar.md`.
- **Dokunma:** Bilinçli tekrar (konuşma metni, edebi anlatım, adım adım talimat). "Bu ..." ile başlayan cümleler SOZ-05'e girer, ayrıca sayılmaz.
- **Güç:** tek başına zayıf
- **Önce:** *Ekibimiz yeni depoyu mart ayında açtı. Ekibimiz teslim süresini iki güne indirdi. Ekibimiz şimdi de iade sürecini yeniliyor.*
- **Sonra:** *Ekibimiz yeni depoyu mart ayında açıp teslim süresini iki güne indirdi. Şimdi de iade sürecini yeniliyor.*

---

<a id="soz-01"></a>
### SOZ-01 · "Önemli bir rol oynamaktadır" ailesi

- **Belirti:** önemli bir rol oynamaktadır, büyük önem taşımaktadır, kritik bir öneme sahiptir, vazgeçilmez bir unsurdur, ayrılmaz bir parçasıdır, hayati önem arz etmektedir.
- **Neden yapay:** Bu kalıplar bir şeyin önemli olduğunu söyler ama neden önemli olduğunu söylemez. Yerini somut bir yükleme bırakmalıdır.
- **Ne yapmalı:** Önemin ne olduğunu söyleyen fiili bulun ("etkiler", "belirler", "sağlar", "düşürür"). Kaynakta bu bilgi yoksa daha sade bir ifadeye indirin ("önemlidir"). Bilgi uydurmayın.
- **Dokunma:** Akademik metinde ölçülü ve tek kullanım.
- **Güç:** güçlü
- **Önce:** *Düzenli uyku, öğrencilerin akademik başarısında önemli bir rol oynamaktadır.*
- **Sonra:** *Düzenli uyku, öğrencilerin akademik başarısını etkiler.*

<a id="soz-02"></a>
### SOZ-02 · Geçiş ve bağlam klişeleri

- **Belirti:** bu bağlamda, bu çerçevede, söz konusu, göz önünde bulundurulduğunda, dikkate alındığında, günümüzde, son yıllarda, hızla gelişen dünyada, teknolojinin hızla ilerlediği günümüzde, sonuç olarak.
- **Neden yapay:** Bu sözler cümleler arasında bir bağ varmış izlenimi verir ama çoğu zaman hiçbir şey bağlamaz. "Günümüzde" ile başlayan açılış, yapay zekanın en tanıdık imzalarından biridir.
- **Ne yapmalı:** Silin ve cümlenin hâlâ ayakta durup durmadığına bakın. Çoğu zaman durur. "Söz konusu X"i "bu X" ya da yalnızca "X" yapın.
- **Dokunma:** Resmi yazışmada "söz konusu" belirli bir belgeyi işaret ediyorsa ("söz konusu sözleşme") kalabilir.
- **Güç:** orta
- **Önce:** *Teknolojinin hızla geliştiği günümüzde, yapay zeka birçok sektörü dönüştürmektedir. Bu bağlamda, söz konusu dönüşüm göz önünde bulundurulduğunda şirketlerin hazırlıklı olması gerekmektedir.*
- **Sonra:** *Yapay zeka birçok sektörü dönüştürüyor ve şirketlerin buna hazırlanması gerekiyor.*

<a id="soz-03"></a>
### SOZ-03 · Pekiştirme şişirmesi

- **Belirti:** oldukça, son derece, büyük ölçüde, son derece önemli, kritik, kilit, eşsiz, benzersiz, muazzam, inanılmaz, devrim niteliğinde.
- **Neden yapay:** Her şey "son derece" önemli olunca hiçbir şey önemli olmaz. Modeller tarafsız bilgiyi pekiştirmelerle süsler.
- **Ne yapmalı:** Pekiştirmeyi silin. Gerçek bir derece bilgisi varsa sayı ya da somut karşılaştırmayla verin (kaynakta varsa).
- **Dokunma:** Kaynakta ölçülebilir bir karşılığı olan tek bir pekiştirme.
- **Güç:** orta
- **Önce:** *Bu son derece kritik güncelleme, sistemin performansını büyük ölçüde artırarak eşsiz bir deneyim sunuyor.*
- **Sonra:** *Bu güncelleme sistemin performansını artırıyor.*

<a id="soz-04"></a>
### SOZ-04 · "olarak" ve "-mekte olup" fazlalığı

- **Belirti:** "şirket olarak", "ekip olarak", "genel olarak", "temel olarak", "aktif olarak", "düzenli olarak"; "-mekte olup", "-miş olup".
- **Neden yapay:** "Olarak" çoğu yerde bilgi taşımaz. "-mekte olup" ise iki cümleyi resmi yazışma havasında yapıştırır.
- **Ne yapmalı:** "Olarak"ı silin ya da ekle karşılayın ("düzenli olarak" → "düzenli"). "-mekte olup"u iki cümleye bölün ya da zarf-fiil kullanın.
- **Dokunma:** "Şirket olarak" konuşanın kurum adına konuştuğunu vurgulamak için bir kez kullanılabilir.
- **Güç:** tek başına zayıf
- **Önce:** *Şirket olarak müşterilerimizle aktif olarak iletişim kurmakta olup geri bildirimleri düzenli olarak değerlendirmekteyiz.*
- **Sonra:** *Müşterilerimizle sürekli iletişim kuruyor, geri bildirimleri düzenli değerlendiriyoruz.*

<a id="soz-05"></a>
### SOZ-05 · "Bu durum" / "Bu da" ile açılış

- **Belirti:** Art arda cümleler "Bu durum ...", "Bu da ...", "Bu sayede ...", "Bu noktada ..." ile başlıyor.
- **Neden yapay:** Cümleler arasında bağ kurmak için modeller önceki cümlenin tamamını "bu" ile işaret eder. Sık tekrarlanınca metin zincirleme bir hâl alır.
- **Ne yapmalı:** İki cümleyi birleştirin (sıfat-fiil, zarf-fiil) ya da "bu"nun neyi işaret ettiğini adıyla söyleyin.
- **Dokunma:** Bir paragrafta bir kez.
- **Güç:** tek başına zayıf
- **Önce:** *Sunucular yeni veri merkezine taşındı. Bu durum gecikmeyi azalttı. Bu da kullanıcı deneyimini iyileştirdi.*
- **Sonra:** *Sunucuların yeni veri merkezine taşınmasıyla gecikme azaldı, kullanıcı deneyimi iyileşti.*

<a id="soz-06"></a>
### SOZ-06 · Gösterişli mecaz öbekleri

- **Belirti:** yeni bir boyut kazandırmak, kapılarını aralamak, dönüşüm yolculuğu, yolculuğa çıkmak, yeni bir sayfa açmak, köprü kurmak, ufuk açıcı, çıtayı yükseltmek, potansiyelini açığa çıkarmak.
- **Neden yapay:** Somut bir bilgi yerine duygu yükü taşıyan genel mecazlar kullanılır. Kurumsal ve pazarlama metinlerinde yapay zekanın en bariz izidir.
- **Ne yapmalı:** Mecazın arkasındaki somut iddiayı yazın. Kaynakta somut bir iddia yoksa düz ve sade bir ifadeye indirin.
- **Dokunma:** Edebi metin ve kullanıcının bilinçli üslubu.
- **Güç:** orta
- **Önce:** *Bu iş birliği, eğitimde dijital dönüşüm yolculuğumuza yeni bir boyut kazandıracak.*
- **Sonra:** *Bu iş birliğiyle eğitimde dijitalleşme çalışmalarımızı genişleteceğiz.*

<a id="soz-07"></a>
### SOZ-07 · Adlaştırma zinciri ve boş yardımcı fiil

- **Belirti:** Eylemin ada çevrilip başka bir fiile yüklendiği zincirler: "yedeklenmesinin sağlanması gerekmektedir", "incelemesinin yapılması", "ödemenin gerçekleştirilmesi". Asıl işi ad taşır, "gerçekleştirmek", "sağlamak", "yapmak", "icra etmek" yalnızca çekim eki taşır.
- **Neden yapay:** Bürokratik yazının alışkanlığıdır ve modeller "resmi" görünmek için buna yaslanır. Okur eylemi bulmak için zinciri sondan başa çözmek zorunda kalır.
- **Ne yapmalı:** Addaki eylemi yeniden fiil yapın ve doğrudan çekimleyin: "ödemenin gerçekleştirilmesi" → "ödemek", "yapılması gerekmektedir" → "yapılmalı". Eylemi kimin yaptığı kaynakta belli değilse edilgen bırakın, özne uydurmayın.
- **Dokunma:** Yerleşik birleşik fiiller ("katkıda bulunmak", "yardım etmek", "karar vermek") boş fiil değildir. Mevzuat ve sözleşme dilinde zincir kalıbın parçası olabilir.
- **Güç:** orta
- **Önce:** *Verilerin haftalık olarak yedeklenmesinin sağlanması gerekmektedir. Geçiş işlemi cumartesi günü gerçekleştirilecektir.*
- **Sonra:** *Veriler haftada bir yedeklenmeli. Geçiş cumartesi günü yapılacak.*

<a id="soz-08"></a>
### SOZ-08 · Derin görünen vecize

- **Belirti:** meselenin özü, asıl soru şu, asıl mesele, işin özünde, özünde, işin aslı; özlü söz kılığında genellemeler: "Şeffaflık, güvenin dilidir.", "Veri, yeni petroldür.", "Verimlilik, insanı unuttuğunuzda bir tuzağa dönüşür."
- **Neden yapay:** Sıradan bir tespit gizli bir hakikat ya da özlü söz kılığına sokulur. Kılık bilgi eklemez, yalnızca ağırlık verir.
- **Ne yapmalı:** Vecizenin arkasındaki somut iddiayı yazın. Kaynakta somut bir iddia yoksa düz ve ölçülü söyleyin, iddia uydurmayın.
- **Dokunma:** Deneme ve köşe yazısında yazarın kendi kurduğu, metinde bir kez geçen özlü söz. Alıntılanan atasözü ve deyim. "Asıl" sözcüğünün gerçek bir karşıtlık bildirdiği kullanım ("Asıl sözleşme ekte.").
- **Güç:** güçlü
- **Önce:** *Asıl soru, ekiplerin değişime uyum sağlayıp sağlayamayacağı. Meselenin özünde ise kurum kültürü yatıyor. Şeffaflık, güvenin dilidir.*
- **Sonra:** *Ekiplerin değişime uyum sağlaması her şeyden önce kurum kültürüne bağlı. Şeffaf davranan kurumlara daha çok güvenilir.*

<a id="soz-09"></a>
### SOZ-09 · Kaynaksız otorite

- **Belirti:** "Uzmanlara göre", "Uzmanlar ... konusunda hemfikir", "Araştırmalar gösteriyor ki", "Yapılan pek çok çalışma açıkça ortaya koymaktadır", "Bilim insanları uyarıyor", "Sektör liderleri ... vurguluyor". Ardından hiçbir kaynak gelmiyor.
- **Neden yapay:** Model iddiaya ağırlık vermek için belirsiz bir otorite çağırır. Okur kimin, nerede, ne söylediğini öğrenemez.
- **Ne yapmalı:** Kaynak metinde adıyla geçiyorsa (bir kurum, bir yıl, bir yayın) atfı ona bağlayın. Geçmiyorsa **atfı silmeyin:** Silerseniz iddia yazarın kendi iddiasına dönüşür ve güçlenir. Yalnızca şişirmeyi ("pek çok", "açıkça ortaya koymaktadır") azaltın ve kaynağın belirtilmediğini kullanıcıya notta söyleyin. Kaynak uydurmayın.
- **Dokunma:** Kaynak gösterilen atıflar. Akademik metinde ardından kaynakça gelen "çalışmalar göstermektedir" cümlesi.
- **Güç:** orta
- **Önce:** *Uzmanlar, ekran süresinin çocukların dikkatini olumsuz etkilediği konusunda hemfikir. Yapılan pek çok araştırma da bunu açıkça ortaya koymaktadır.*
- **Sonra:** *Uzmanlar ekran süresinin çocukların dikkatini olumsuz etkilediği konusunda hemfikir, araştırmalar da bunu destekliyor.* (Notta: "Kaynak metin hangi uzmanlara ve araştırmalara dayandığını belirtmiyor.")

---

<a id="cev-01"></a>
### CEV-01 · Çeviri deyimler

- **Belirti:** günün sonunda (*at the end of the day*), derinlemesine dalmak (*deep dive*), oyunun kurallarını değiştiren (*game-changer*), masaya getirmek (*bring to the table*), bir adım öne çıkmak (*step up*), aynı sayfada olmak (*be on the same page*), kutunun dışında düşünmek (*think outside the box*), ileriye dönük (*going forward*), kazan-kazan.
- **Neden yapay:** İngilizce deyimlerin sözcük sözcük çevirisidir. Türkçe okur bunları ya yadırgar ya da "plaza dili" olarak algılar.
- **Ne yapmalı:** Türkçe karşılığını ya da düz anlamını kullanın: günün sonunda → sonuçta / nihayetinde; derinlemesine dalmak → ayrıntılı incelemek; oyunun kurallarını değiştiren → alışılmış düzeni değiştiren / çığır açan (ölçülü); masaya getirmek → katmak, sunmak; aynı sayfada olmak → aynı fikirde olmak, uzlaşmak.
- **Dokunma:** Kullanıcı bilinçli olarak plaza dili ya da ironik bir dil kullanıyorsa.
- **Güç:** güçlü
- **Önce:** *Bu yazıda yapay zekanın eğitimdeki rolüne derinlemesine dalacağız. Günün sonunda, bu teknoloji oyunun kurallarını değiştiren bir güç.*
- **Sonra:** *Bu yazıda yapay zekanın eğitimdeki yerini ayrıntılı olarak inceliyoruz. Sonuçta bu teknoloji, öğretimin alışılmış düzenini değiştiriyor.*

<a id="cev-02"></a>
### CEV-02 · "-e sahip olmak" fazlalığı

- **Belirti:** "geniş bir deneyime sahip", "yüksek bir performansa sahiptir", "üç odaya sahip", "önemli bir yere sahiptir".
- **Neden yapay:** İngilizce *have/has* yapısının çevirisidir. Türkçe bunu çoğu zaman "-lı/-li", "var" ya da doğrudan sıfatla söyler.
- **Ne yapmalı:** "-lı/-li" ekini, "var/yok" yapısını ya da isim cümlesini kullanın.
- **Dokunma:** Mülkiyet ya da hak vurgusu ("şirketin %51'ine sahip", "telif hakkına sahip").
- **Güç:** orta
- **Önce:** *Ekibimiz geniş bir deneyime sahip olup ürünümüz yüksek bir performansa sahiptir.*
- **Sonra:** *Ekibimiz deneyimli, ürünümüz de yüksek performanslı.*

<a id="cev-03"></a>
### CEV-03 · "tarafından" ve "için" yığılması

- **Belirti:** "X tarafından geliştirilen Y tarafından kullanılan", "bu, kullanıcılar için önemlidir", "işletmeler için faydalı olmak".
- **Neden yapay:** İngilizce *by* ve *for* yapılarının çevirisidir. Türkçede etken çatı ve yönelme durumu daha doğaldır.
- **Ne yapmalı:** "X tarafından yapılan" → "X'in yaptığı". "Y için önemli" → bağlama göre "Y'yi ilgilendirir", "Y'nin işine yarar".
- **Dokunma:** Resmi yazışmada ve akademik metinde tek bir "tarafından". Kurum adı geçen resmi bildirimler.
- **Güç:** orta
- **Önce:** *Ekibimiz tarafından geliştirilen bu araç, küçük işletmeler için oldukça faydalı olacaktır.*
- **Sonra:** *Ekibimizin geliştirdiği bu araç küçük işletmelerin işine yarayacak.*

<a id="cev-04"></a>
### CEV-04 · Gereksiz iyelik zamiri ve "bir"

- **Belirti:** "bizim ekibimiz", "sizin hesabınız", "onun fikri" (iyelik eki zaten varken). "Bir" sözcüğünün belirsiz tanımlık (*a/an*) gibi her ada eklenmesi: "harika bir fırsat sunan bir platform".
- **Neden yapay:** Türkçede iyelik eki kişiyi zaten gösterir. Zamir yalnızca vurgu için kullanılır. "Bir" ise İngilizcedeki tanımlık refleksiyle çoğalır.
- **Ne yapmalı:** Vurgu yoksa zamiri silin. Fazladan "bir"leri ayıklayın.
- **Dokunma:** Karşıtlık vurgusu ("Bizim ekibimiz değil, onların ekibi yaptı.").
- **Güç:** tek başına zayıf
- **Önce:** *Bizim ekibimiz sizin projeniz için harika bir çözüm sunan bir yaklaşım geliştirdi.*
- **Sonra:** *Ekibimiz projeniz için yeni bir yaklaşım geliştirdi.* ("harika" bilgi taşımıyor. "çözüm sunan" ise "yaklaşım"ın tekrarı.)

<a id="cev-05"></a>
### CEV-05 · "bir şekilde" zarfları

- **Belirti:** "hızlı bir şekilde", "etkili bir biçimde", "sorunsuz bir şekilde", "güvenli bir şekilde", "detaylı bir şekilde".
- **Neden yapay:** İngilizce *-ly* zarflarının sözcük sözcük karşılığıdır. Türkçede sıfat çoğu zaman olduğu gibi zarf olur ("hızlı yürüdü") ya da "-ca/-ce" ekini alır.
- **Ne yapmalı:** "bir şekilde"yi silip sıfatı yalın bırakın ya da "-ca/-ce", "-arak" kullanın. Zarf bilgi taşımıyorsa ("sorunsuz bir şekilde çalışır") tamamen atın.
- **Dokunma:** Belirsizlik bildiren gerçek kullanım ("bir şekilde hallettik", "öyle ya da böyle" anlamında).
- **Güç:** orta
- **Önce:** *Dosyalarınızı güvenli bir şekilde saklar, ekibinizle hızlı bir şekilde paylaşmanıza olanak tanır.*
- **Sonra:** *Dosyalarınızı güvenle saklar, ekibinizle hızlıca paylaşmanızı sağlar.*

<a id="cev-06"></a>
### CEV-06 · Okunuşa uymayan ek

- **Belirti:** Yabancı sözcüğe ya da kısaltmaya gelen ekin okunuşa değil yazılışa göre seçilmesi: "cache'ı", "Slack'de", "Chrome'yi", "TDK'ya".
- **Neden yapay:** Model eki sözcüğün son harfine bakarak seçer. Türkçe yazan biri sözcüğü nasıl okuyorsa eki ona göre getirir.
- **Ne yapmalı:** Eki okunuşa uydurun: "cache'i" (keş), "Slack'te" (silek), "Chrome'u" (krom). Kısaltmalarda kural TDK'dandır, yabancı sözcüklerde yerleşik uygulamadır. Bkz. `noktalama.md` §5. Terimin kendisine dokunmayın.
- **Dokunma:** Okunuşu kişiden kişiye değişen sözcükler ("SQL": es-kü-el ya da sikıl). Metindeki tercih tutarlıysa kalır.
- **Güç:** kural
- **Önce:** *Yayına almadan önce cache'ı temizleyip durumu Slack'de duyurduk.*
- **Sonra:** *Yayına almadan önce cache'i temizleyip durumu Slack'te duyurduk.*

---

<a id="nok-01"></a>
### NOK-01 · Cümle içinde uzun çizgi (—)

- **Belirti:** Cümle içinde ara söz, açıklama ya da ani dönüş için "—" kullanılıyor.
- **Neden yapay:** TDK'ya göre uzun çizgi yalnızca satır başındaki konuşmaları gösterir. Cümle içindeki kullanım İngilizce tipografiden gelir ve yapay zeka metinlerinin en kolay fark edilen izidir.
- **Ne yapmalı:** Ara söz için virgül, -kısa çizgi- ya da ayraç. Açıklama için iki nokta. Ani dönüş için nokta ve yeni cümle. Bkz. `noktalama.md` §1.
- **Dokunma:** Satır başındaki diyalog çizgisi. Kullanıcının açıkça korumak istediği tipografi.
- **Güç:** güçlü
- **Önce:** *Toplantıda tek bir konu konuşuldu — bütçe. Herkes — finans ekibi de dahil — şaşırdı.*
- **Sonra:** *Toplantıda tek bir konu konuşuldu: bütçe. Finans ekibi de dâhil herkes şaşırdı.*

<a id="nok-02"></a>
### NOK-02 · "ve"den önce virgül

- **Belirti:** Sıralamada son öğeden önce "..., ve ..." (Oxford virgülü).
- **Neden yapay:** İngilizce noktalama kuralıdır. TDK'ya göre "ve, veya, ya da" öncesine virgül konmaz.
- **Ne yapmalı:** Virgülü silin.
- **Dokunma:** —
- **Güç:** kural
- **Önce:** *Tasarım, geliştirme, ve test aşamaları tamamlandı.*
- **Sonra:** *Tasarım, geliştirme ve test aşamaları tamamlandı.*

<a id="nok-03"></a>
### NOK-03 · İngilizce sayı ve yüzde biçimi

- **Belirti:** *25%*, *3.5 milyon*, *1,200 kişi*.
- **Neden yapay:** Türkçede yüzde işareti önde (*%25*), ondalık ayırıcı virgül (*3,5*), binlik ayırıcı noktadır (*1.200*).
- **Ne yapmalı:** Biçimi düzeltin, **değeri asla değiştirmeyin.** "1,200" ifadesinin binlik mi ondalık mı olduğu bağlamdan net değilse dokunmayın ve özette belirtin.
- **Dokunma:** Kod, sürüm numarası (*v2.5*), IP adresi, ürün kodu, alıntılanmış İngilizce veri.
- **Güç:** kural
- **Önce:** *Satışlar 12.5% artarak 3,400 adede ulaştı.*
- **Sonra:** *Satışlar %12,5 artarak 3.400 adede ulaştı.*

<a id="nok-04"></a>
### NOK-04 · Ünlem ve emoji bolluğu

- **Belirti:** Her paragraf ünlemle bitiyor. Madde başlarında 🚀 ✅ 💡 gibi emojiler var.
- **Neden yapay:** Sosyal medya için üretilmiş yapay zeka metninin tipik süslemesidir.
- **Ne yapmalı:** Ünlemleri metin başına en fazla bire indirin. Emojileri, kullanıcı açıkça istemedikçe kaldırın ya da bire indirin.
- **Dokunma:** Kullanıcının kendi markasının bilinçli sosyal medya dili.
- **Güç:** orta
- **Önce:** *Büyük haber! 🚀 Yeni ürünümüz yayında! Hemen deneyin! 💡*
- **Sonra:** *Yeni ürünümüz yayında. Hemen deneyebilirsiniz!*

---

<a id="bic-01"></a>
### BIC-01 · Gereksiz başlık, madde işareti ve kalın yazı

- **Belirti:** Üç paragraflık bir e-postada başlıklar, her cümlenin madde işaretine dönüşmesi, cümle ortalarında **kalın** yazılmış sözcükler.
- **Neden yapay:** Modeller her metni bir rapor gibi yapılandırır. Akıcı bir metin parçalanınca okur bağlantıları kendisi kurmak zorunda kalır.
- **Ne yapmalı:** Kısa metinde başlıkları kaldırın. Birbiriyle ilişkili maddeleri düzyazıya çevirin. Kalın yazıyı yalnızca gerçekten taranacak bilgi (tarih, son gün) için bırakın. **İçerik aynen korunmalıdır:** Maddedeki her bilgi düzyazıda da yer almalıdır.
- **Dokunma:** Adım adım talimatlar, gerçekten taranacak listeler, kullanıcının belirlediği şablon.
- **Güç:** orta
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
### BIC-02 · Kalın etiketli madde

- **Belirti:** Her maddenin kalın bir etiket ve iki noktayla başladığı listeler: "**Hız:** Sayfalar daha çabuk açılır.", "**Güvenlik:** Veriler şifrelenir." Çoğu zaman etiket, ardından gelen cümlenin bir sözcüğünü tekrar eder.
- **Neden yapay:** Sohbet modellerinin en tanıdık cevap şablonudur. Düz bir paragrafla söylenebilecek iki üç bilgiyi sunum slaytına çevirir.
- **Ne yapmalı:** Madde sayısı azsa düzyazıya çevirin. Liste gerçekten gerekiyorsa etiketi kaldırıp maddeyi yalın bir cümle olarak yazın. Etiketteki bilgi cümlede yoksa cümleye taşıyın, kaybetmeyin.
- **Dokunma:** Sözlükçe, özellik tablosu, SSS gibi etiketin gerçekten aranacak bir başlık olduğu listeler. Kullanıcının şablonu.
- **Güç:** orta
- **Önce:**
  ```
  - **Hız:** Yeni sürümde sayfalar daha hızlı açılır.
  - **Güvenlik:** Bütün veriler şifrelenerek saklanır.
  ```
- **Sonra:** *Yeni sürümde sayfalar daha hızlı açılır, bütün veriler de şifrelenerek saklanır.*

<a id="bic-03"></a>
### BIC-03 · Başlığı ilk cümlede tekrarlama

- **Belirti:** Başlığın hemen altında başlığı cümleye çeviren bir giriş var. "## Güvenlik" başlığının altında "Güvenlik, her sistemin en önemli parçasıdır." gibi.
- **Neden yapay:** Model her bölüme bir giriş cümlesi koyar. Başlık konuyu zaten söylemiştir, giriş cümlesi okura yeni bir şey vermez.
- **Ne yapmalı:** Başlığı tekrar eden cümleyi silin, bölüm asıl bilgiyle başlasın.
- **Dokunma:** Başlıktan fazlasını söyleyen, bölümün kapsamını ya da sonucunu veren gerçek bir giriş cümlesi.
- **Güç:** orta
- **Önce:**
  ```
  ## Yedekleme
  Yedekleme, veri güvenliğinin temel taşıdır.
  Sistem her gece 02.00'de veritabanının tam yedeğini alır.
  ```
- **Sonra:**
  ```
  ## Yedekleme
  Sistem her gece 02.00'de veritabanının tam yedeğini alır.
  ```

<a id="bic-04"></a>
### BIC-04 · Metnin kendini anlatması

- **Belirti:** Metin konusunu değil kendini anlatıyor. Okurun zaten gördüğü düzeni ("Aşağıdaki tablo üç paketi karşılaştırmaktadır.", "Bu bölüm ekiplere göre düzenlenmiştir."), nasıl hazırlandığını ("Bu rapor çeşitli kaynaklardan derlenmiş olup doğrulanamayan bilgiler işaretlenmiştir.") ya da neyin yerine geldiğini ("Bu fonksiyon eski yöntemin yerine eklenmiştir.") söylüyor.
- **Neden yapay:** Modelin çalışma notu ya da yapıyı açıklama refleksi okura kalmıştır.
- **Ne yapmalı:** Okurun göremediği bir bilgi yoksa silin. Okurun ne yapacağını değiştiren bir uyarı varsa (ör. iki fiyat doğrulanmadı) onu konunun diliyle tek cümlede söyleyin. Önceki sürümden söz etmeyi sürüm notlarına bırakın.
- **Dokunma:** Sürüm notları, değişiklik günlüğü, geçiş kılavuzu. Okurun izleyebileceği kaynak gösterimi. Akademik metinde yöntem açıklaması.
- **Güç:** orta
- **Önce:** *Bu bölümde hizmet paketlerinin fiyatları karşılaştırılmaktadır. Aşağıdaki fiyatlar her firmanın kendi sitesinden derlenmiş olup doğrulanamayan bilgiler işaretlenmiştir.*
- **Sonra:** *Fiyatlar firmaların kendi sitelerinde yayımladığı fiyatlardır. İşaretli olanlar doğrulanamadı.*

---

<a id="dol-01"></a>
### DOL-01 · Açılış dolguları ve sahneli giriş

- **Belirti:** "Harika bir soru!", "Elbette!", "Tabii ki, işte ...", "Bu yazıda ... ele alacağız", "Merhaba! Bugün sizlerle ... paylaşmak istiyorum". Asıl söze geçmeden önce onu sahneleyen girişler: "Gelin birlikte bakalım.", "Hadi başlayalım!", "Lafı uzatmadan ...", "İşin aslı şu:", "Açık konuşalım:", "Bilmeniz gerekenler şunlar:", "İşte işin püf noktası:".
- **Neden yapay:** Sohbet modelinin cevap refleksidir. Sahneli giriş, söyleyeceği şeyi söylemek yerine onu duyurur ya da sahte bir içtenlik anı kurar. İkisi de metne bilgi katmaz.
- **Ne yapmalı:** Silin, metin doğrudan konuyla başlasın. Sahneli girişin duyurduğu noktayı doğrudan söyleyin.
- **Dokunma:** Mektup ve e-postadaki olağan selamlama ("Merhaba Ayşe Hanım,"). Cümle içinde geçen gündelik bir "açıkçası" ya da "bakın". İz, olağan bir iddianın önüne tek başına konan giriştir.
- **Güç:** güçlü
- **Önce:** *Harika bir soru! Bu yazıda uzaktan çalışmanın avantajlarını ele alacağız.*
- **Sonra:** *Uzaktan çalışmanın birkaç avantajı var.*
- **Önce (sahneli giriş):** *Lafı uzatmadan konuya girelim. İşin aslı şu: Önbellek üç katmanda çalışıyor.*
- **Sonra:** *Önbellek üç katmanda çalışıyor.*

<a id="dol-02"></a>
### DOL-02 · Kapanış dolguları

- **Belirti:** "Umarım yardımcı olur!", "Başka sorunuz olursa çekinmeden sorun.", "Bu konuda daha fazla bilgi almak isterseniz ...", "Unutmayın, ...".
- **Neden yapay:** Sohbet modelinin kapanış refleksidir.
- **Ne yapmalı:** Silin. E-postada gerçek bir iletişim daveti gerekiyorsa sade bir kapanış bırakın ("Sorunuz olursa yazabilirsiniz.").
- **Dokunma:** E-postanın imza bloğu ve olağan kapanışı ("Saygılarımla,").
- **Güç:** güçlü
- **Önce:** *Umarım bu bilgiler size yardımcı olur! Başka bir sorunuz olursa çekinmeden sormaktan lütfen çekinmeyin.*
- **Sonra:** *(silinir)*

<a id="dol-03"></a>
### DOL-03 · Model notu: bilgi sınırı ve tahmin

- **Belirti:** Modelin kendi bilgisinden söz ettiği notlar: "bilgi kesim tarihim itibarıyla", "mevcut bilgilere göre", "erişebildiğim kaynaklarda", "kamuya açık kaynaklarda ayrıntılı bilgi bulunmamakla birlikte", "bu konuda sınırlı bilgi bulunmaktadır". Çoğu zaman ardından boşluğu dolduran bir tahmin gelir: "muhtemelen 1990'larda kurulmuştur", "büyük olasılıkla orta gelirli bir ailede büyümüştür".
- **Neden yapay:** Modelin kendi sınırına dair notu, okura yazılmış metne karışmıştır. Ardından gelen tahmin, boşluğu makul görünen bir ayrıntıyla doldurur.
- **Ne yapmalı:** Modelin kendinden söz eden kısmını silin. Kaynağın bir bilgiyi vermediği gerçekse bunu düz bir cümleyle söyleyin. Tahmine dokunmayın, temkinini de koruyun: Onu silmek de kesinleştirmek de anlamı değiştirir. Tahminin kaynak metinde de dayanaksız olduğunu kullanıcıya notta belirtin.
- **Dokunma:** Okura bir kaynağın eksik olduğunu bildirmesi gereken metinler (araştırma notu, haber). Bu durumda da model diliyle değil, konunun diliyle.
- **Güç:** güçlü
- **Önce:** *Bilgi kesim tarihim itibarıyla şirketin kuruluşuna dair kamuya açık ayrıntılı bilgi bulunmamakla birlikte, muhtemelen 1990'lı yıllarda kurulduğu düşünülmektedir.*
- **Sonra:** *Şirketin kuruluş tarihi kaynaklarda geçmiyor, muhtemelen 1990'larda kuruldu.* (Notta: "1990'lar tahmini kaynak metinde de bir dayanağa bağlanmamış.")

---

<a id="oku-01"></a>
### OKU-01 · Okurun bildiğini yeniden anlatma

- **Belirti:** Bir yanıt (e-posta cevabı, kod incelemesi yorumu, mesajlaşma uygulamasındaki cevap) sorunu baştan tanımlıyor, karşı tarafın zaten bildiği arka planı anlatıyor, kanıtları sıralıyor ve asıl cevabı son cümleye bırakıyor.
- **Neden yapay:** Model, hiçbir bağlamı olmayan bir okura yazıyormuş gibi yazar. Yanıtın okuru ise konuşmanın içindedir. Cümlelerin her biri tek başına düzgün olduğu için bu iz cümle düzeyindeki düzeltmelerden sağ çıkar.
- **Ne yapmalı:** Cevabı ya da kararı başa alın. Okurun bilmediği ve kararını etkileyecek bilgiyi tutun. Yalnızca okurun kendi yazdığı ya da konuşmada açıkça kabul ettiği bilgiyi silin. Konuşmanın öncesi görünmüyorsa yalnızca sırayı değiştirin, silmeyin.
- **Dokunma:** Bağımsız belgeler (rapor, makale, dokümantasyon). Konuşmaya yeni katılan birine yazılan özet. Okur için gerçekten yeni olan kanıt.
- **Güç:** orta
- **Önce:** (Ayşe'nin sorusu: "Ödeme hatası için bu hafta düzeltme çıkabilir mi?") *Merhaba Ayşe, ödeme sayfasında kullanıcıların kartla öderken hata aldığını biliyorsun. Sorunu inceledik: Banka entegrasyonundaki zaman aşımı süresi 10 saniyeydi ve yoğun saatlerde bu süre yetmiyordu. Süreyi 30 saniyeye çıkardık ve test ortamında 200 deneme yaptık, hiçbiri hata vermedi. Bu yüzden düzeltmeyi perşembe günü yayına alabiliriz.*
- **Sonra:** *Merhaba Ayşe, evet, düzeltmeyi perşembe günü yayına alabiliriz. Hata, banka entegrasyonundaki 10 saniyelik zaman aşımının yoğun saatlerde yetmemesinden çıkıyordu. Süreyi 30 saniyeye çıkardık, test ortamındaki 200 denemenin hiçbiri hata vermedi.*

---

<a id="yaz-01"></a>
### YAZ-01 · Bağlaç de/da

- **Belirti:** "bende geliyorum", "Ali'de biliyor", "gidip te".
- **Neden yapay:** Yapay zekadan çok insan hatasıdır, ama metin düzeltilirken yakalanmalıdır.
- **Ne yapmalı:** Bağlaç de/da'yı ayırın, kesmeyi kaldırın, "te/ta"yı "de/da" yapın. Bkz. `noktalama.md` §4.
- **Dokunma:** Bulunma eki (-de/-da/-te/-ta) bitişik kalır.
- **Güç:** kural
- **Önce:** *Bende bu toplantıya katılacağım, Elif'te gelecek.*
- **Sonra:** *Ben de bu toplantıya katılacağım, Elif de gelecek.*

<a id="yaz-02"></a>
### YAZ-02 · ki

- **Belirti:** "demekki", "halbuki" (TDK: hâlbuki), "yarın ki toplantı", "masada ki kitap".
- **Neden yapay:** Yapay zekadan çok insan hatasıdır, ama metin düzeltilirken yakalanmalıdır.
- **Ne yapmalı:** Bağlaç "ki"yi ayırın (yedi kalıplaşmış söz hariç: belki, çünkü, hâlbuki, mademki, meğerki, oysaki, sanki). Ek olan "-ki"yi bitiştirin.
- **Dokunma:** —
- **Güç:** kural
- **Önce:** *Yarın ki toplantıda konuşacağız, demekki karar ertelendi.*
- **Sonra:** *Yarınki toplantıda konuşacağız, demek ki karar ertelendi.*

<a id="yaz-03"></a>
### YAZ-03 · Soru eki mi

- **Belirti:** "gelecekmisin", "doğrumu", "biliyormusun".
- **Neden yapay:** Yapay zekadan çok insan hatasıdır, ama metin düzeltilirken yakalanmalıdır.
- **Ne yapmalı:** Soru ekini ayırın. Sonraki ekleri soru ekine bitiştirin.
- **Dokunma:** —
- **Güç:** kural
- **Önce:** *Raporu yarına yetiştirebilecekmisiniz?*
- **Sonra:** *Raporu yarına yetiştirebilecek misiniz?*

<a id="yaz-04"></a>
### YAZ-04 · Kesme işareti

- **Belirti:** Kurum adlarına kesme ("Türk Dil Kurumu'na"), yapım ekine kesme ("Türkiye'li"), kısaltmaya yanlış ünlü ("TDK'ya").
- **Neden yapay:** Kurum adına kesme koymak hem insanların hem modellerin sık yaptığı bir hatadır. Kısaltmaya gelen yanlış ek ise CEV-06'daki okunuş sorununun bir türüdür.
- **Ne yapmalı:** Kurum adlarında kesmeyi kaldırın, yapım ekinde ayırmayın, kısaltmaya gelen eki okunuşa uydurun. Bkz. `noktalama.md` §5.
- **Dokunma:** Kullanıcının marka adı yazımı (marka kendi adını kesmeyle yazıyorsa). [Tartışmalı, bkz. CONTRIBUTING.]
- **Güç:** kural
- **Önce:** *Başvurular Ankara Üniversitesi'ne yapılacak, sonuçlar TDK'ya bildirilecek.*
- **Sonra:** *Başvurular Ankara Üniversitesine yapılacak, sonuçlar TDK'ye bildirilecek.*

<a id="yaz-05"></a>
### YAZ-05 · Büyük harf

- **Belirti:** "Kasım ayında" (genel zaman), "Türk Lirası" (para birimi), "İstanbul İli", iki noktadan sonra öbeğin büyük harfle başlaması.
- **Neden yapay:** İngilizcede ay adları ve para birimi adları büyük harfle yazılır, iki noktadan sonra da büyük harf olağandır. Modeller bu alışkanlığı Türkçeye taşır.
- **Ne yapmalı:** Bkz. `noktalama.md` §3 ve §6.
- **Dokunma:** Başlıkların büyük harf düzeni (metin içinde tutarlıysa).
- **Güç:** kural
- **Önce:** *Fiyatlar Kasım ayında 500 Türk Lirası'na çıkacak. Üç seçenek var: Aylık, yıllık ve ömür boyu.*
- **Sonra:** *Fiyatlar kasım ayında 500 Türk lirasına çıkacak. Üç seçenek var: aylık, yıllık ve ömür boyu.*

<a id="yaz-06"></a>
### YAZ-06 · Sık yazım hataları

- **Belirti:** "birşey", "herşey", "hiç bir", "bir çok", "bir kaç", "pekçok", "yada", "yanlız".
- **Neden yapay:** Yapay zekadan çok insan hatasıdır, ama metin düzeltilirken yakalanmalıdır.
- **Ne yapmalı:** Doğru yazımı kullanın: bir şey, her şey, hiçbir, birçok, birkaç, pek çok, ya da, yalnız. Liste için bkz. `noktalama.md` §8.
- **Dokunma:** Alıntılar ve kullanıcının olduğu gibi aktardığı mesajlar.
- **Güç:** kural
- **Önce:** *Bir çok kullanıcı herşeyin yolunda olduğunu yada hiç bir sorun yaşamadığını söyledi.*
- **Sonra:** *Birçok kullanıcı her şeyin yolunda olduğunu ya da hiçbir sorun yaşamadığını söyledi.*

---

## Aşırı düzeltme

Bu bölümdeki örüntüler kaynak metinde değil, **düzeltilmiş metinde** aranır. Bir izi silerken yerine yenisini koymak, izi bırakmaktan daha kötüdür: Metin hem değişmiş hem de yine yapay kalmış olur. Yeniden yazımı bitirdikten sonra çıktıyı bu beş soruyla okuyun. Buradaki bloklar önce/sonra yerine kaynak, aşırı düzeltme ve yerinde düzeltme üçlüsünü gösterir.

<a id="asi-01"></a>
### ASI-01 · Yedek sözcük tiki

- **Belirti:** Silinen klişelerin yerine her seferinde aynı "doğal" sözcük geliyor: "aslında", "açıkçası", "doğrusu", "işin özü", "gerçekten".
- **Neden yapay:** Yasak listesiyle çalışmanın yan etkisidir. Boşalan yere bir şey koyma refleksi, eski tikin yerine yenisini üretir.
- **Ne yapmalı:** Klişeyi sildiğiniz yere hiçbir şey koymadan cümleyi okuyun. Ayakta duruyorsa öyle bırakın.
- **Dokunma:** Kaynak metinde zaten bulunan ve anlam taşıyan söylem sözcükleri.
- **Kaynak:** *Bu bağlamda, yeni panel son derece hızlıdır. Sonuç olarak, kullanıcılar memnundur.*
- **Aşırı düzeltme:** *Aslında yeni panel gerçekten hızlı. Açıkçası kullanıcılar da memnun.*
- **Yerinde düzeltme:** *Yeni panel hızlı, kullanıcılar da memnun.*

<a id="asi-02"></a>
### ASI-02 · Kılık değiştiren kalıp

- **Belirti:** Bir kalıp silinirken aynı iskeletin başka bir biçimi kuruluyor: "sadece X değil, aynı zamanda Y" yerine "X değil, Y", "X'in ötesinde Y", "X'ten çok Y". Uzun çizgi yerine her yere iki nokta ya da üç nokta konması da aynı hatadır.
- **Neden yapay:** Sözcükler değişir, cümlenin hareketi aynı kalır. Okur kalıbı sözcüklerinden değil ritminden tanır.
- **Ne yapmalı:** Kalıbın arkasındaki bilgiyi çıkarın ve düz söyleyin. Karşıtlığın olumsuz yarısı bilgi taşımıyorsa atın.
- **Dokunma:** Kaynakta gerçek bir yanlış anlamayı düzelten karşıtlık (bkz. YAPI-06, Dokunma).
- **Kaynak:** *Bu sadece bir takvim uygulaması değil, aynı zamanda bir planlama asistanı.*
- **Aşırı düzeltme:** *Bu bir takvim uygulamasından çok, bir planlama asistanı.*
- **Yerinde düzeltme:** *Uygulama takvim tutmanın yanında planlamanıza da yardım ediyor.*

<a id="asi-03"></a>
### ASI-03 · Sahte samimiyet

- **Belirti:** Metni "insan" göstermek için eklenen ve kaynakta olmayan öğeler: uydurma bir anı, "itiraf edeyim", "hepimizin başına gelmiştir", okura dönük sohbet cümleleri, konuşma dili parçacıkları ("yani", "hani", "işte").
- **Neden yapay:** Bilgi eklemektir, değişmez kuralları çiğner. Kurumsal ya da teknik bir metinde registerı da bozar.
- **Ne yapmalı:** Eklediğiniz her sözcüğü silip okuyun. Anlamdan ve tondan bir şey eksilmiyorsa geri koymayın. Kaynakta olmayan hiçbir deneyim, duygu ya da ayrıntı yazmayın.
- **Dokunma:** Kaynak metindeki gerçek kişisel anlatım. Yazarın kendi anısı ve sesi korunur.
- **Kaynak:** *Yedekleme işlemi her gece 02.00'de otomatik olarak başlamaktadır.*
- **Aşırı düzeltme:** *Hepimiz bir gün dosyalarımızı kaybetmişizdir. İşte bu yüzden yedekleme her gece 02.00'de kendiliğinden başlıyor.*
- **Yerinde düzeltme:** *Yedekleme her gece 02.00'de kendiliğinden başlar.*

<a id="asi-04"></a>
### ASI-04 · Arı Türkçe merakı

- **Belirti:** Gündelik ve mesleki dilde yaşayan yabancı kökenli sözcüklerin zorlama karşılıklarla değiştirilmesi: "performans" → "başarım", "strateji" → "izlem", "e-posta" → "e-ileti". Meslek içinde İngilizcesiyle kullanılan terimlerin çevrilmesi: "pull request" → "çekme isteği", "middleware" → "ara katman yazılımı".
- **Neden yapay:** Bu skill bir dil arılaştırma aracı değildir. Hedef, okurun yadırgamadığı Türkçedir ve okur "performans" sözcüğünü yadırgamaz. Terim değiştirmek ayrıca değişmez kurallara aykırıdır.
- **Ne yapmalı:** Sözcük seçimine yalnızca çeviri kokan **kalıplarda** (bkz. `CEV` blokları) dokunun. Tek tek sözcüklerin kökenine bakmayın.
- **Dokunma:** Kullanıcı açıkça öz Türkçe bir üslup istiyorsa.
- **Kaynak:** *Yeni strateji, sistemin performansını artırmayı hedeflemektedir.*
- **Aşırı düzeltme:** *Yeni izlem, dizgenin başarımını artırmayı amaçlıyor.*
- **Yerinde düzeltme:** *Yeni strateji sistemin performansını artırmayı hedefliyor.*

<a id="asi-05"></a>
### ASI-05 · Aşırı gömme

- **Belirti:** Kısa cümleleri birleştirirken bütün bilginin sıfat-fiillerle tek bir adın önüne yığılması. Okur yükleme varana kadar üç dört yan cümleyi aklında tutmak zorunda kalıyor.
- **Neden yapay:** Tekdüzeliği kırmak için yapılan birleştirmenin dozu kaçmıştır. İngilizce iskeletin tersine dönmüş hâli de Türkçe okuru yorar.
- **Ne yapmalı:** Bir adın önünde en çok iki yan cümle bırakın. Fazlasını ayrı cümleye bölün.
- **Dokunma:** Hukuki ve akademik metinde uzun ad öbekleri türün gereği olabilir.
- **Kaynak:** *Bir araç geliştirdik. Araç faturaları tarıyor. Hataları işaretliyor. Geçen ay yayınladık.*
- **Aşırı düzeltme:** *Geçen ay yayınladığımız, faturaları tarayan ve hataları işaretleyen, bizim geliştirdiğimiz aracı kullanabilirsiniz.* (Ayrıca "kullanabilirsiniz" kaynakta yok.)
- **Yerinde düzeltme:** *Faturaları tarayıp hataları işaretleyen bir araç geliştirdik. Geçen ay yayınladık.*

---

## Yeni örüntü şablonu

Aşağıdaki bloğu kopyalayın, uygun kategoriye ekleyin, sıradaki numarayı verin ve dizine güç etiketiyle birlikte bir satır ekleyin.

```markdown
<a id="kat-nn"></a>
### KAT-NN · Kısa ad

- **Belirti:** Metinde nasıl görünür? Somut sözcükler ya da yapılar.
- **Neden yapay:** İnsan yazısından nasıl ayrışıyor? Kaynağı nedir (çeviri, model refleksi...)?
- **Ne yapmalı:** Hangi dönüşüm uygulanmalı? İlgili referans dosyasına bağlantı verin.
- **Dokunma:** Örüntünün meşru olduğu durumlar. Bu satır zorunludur.
- **Güç:** güçlü | orta | tek başına zayıf | kural (bkz. dosyanın başındaki Güç tablosu)
- **Önce:** *Özgün, yapay zeka tarzında bir örnek.*
- **Sonra:** *Anlamı, sayıları ve özel isimleri aynen koruyan düzeltilmiş hali.*
```
