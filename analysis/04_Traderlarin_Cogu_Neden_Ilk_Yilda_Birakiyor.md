# 04 - Trader'ların Çoğu Neden İlk Yılda Bırakıyor? (Ve Kalanlar Ne Yapıyor?)

## 1. Akademik Araştırmalar & Hayatta Kalma Oranları
* **Tayvan 15 Yıllık Day Trading Araştırması:** Day trade'e başlayan katılımcıların %50'den fazlası ilk yıl içinde pes etmektedir. 3 yılın sonunda masada kalanların oranı yalnızca **%15**'tir.
* **Brezilya Vadeli İşlemler Araştırması (2013-2015):** 300 günden uzun süre day trading yapan bireysel trader'ların **%97'si net zarar** ile elenmiştir.

---

## 2. Trader'ları İlk Yılda Eleyen 4 Temel Neden

### 1. Kendine Yeterince Zaman Tanımamak
* 1 yıl tıp okuyarak cerrah, 1 yıl hukuk okuyarak avukat olunamaz. Trading de onlarca yıl süren bir zanaattır.
* **Peter Brandt:** *"Nasıl trade etmeniz gerektiğine dair bir fikir edinmek için en az 3 yıl, yetkinliğe ulaşmak için en az 5 yıl gerekir."*
* **Marty Schwartz & Mark Minervini:** Borsa sihirbazı olmadan önce 5 ila 10 yıl boyunca para kaybetmiş, hesaplarını defalarca sıfırlamışlardır.

### 2. Yaklaşımdaki İstikrarsızlık (Stratejiden Stratejiye Atlamak)
* Birkaç kayıptan sonra veya piyasa rejimine uymadığı için hemen yeni bir stratejiye geçmek (Parlak Nesne Sendromu).
* Her stratejinin çalışmadığı piyasa koşulları vardır. Trend stratejisi yatay piyasada doğranır; yatay piyasa stratejisi trendde ezilir.
* Kural: Stratejinizin zamanı gelene kadar sabırla bekleyin; başka stillerin kârına özenip tarzınızı değiştirmeyin.

### 3. Ölümcül Kaldıraç (Lethal Leverage)
Aracı kurumların sunduğu 50:1, 100:1 veya 500:1 kaldıraçlar doğrudan sermaye imha aracıdır:

$$	ext{Hesap Sıfırlanma Mesafesi} = rac{100\%}{	ext{Kaldıraç Oranı}}$$

| Kaldıraç Oranı | Hesabı Sıfırlayan Ters Hareket | Piyasa Gerçekliği |
|:---|:---|:---|
| **10:1** | %10.0 | Ortalama hissenin birkaç haftalık hareketi |
| **50:1** | %2.0 | Apple hissesinin sıradan bir günlük hareketi |
| **100:1** | %1.0 | Bitcoin'in 15 dakikalık standart fitili |
| **500:1** | **%0.20** | Enstrümanın gürültü / spread dalgalanması |

Sırf broker kaldıraç veriyor diye onu kullanmak zorunda değilsiniz.

### 4. Tek Bir Büyük Zarar & Ortalama Maliyet Düşürme Günahı
* Kâr eden işlemi azıcık kâr görünce korkudan hemen kapatıp, zarar eden işlemi "birazdan döner" diyerek günlerce taşımak.
* **Ölümcül Günah:** Zarar eden pozisyona ekleme yapmak (Maliyet düşürme).
  *"20 dolardan beğendiğim hisse 14 dolara düştüyse daha ucuza alırım"* düşüncesi, trader'ı istemeden "mecburi uzun vadeli yatırımcı" yapar.

---

## 3. Kalan %3 Ne Yapıyor?
1. Kendilerine 3-5 yıllık çıraklık süresi tanırlar.
2. Tek bir stratejiyi yüzlerce işlem boyunca test eder ve ustalaşırlar.
3. Kaldıraçtan uzak durur, hesap riskini %1 ile sınırlar.
4. Stop seviyesini işleme girmeden önce belirler ve asla pazarlık yapmazlar.

---

## 4. Tetik Botu Risk Entegrasyonu
* **`tetik/config/risk_policy.seed.toml`:**
  * Binance BTCUSDT perpetual için maksimum efektif kaldıraç tavanı (`max_effective_leverage = 3.0`).
  * `allow_averaging_down = false`: Zarardaki pozisyona ekleme kesinlikle engellenmiştir.
