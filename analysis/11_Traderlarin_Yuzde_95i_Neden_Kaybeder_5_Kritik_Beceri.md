# 11 - Traderların %95’i Neden Kaybediyor? 5 Kritik Beceri

## 1. Beceri 1: Duygusal Kontrol (Kararları Ekran Kapalıyken Almak)
* Ekranda kırmızı/yeşil mumları izlerken beyinde kortizol ve dopamin savaşı başlar.
* Çözüm: **Tüm kararları ekran kapalıyken almak.**
* Giriş, stop ve hedef seviyeleri emir olarak sisteme girilir. Pozisyon açıldıktan sonra trader bir karar alıcı değil, sadece sürecin izleyicisi olmalıdır.

## 2. Beceri 2: Pusu Sabrı (Michael Burry Modeli)
* Sabır hiçbir şey yapmadan oturmak değil; avını bekleyen keskin nişancı gibi doğru anı pusuya yatarak beklemektir.
* **Katı Kural:** Mükemmel bir işlem için 5 filtre şartınız varsa ve piyasa o an size sadece 4'ünü veriyorsa, **o işlem pas geçilir**. 4/5 asla yeterli değildir.

## 3. Beceri 3: Sermaye Koruma (Hayatta Kalma Matematiği)
* Kumarbazlar ne kadar kazanacaklarına, profesyoneller ne kadar kaybedebileceklerine odaklanır.
* Tek işlemde risk **maksimum %1 - %2** olmalıdır. Bu sayede 10 işlem üst üste stop olsa bile kasanın %80-%90'ı sağlam kalır.

## 4. Beceri 4: Zihinsel Dayanıklılık (Entitlement Bias'ı Yok Etmek)
* Kırılmalar genelde para kaybından değil, "kusursuz analiz yaptım ama piyasa beni stop edip hedefime gitti, hakkım yendi" hissinden doğar.
* Piyasa adil bir yer olmak zorunda değildir. Zihinsel dayanıklılık, piyasanın rastgele fitillerini kişisel algılamamaktır.

## 5. Beceri 5: Rejim Adaptasyonu
* Piyasalar sürekli mutasyon geçiren organizmalardır. Geçen yıl çalışan bir strateji bu yıl çalışmayabilir.
* Kendi işlem günlüğünü okuyarak değişen piyasa rejimine adapte olmak zorunludur.

---

## 6. Tetik Entegrasyonu
* **`tetik/crates/signals/src/regime.rs`:** Piyasa rejimi (`Trend`, `Range`, `VolatileTransition`) tespit edilmeden hiçbir setup tetiklenemez.
