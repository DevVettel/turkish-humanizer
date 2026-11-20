---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Ekip arkadaşım Murat Slack'te şunu sordu: "Staging'deki migration hatası için bugün deploy edebilir miyiz?"

Benim taslak cevabım aşağıda. Yapay zeka yazmış gibi durmasın, doğallaştır:

Merhaba Murat! Harika bir soru. Bildiğin gibi staging ortamında migration çalıştırılırken hata alınmaktadır. Sorunu detaylı bir şekilde inceledim: users tablosundaki email sütununa eklenen unique kısıtı, 42 tekrarlı kayıt nedeniyle başarısız oluyordu. Tekrarlı kayıtları temizleyen bir script yazdım ve staging'de üç kez denedim, her seferinde sorunsuz çalıştı. Sonuç olarak, bugün saat 17.00'den sonra deploy edebiliriz. Umarım yardımcı olmuştur!
