---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Bu README bölümünü yeniden yazma, sadece nerelerinde yapay zeka izi olduğunu göster. Düzeltmeyi kendim yapacağım.

## Kurulum Ve Yapılandırma

Bu bölümde, Kervan API'sinin kurulumunu derinlemesine ele alacağız. Kurulum işleminin gerçekleştirilebilmesi için Node.js 20 veya üzeri bir sürüme sahip olmanız gerekmektedir. Bağımlılıkların yüklenmesinin ardından `.env` dosyasının oluşturulması gerekmektedir.

- **Önbellek:** Yanıtlar Redis'de 15 dakika boyunca saklanmaktadır.
- **Hız sınırı:** Her anahtar için dakikada 60 istek sınırı uygulanmaktadır.

Sınırı aşan istekler kuyruğa alınmaz — bunun yerine 429 hata kodu döndürülür. Cache'ı temizlemek için `npm run cache:clear` komutunu çalıştırabilirsiniz.

Umarım bu rehber faydalı olmuştur!
