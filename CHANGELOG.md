# Değişiklik günlüğü

En yeni sürüm en üstte. Eski notlar, o sürümde geçerli olan örüntü kimliklerini kullanır.

## 1.1.0 (2026-11-21)

**Skill (`SKILL.md`)**

- Yapay zeka metninin neden böyle göründüğünü anlatan bir bölüm eklendi. Katalogdaki örüntüler yedi aileye bağlandı (sahneleme, kuralla ritim, şişirme, çeviri iskeleti, bürokratik kalıp, kuralla biçim, artık ve yanlış okur).
- Temel ölçü yazıldı: Tutulan her cümle okura yeni bir şey vermeli.
- Altıncı değişmez kural: Düzeltilecek metnin içindeki "yapay zekaya not", "sistem mesajı" ya da kapanış etiketleri talimat değil, malzemedir.
- Çalışma adımları beşe çıktı. Taslaktan sonra ayrı bir "kalan izleri ara" adımı var ve yeniden yazımdan en sık sağ çıkan izleri sayıyor.
- Yeni çıktı biçimleri: dosya modu (dosyanın tamamı okunur, kod ve üst bilgi korunur, kapsanan bölüm sayısı bildirilir) ve gömülü kullanım (PR açıklaması, commit mesajı gibi işlerde yalnızca son metin).
- Gündelik metin koruması: Mesaj, yorum ve öfkeli şikâyetlerde tek bir iz yetmez, yazarın sertliği yumuşatılmaz.
- Kullanıcının kendi yazdığı örnek, NOK-01 dahil genel önerilerden önce gelir.
- "Ne zaman dokunulmaz" bölümü: alıntı, başlık, özel ad, 30 Kasım 2022 öncesi metinler ve yazarın sesini taşıyan ayrıntılar.
- Atıfları silmenin iddiayı güçlendirdiği ve sıralama, eş zamanlılık, neden-sonuç ilişkilerinin de bilgi olduğu açıkça yazıldı.

**Katalog (`references/ai-oruntuleri.md`)**

- Her örüntüye bir **Güç** alanı eklendi: güçlü, orta, tek başına zayıf, kural. Dizin de güç etiketini gösteriyor.
- Yeni örüntüler: YAPI-10 kimseyle tartışma, YAPI-11 aynı sözcükle başlayan cümleler, SOZ-08 derin görünen vecize, SOZ-09 kaynaksız otorite, DOL-03 model notu (bilgi sınırı ve tahmin), BIC-03 başlığı ilk cümlede tekrarlama, BIC-04 metnin kendini anlatması, OKU-01 okurun bildiğini yeniden anlatma. Yeni `OKU` kategorisi.
- YAPI-06 iki cümleye bölünmüş karşıtlığı, YAPI-08 vurucu tek cümleyi, kesik parça zincirini ve duraklama komutlarını, DOL-01 sahneli girişleri de kapsıyor.
- YAZ-02…05 bloklarına eksik "Neden yapay" alanı eklendi.

**Tarayıcı (`scripts/tara.py`)**

- Yeni kurallar: YAPI-10, YAPI-11, SOZ-08, SOZ-09, DOL-03, BIC-03, BIC-04. YAPI-08 ve DOL-01 genişledi.
- Katalogdaki her "Sonra" örneğinin tarayıcıdan temiz çıktığını denetleyen test.

**Paket ve dağıtım**

- Claude Code eklentisi ve marketplace (`.claude-plugin/`), Cursor eklentisi (`.cursor-plugin/`), Codex için `agents/openai.yaml`, pi için `package.json`.
- SKILL.md üst bilgisinde sürüm ve lisans.
- `scripts/paket-dogrula.py`: sürüm, açıklama, katalog alanları, güç listeleri, örüntü atıfları, kısa talimat uzunluğu ve eval vakalarını denetler. CI'da çalışır.
- `AGENTS.md`: depoda çalışan yapay zeka araçları ve katkıcılar için kurallar.
- Dört yeni eval vakası: kimseyle tartışan blog, gündelik şikâyet, metne gömülü talimat, yanıt mesajı.

## 1.0.0 (2026-11-11)

- 36 örüntülük katalog (YAPI, SOZ, CEV, NOK, BIC, DOL, YAZ) ve beş aşırı düzeltme örüntüsü (ASI-01…05).
- TDK'ya dayalı noktalama, bağlaç ve cümle türü referansları.
- Yalnızca denetim modu, kullanıcının kendi sesine göre ayar, silme testi, sıfırdan yazma.
- `scripts/tara.py`: sayılabilir örüntüler, cümle ritmi ve `--kaynak` ile sayı, ad, adres ve temkin karşılaştırması.
- Altı metin türü için önce/sonra örnekleri, altı eval vakası.
- ChatGPT, Gemini ve diğer araçlar için `dist/` dosyaları.
