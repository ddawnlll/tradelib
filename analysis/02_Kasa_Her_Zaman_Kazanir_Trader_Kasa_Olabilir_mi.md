# 02 - Kasa Her Zaman Kazanır. Trader Kasa Olabilir mi?

## 1. Yönetici Özeti & Kasa Paradigması
Borsa bir kumarhane midir? Yanıt masanın hangi tarafında oturduğunuza bağlıdır. Oyuncu tarafında oturuyorsanız borsa dünyanın en acımasız kumarhanesidir. Ancak kasa tarafında oturuyorsanız borsa, matematiksel olasılıkların ve istatistiksel avantajın (edge) çalıştığı bir sermaye yönetim işidir.

Kasa her oyunu kazanmaz. Hatta bazı geceler zarar edebilir. Ancak kasanın sistemi 3 değişmez sütuna dayanır:
1. **Küçük ama Sabit Matematiksel Avantaj (Edge)**
2. **Çok Sayıda Tekrar (Büyük Sayılar Kanunu)**
3. **Katı Masa Limiti (Sınırlı & Sabit Risk)**

---

## 2. Kumarhane Matematiği vs Trader Avantajı

### Kumarhanenin Yeşil Sıfır Avantajı
* Avrupa ruletinde 37 hane bulunur (1-36 arası ve 0). Kırmızıya oynayanın kazanma olasılığı:
  $$P(	ext{Kırmızı}) = rac{18}{37} pprox 48.65\%$$
* Kasa yeşil sıfır sayesinde tek bir haneden ibaret avantaj elde eder:
  $$	ext{House Edge} = rac{1}{37} pprox 2.70\%$$
* Kasa 100$'lık bir bahiste ortalama sadece 2.70$ kazanır. Ancak gecede 1,000 tur oynandığında bu düzenli ve devasa bir kazanca dönüşür.

### Kumar Oyunlarında Kasa Avantajı Tablosu
| Oyun | Kasa Avantajı (House Edge) |
|:---|:---|
| **Blackjack (Kusursuz Strateji)** | ~%0.5 |
| **Bakarat** | ~%1.0 |
| **Avrupa Ruleti (Tek Sıfır)** | %2.7 |
| **Amerikan Ruleti (Çift Sıfır)** | %5.3 |
| **Slot Makineleri** | %4.0 - %10.0 |
| **Keno** | > %25.0 |

---

## 3. Oyuncunun 3 Ölümcül Hatası

1. **Avantajı Olmadan Oynamak:** Sadece yön tahmin ederek veya içgüdüyle işleme girmek. Eksi beklenen değerli hiçbir sistem uzun vadede artıya geçemez.
2. **Kumarbaz Yanılgısı (Gambler's Fallacy):** "5 kere kırmızı geldi, artık siyah gelmeli" düşüncesi. Rulet çarkının hafızası yoktur. Bir enstrüman 5 gündür düşüyor diye yükselmek zorunda değildir; piyasa kimseye borçlu değildir.
3. **Martingale & Kaybettikçe Bahsi Büyütmek:**
   * 10$ kazanmak için kaybettikçe bahsi ikiye katlamak (10 -> 20 -> 40 -> 80 -> 160 -> 320 -> 640$).
   * 7 tur üst üste kaybetme olasılığı 200 turluk bir sekansta **yaklaşık %60**'tır!
   * 1,270$ kaybedip 1,280$'lık bahis açmaya kalktığınızda masa limitine çarpar ve sıfırlanırsınız.

---

## 4. Trader Nasıl Kasa Olur?

### Pozitif Matematiksel Beklenti ($E$)
100 işlem açan bir trader'ın kazanma oranı sadece %45 olsun (yarıdan fazlası kayıp):
* Risk/Ödül Oranı: 1R Risk, 2R Kazanç.
* 45 kazanç $	imes$ 2R = +90R
* 55 kayıp $	imes$ 1R = -55R
* **Net Sonuç:** $+35R$ Kâr!

$$\mathbb{E} = (P_w 	imes R_w) - (P_l 	imes R_l) = (0.45 	imes 2) - (0.55 	imes 1) = 0.90 - 0.55 = +0.35R$$

Her işlem başına beklenen ortalama değer $+0.35R$'dır.

### Varyans & Kayıp Serisi Gerçeği
Aynı %45 kazanma oranına sahip bir sistemde, 100 işlem içinde **en az bir kez üst üste 6 kayıp görme ihtimali %73**'tür. Kasa gibi düşünen bir trader, bu 6 kaybın sistemin doğal bir parçası olduğunu bilir ve stratejisini çöpe atmaz.

---

## 5. Mark Douglas: Güvenli Trade Sanatı (Trading in the Zone)
Profesyonel trader aynı anda iki gerçeğe inanır:
1. **Tek bir işlem için sonuç tamamen belirsizdir ve bilinemez.**
2. **Büyük bir işlem serisi için sonuç neredeyse bellidir çünkü kurallar avantajın tarafındadır.**

### 5 Temel Gerçek:
1. Her şey olabilir.
2. Para kazanmak için bir sonraki anda ne olacağını bilmeniz gerekmez.
3. Bir avantaj (edge), bir olayın diğerinden daha olası olduğunu belirten istatistiksel bir üstünlüktür.
4. Piyasadaki her an benzersizdir.
5. Kazanç ve kayıpların dağılımı rastgeledir.

### 20 İşlem Alıştırması:
Kuralları net bir kurulum seçin. Önümüzdeki 20 sinyali hiçbir kuralı esnetmeden, hiçbirini atlamadan uygulayın. Tekil işlemlerin sonucuna değil, sadece 20 işlemin toplu neticesine bakın.

---

## 6. Tetik Entegrasyon Notları
* **`tetik/config/setups.toml`:**
  * Her yeni setup için canlıya geçiş şartı: `min_shadow_trades = 20`.
  * `require_lower_bound_above_zero = true`: 20 işlemlik Wilson score confidence aralığının alt sınırı pozitif expectancy üretmelidir.
* **Katı Sabit Risk Modeli:** Kesinlikle Martingale veya grid tarzı zarar büyüdükçe pozisyon artırma yasaklanmıştır.
