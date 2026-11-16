# 13 - İşlemlerin Yarısında Yanılıp Yine de Nasıl Para Kazanılır?

## 1. Olasılık Oyunu: Hileli Zar Deneyi
* Kazanma Oranı: %45 (İşlemlerin çoğunda yanılıyoruz)
* Risk: 1R
* Kazanç: 2R
* 100 işlemde: 55 kayıp (-55R) + 45 kazanç (+90R) = **+35R Net Kâr**.

---

## 2. R-Multiple Pozisyon Boyutlandırma Formülü

$$	ext{İşlem Lot Büyüklüğü} = rac{	ext{Toplam Sermaye} 	imes 	ext{Risk Yüzdesi (1R)}}{|	ext{Giriş Fiyatı} - 	ext{Stop Loss Fiyatı}|}$$

### Somut Hesaplama Örneği:
* Toplam Portföy: 100,000$
* İşlem Başına Risk (%1): 1,000$ ($1R$)
* **Senaryo A (Dar Stop):**
  * Giriş = 50$, Stop = 48$ (Fark = 2$)
  * $	ext{Lot} = rac{1,000}{2} = \mathbf{500 	ext{ Hisse}}$
* **Senaryo B (Geniş Stop):**
  * Giriş = 50$, Stop = 40$ (Fark = 10$)
  * $	ext{Lot} = rac{1,000}{10} = \mathbf{100 	ext{ Hisse}}$

> Stop mesafesi genişledikçe alınan lot küçülür; daraldıkça büyür. Ancak stop vurulduğunda kaybedilen tutar her zaman **kesinlikle 1,000$ (1R)** kalır.

---

## 3. R Dilinin Psikolojik Gücü
* "Bugün 5,000 TL kaybettim" demek hayatta kalma güdüsünü ve geçim stresini tetikler.
* "1R stop oldum" demek mekanik ve istatistiksel sürecin olağan bir maliyetidir.

---

## 4. Tetik Botu Formülü
`tetik` botunun emir motoru (`crates/exec/src/orders.rs`) emir boyutunu asla sabit kontrat adediyle değil, dinamik `risk_budget / stop_distance` formülüyle hesaplar.
