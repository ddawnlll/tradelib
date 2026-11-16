#!/usr/bin/env python3
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ANALYSIS_DIR = BASE_DIR / "analysis"
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

analyses = [
    {
        "file": "01_Profesyonel_Trader_Olmak_Icin_Gercekte_Ne_Gerekir.md",
        "title": "Profesyonel Trader Olmak İçin Gerçekte Ne Gerekir?",
        "vid": "Pbh_XGFYQ4E",
        "duration": "708s (11:48)",
        "url": "https://www.youtube.com/watch?v=Pbh_XGFYQ4E",
        "summary": "Bireysel (evden) trade edenler ile profesyonel kurumsal prop ofisleri arasındaki 10 temel fark. Prop firmaların aradığı 10 karakter özelliği ve bir ofisin asla öğretemeyeceği tek kritik nitelik.",
        "content": """# 01 - Profesyonel Trader Olmak İçin Gerçekte Ne Gerekir?

## 1. Yönetici Özeti & Çekirdek Teori
Evden tek başına trade eden bir bireysel yatırımcı, neyi yanlış yaptığını anlayana kadar ortalama 2 yılını ve on binlerce dolarını kaybedebilir. Bireysel trader'lar genellikle sürekli "haklı çıkmak" zorunda olduklarını zannederken, kurumsal prop ofisleri haklı çıkmaya çalışanları değil, **"profesyonel bir kaybeden"** olmayı öğrenmiş trader'ları bünyesine katar.

Bir prop trading ofisi 10 temel özelliğin 9'unu adaya öğretebilir. Ancak 10. özellik olan **öğrenmeye açıklık ve koçluk alabilme kabiliyeti** dışarıdan verilemez.

---

## 2. Prop Desk'in Aradığı 10 Altın Nitelik

| No | Nitelik | Kurumsal (Prop Desk) Yaklaşımı | Bireysel (Retail) Hata Kalıbı |
|:---|:---|:---|:---|
| **01** | **Profesyonel Kaybeden Olmak** | Zararı önceden belirlenmiş stop seviyesinde keser, günü inceler ve ertesi gün nötr döner. | Zararı kabul etmez, stopu kaydırır, maliyet düşürür veya intikam işlemi açar. |
| **02** | **Süreç Disiplini** | Henüz kâr yokken bile rutini uygular: Günlük tutar, günün en iyi grafiğini arşivler, sabah toplantısına hazırlanır. | Sadece kâr ettiğinde motive olur, rutin tutmaz, plansız ekrana oturur. |
| **03** | **Biyolojik & Fiziksel Disiplin** | Uyku, spor ve beslenmeyi birer trade aracı görür. Kötü uyuduğu gün işlem büyüklüğünü yarıya indirir. | Uykusuz, yorgun ve stresliyken ekran başına oturup büyük riskler alır. |
| **04** | **Kimsenin Ödemediği Bedeli Ödemek** | İlk gelen, son çıkan olur. Kendi ekran kayıtlarını akşam tekrar izler, hatalarını analiz eder. | Günde 15 dakika ekrana bakıp zengin olma hayali kurar. |
| **05** | **Kasa Zihniyeti (Edge & R)** | %40 win rate ile 1R risk / 4R kazanç matematiğine odaklanır. "Bugün planıma uydum mu?" sorusunu sorar. | "Bugün para kazandım mı?" sorusuna odaklanır, kârı şansla açıklar. |
| **06** | **Duygusal Denge** | En iyi gününde aşırı coşmaz, en kötü gününde çökmez. Zirve ve dip yanılsamalarını eler. | Kazandığında kendini dahi zanneder (öfori), kaybettiğinde depresyona girer. |
| **07** | **Sabır & Süreç Odaklılık** | Parayı hedef değil, disiplinli sürecin doğal bir yan ürünü olarak görür. Yıllarca yoğrulmayı göze alır. | Kirayı ve faturaları trading ile ödemeye çalışarak sistemi baskı altına sokar. |
| **08** | **Kendi Paternlerini Analiz Etme** | Ay sonunda işlemleri strateji bazında (haber, kırılım, trend dönüşü) ayıklar. Zayıf stratejiyi eler. | Nerede kazanıp nerede kaybettiğini bilmeden rastgele işlem açmaya devam eder. |
| **09** | **Senaryo Hazırlığı** | Piyasa açılmadan önce en fazla 3 senaryo belirler. Listede olmayan hiçbir harekete atlamaz. | Açılışta ekranda ne hareket ederse onun peşine takılır (FOMO). |
| **10** | **Öğrenmeye Açıklık (Sünger Modeli)** | Kıdemli trader'ları ve mentörleri dinler, proaktif soru sorar, egoyu sıfırlar. | Her şeyi bildiğini iddia eder, tavsiye kabul etmez, sihirli indikatör arar. |

---

## 3. Matematiksel & Operasyonel Kurallar
1. **Günün Sorusu:** Değerlendirme metriği PnL tutarı değil, `Plan Uyum Skoru (0-100)` olmalıdır. Planına sadık kalıp zarar eden bir işlem başarılı kabul edilir.
2. **Kötü Gece Kuralı:** Eğer trader uyku düzenini bozduysa veya mental yorgunluk yaşıyorsa:
   $$\text{Max Risk} = \text{Normal Risk} \times 0.50$$
3. **Maksimum 3 Fikir Kuralı:** Seans açılışından önce en fazla 3 adet doğrulanmış kurulum belirlenir. Bu 3 enstrüman haricinde gün içinde gelişen hiçbir fırsata girilmez.

---

## 4. Tetik Botu Mimari Entegrasyonu
* **`tetik/config/risk_policy.seed.toml`:**
  * Günlük maksimum aktif kurulum sayısı 3 ile sınırlandırılmalıdır (`max_active_setups = 3`).
  * API latency veya execution slippage anomalilerinde otomatik risk yarıya düşürme kuralı.
* **`tetik/crates/agent/src/realized.rs`:**
  * Gün sonu raporunda sadece gerçekleşen PnL değil, setup uyum oranı ve kural ihlali bayrakları (`violation_count`) metrikleştirilmelidir.
"""
    },
    {
        "file": "02_Kasa_Her_Zaman_Kazanir_Trader_Kasa_Olabilir_mi.md",
        "title": "Kasa Her Zaman Kazanır. Trader Kasa Olabilir mi?",
        "vid": "J-6bHLN-D70",
        "duration": "771s (12:51)",
        "url": "https://www.youtube.com/watch?v=J-6bHLN-D70",
        "summary": "100 işlemin 55'ini kaybedip kumarhane gibi kazanmanın arkasındaki olasılık matematiği. Ruletin yeşil sıfırı, büyük sayılar kanunu, Martingale tuzağı ve Mark Douglas'ın 20 işlem alıştırması.",
        "content": """# 02 - Kasa Her Zaman Kazanır. Trader Kasa Olabilir mi?

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
  $$P(\text{Kırmızı}) = \frac{18}{37} \approx 48.65\%$$
* Kasa yeşil sıfır sayesinde tek bir haneden ibaret avantaj elde eder:
  $$\text{House Edge} = \frac{1}{37} \approx 2.70\%$$
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
* 45 kazanç $\times$ 2R = +90R
* 55 kayıp $\times$ 1R = -55R
* **Net Sonuç:** $+35R$ Kâr!

$$\mathbb{E} = (P_w \times R_w) - (P_l \times R_l) = (0.45 \times 2) - (0.55 \times 1) = 0.90 - 0.55 = +0.35R$$

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
"""
    },
    {
        "file": "03_Yanlis_Mentorla_Yillari_Kaybetmek_5_Filtre.md",
        "title": "Trader'ların Çoğu Yıllarını Yanlış Mentorla Kaybediyor (5 Filtre)",
        "vid": "K7TldQMEMEw",
        "duration": "332s (05:32)",
        "url": "https://www.youtube.com/watch?v=K7TldQMEMEw",
        "summary": "Sosyal medyadaki pazarlamacılar ile gerçek prop desk mentörleri arasındaki farklar. Bir mentör veya eğitim kaynağını test etmek için 5 kurumsal filtre.",
        "content": """# 03 - Trader'ların Çoğu Yıllarını Yanlış Mentorla Kaybediyor (5 Filtre)

## 1. Yönetici Özeti
Finansal piyasalarda başarısız olan trader'ların en büyük ortak noktalarından biri, yıllarını yanlış insanlardan öğrenerek harcamalarıdır. İnternet pazarlama ustaları ve içerik üreticileriyle doludur; ancak bir başkasının tutarlı kâr etmesini sağlama yeteneğine sahip olanlar çok nadirdir.

---

## 2. Mentörlük İçin 5 Kurumsal Filtre

```mermaid
flowchart TD
    F1["1. Riske Takıntılı Olmak\n(Pozisyon büyüklüğü, günlük max zarar, sermaye koruma)"] --> F2["2. Hedeflenen Seviyeyi Bizzat Yaşamış Olmak\n(Büyük ölçekli kurumsal sermaye yönetimi)"]
    F2 --> F3["3. Tatsız Dönemler Konusunda Dürüstlük\n(Kayıp serileri, tilt anları ve can sıkıntısı yönetimi)"]
    F3 --> F4["4. Sürece ve Plana Odaklanma\n(PnL yerine kural uyumu ve risk disiplini)"]
    F4 --> F5["5. Gerçek Zamanlı Erişilebilirlik\n(Hata sıcakken ve tilt başlarken anında müdahale)"]
```

### Filtre 1: Riske Takıntılı Olmak
* Sahte mentör vaktinin %90'ını giriş noktaları, gizli indikatörler ve kusursuz kurulumlarla harcar.
* Gerçek mentör riske takıntılıdır: İşlem başına maksimum zarar, günlük limit, portföy ısısı ve oyun içinde kalma süresi üzerine odaklanır.

### Filtre 2: Ulaşmak İstediğiniz Yerde Olması
* Hedefiniz uzun vadeli tutarlılık ise, sadece şanslı bir ralli geçirmiş biri mentör olamaz.
* Hedefiniz kurumsal hacim yönetmek ise, 500$'lık hesapla ekran görüntüsü atan biri rehber olamaz.

### Filtre 3: Tatsız Dönemler Konusunda Şeffaflık
* Her ayının yeşil geçtiğini iddia eden biri yalan söylüyordur.
* Gerçek mentör; çekilme (drawdown) dönemlerinden, can sıkıntısından açılan gereksiz işlemlerden ve haftalarca hiçbir şey yapmadan oturmanın zorluğundan bahseder.

### Filtre 4: Sonuç Değil Süreç Odaklılık
* Zayıf rehber kârlı bir günün ardından coşar, zararlı bir günde hayal kırıklığına uğrar.
* Yetkin mentör trader'ın **nasıl** işlem yaptığına bakar: Plana uyuldu mu? Riske saygı gösterildi mi? Zorla işlem arandı mı?

### Filtre 5: Gerçek Zamanlı Hesap Verebilirlik
* Video kursları veya pasif Discord kanalları tilte giren trader'ı durduramaz.
* Gerçek prop desk ortamında yanınızda oturan kıdemli trader, yüz ifadenizden veya artan işlem sıklığınızdan tilte girdiğinizi fark edip masadan kaldırır.

---

## 3. Tetik Botu İçin Mimari Yansıma
Tetik sisteminde mentörlük rolü otonom ajan rollerine devredilmiştir:
* **`tetik/prompts/analysts/skeptic.md`:** Her trade tezini sorgulayan şüpheci kıdemli analist rolü.
* **`tetik/prompts/reviewer.md`:** Gün sonu seans planını ve gerçekleşen işlemleri denetleyen risk amiri rolü.
"""
    },
    {
        "file": "04_Traderlarin_Cogu_Neden_Ilk_Yilda_Birakiyor.md",
        "title": "Trader'ların Çoğu Neden İlk Yılda Bırakıyor? (Ve Kalanlar Ne Yapıyor?)",
        "vid": "WIyUKrAyE_c",
        "duration": "612s (10:12)",
        "url": "https://www.youtube.com/watch?v=WIyUKrAyE_c",
        "summary": "Tayvan ve Brezilya üniversite araştırmaları ışığında day trader'ların %97'sinin batma sebepleri. 4 ölümcül hata: Zaman tanımamak, strateji atlamak, ölümcül kaldıraç ve ortalama maliyet günahı.",
        "content": """# 04 - Trader'ların Çoğu Neden İlk Yılda Bırakıyor? (Ve Kalanlar Ne Yapıyor?)

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

$$\text{Hesap Sıfırlanma Mesafesi} = \frac{100\%}{\text{Kaldıraç Oranı}}$$

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
"""
    },
    {
        "file": "05_Trader_Olmak_Ne_Kadar_Surer_Durust_Cevap.md",
        "title": "Trader Olmak Ne Kadar Sürer? 3 Ay mı, 3 Yıl mı? (Dürüst Cevap)",
        "vid": "NDENGqeOPog",
        "duration": "533s (08:53)",
        "url": "https://www.youtube.com/watch?v=NDENGqeOPog",
        "summary": "Trader olmanın süresi bir takvim süresi değil, birikim meselesidir. 2 yıllık hava yastığı kuralı, 5.000$'lık hesabın kira ödeyemeyeceği gerçeği ve sermaye baskısının yok edilmesi.",
        "content": """# 05 - Trader Olmak Ne Kadar Sürer? 3 Ay mı, 3 Yıl mı? (Dürüst Cevap)

## 1. Çekirdek Formül: 2 Yıllık Hava Yastığı Kuralı
Trader olmanın süresi 3 ay veya 3 yıl değildir. Doğru cevap şudur:
> **Önümüzdeki 2 yıl boyunca tüm yaşam masraflarınızı karşılayacak kadar nakit hava yastığınız (ihtiyaç akçeniz) olduğunda tam zamanlı trading'i düşünebilirsiniz.**

O zamana kadar mevcut işinizi bırakmamalısınız.

$$\text{Hava Yastığı (Runway)} = \text{Aylık Asgari Yaşam Maliyeti} \times 24 \text{ Ay}$$

* Örnek: Aylık gider 2,000$ ise, kenarda dokunulmayacak 48,000$ nakit bulunmalıdır.
* Bu para trading sermayesi değildir; trading'in kirayı ödeme baskısını ortadan kaldıran psikolojik kalkandır.

---

## 2. 5,000 Dolarlık Hesap Neden Kira Ödeyemez?
Birçok acemi 5,000$ sermaye ile işini bırakıp evden geçinmeye çalışır:
* Aylık masraf: 2,000$
* Gereken getiri: $\frac{2,000}{5,000} = \%40 \text{ / Ay}$
* Dünyanın en iyi fonları yılda %30-%50 yaparken, her ay %40 kazanmak zorunda olmak trader'ı 20x-50x kaldıraç almaya, stop koymamaya ve 2 hafta içinde hesabı patlatmaya zorlar.

---

## 3. İlk Kârlar Nereye Harcanmalıdır?
Trading'den elde edilen ilk kârlar lüks tüketime (yeni telefon, pahalı araba, lüks saat) harcanmamalıdır.
* Başlangıçta asıl savaş **siz ve zaman** arasındadır.
* Kazanılan her dolar, kendinize **daha fazla zaman (runway)** satın almak için kullanılmalıdır. Sakin ve telaşsız işlem yapabilme özgürlüğü en büyük avantajdır.

---

## 4. Tetik Botu Sermaye & Risk Kuralı
* Botun risk modeli, kâr çekme hedeflerinden bağımsız olarak net anapara (`unencumbered_equity`) üzerinden çalışır.
* Kasa büyüklüğüne göre risk çarpanı dinamik olarak belirlenir; sermaye azaldıkça bot riskini agresifleştiremez.
"""
    },
    {
        "file": "06_Hala_Para_Kazanamamana_Sebep_Olan_5_Trading_Hatasi.md",
        "title": "Hâlâ Para Kazanamamana Sebep Olan 5 Trading Hatası",
        "vid": "Go19JcFyUDM",
        "duration": "638s (10:38)",
        "url": "https://www.youtube.com/watch?v=Go19JcFyUDM",
        "summary": "Trader'ların %95'ini başarısız kılan 5 davranış kalıbı: Hızlı zenginlik arayışı, plansızlık, eğitime zaman ayırmamak, sihirli indikatör avı ve Ed Seykota disiplin kuralı.",
        "content": """# 06 - Hâlâ Para Kazanamamana Sebep Olan 5 Trading Hatası

## 1. Hata 1: Hızlı Zengin Olma İllüzyonu
* Çoğu kişi %100 prim yapacak tek bir hisseyi bulma hayaliyle tüm sermayesini riske atar.
* Bir hissenin yılda %100 yapma olasılığı düşüktür; ancak neredeyse her kaliteli hisse yıl içinde %20'lik dalgalar üretir.
* Sürdürülebilir model: %100 yapacak tek bir piyango aramak yerine, **%20 prim yapacak 5 adet yüksek olasılıklı dalgayı** pozitif beklenen değerle yakalamaktır.
* Hisselerin yıllık ortalama volatilitesi yaklaşık %38'dir ($100'lık hisse $62-$138 bandında salınır).

## 2. Hata 2: Yazılı Bir Planın Olmaması ("Stopun Nerede?")
* Prop ofisinde bir trader yeni bir fikir sunduğunda sorulan ilk soru: **"Stopun nerede?"**
* Her işleme potansiyel olarak haksız çıkacağımızı varsayarak başlarız.
* Stop seviyesi bilinmeden pozisyon boyutu (lot) matematiksel olarak hesaplanamaz.

## 3. Hata 3: Tarih ve Kitap Okumamak
* YouTube videoları ve podcast'ler bir yere kadar götürür; ancak piyasa tarihini ve insan doğasını anlamak için kitap şarttır.
* 1920'de Jesse Livermore'un yaptığı hatalar bugün algoritmaların hükmettiği piyasalarda da aynen tekrarlanmaktadır çünkü açgözlülük ve korku değişmemiştir.

## 4. Hata 4: Kutsal Kâse İndikatör Arayışı
* İndikatör bir işletmenin sadece tek bir parçasıdır (ürün tasarımı gibidir).
* Dağıtım, risk kontrolü, sermaye yönetimi ve psikoloji olmadan dünyanın en iyi indikatörü dahi para kazandıramaz.

## 5. Hata 5: Disiplin Eksikliği & Ellerinin Üzerinde Oturamamak
* **Ed Seykota Kanunu:** *"Herkes piyasadan tam olarak istediği şeyi alır. Macera, dopamin ve heyecan istiyorsan piyasa sana bunları memnuniyetle verir. Ama para istiyorsan disipline ihtiyacın var."*
* Piyasa kötüyken hiçbir şey yapmadan sadece izleyebilmek (ellerinin üzerinde oturmak) profesyonellerin en büyük erdemidir.

---

## 6. Tetik Entegrasyonu
* **`tetik/crates/desk/src/level_check.rs`:** Fırsat filtrelerinde "gri" alanlara yer verilmez. 5 şartın tamamı sağlanmadığında bot "idle" modda bekler ve zorlama işlem açmaz.
"""
    },
    {
        "file": "07_Evden_Trade_Neden_Pahaliya_Patlar_Ofisin_5_Avantaji.md",
        "title": "Evden Trade Yapmak Neden Pahalıya Patlar? Trading Ofisinin 5 Avantajı",
        "vid": "8dq2UEboEfY",
        "duration": "329s (05:29)",
        "url": "https://www.youtube.com/watch?v=8dq2UEboEfY",
        "summary": "Evde tek başına kalmanın yalnızlığına karşı prop desk ortamının 5 kurumsal avantajı: Şirket sermayesi, çevre kalibrasyonu, yapılandırılmış mentörlük, ortam disiplini ve kolektif zeka.",
        "content": """# 07 - Evden Trade Yapmak Neden Pahalıya Patlar? Trading Ofisinin 5 Avantajı

## 1. Karşılaştırma: Ev (Retail) vs Prop Ofisi (Institutional)

| Kriter | Evden Trade (Bireysel) | Prop Ofisi (Kurumsal) |
|:---|:---|:---|
| **Sermaye Riski** | Kendi birikimi; kayıplar kişisel iflasa yol açabilir. | Şirket sermayesi; zarar sınırında masadan kalkar, borç kalmaz. |
| **Psikolojik Baskı** | Yüksek; fatura ve geçim korkusu kararları bozar. | Düşük; risk yöneticisi denetiminde objektif icraat. |
| **Geri Bildirim** | Yalnızlık ve sosyal medya gürültüsü. | Kıdemli mentörlerin anlık denetimi ve rehberliği. |
| **Disiplin Çerçevesi** | Yatak, mutfak, dikkat dağıtıcı unsurlar. | Profesyonel ortam, hesap verebilirlik ve şeffaf ekranlar. |
| **Piyasa Kapsamı** | 1 çift göz; sınırlı fırsat takibi. | 10+ çift gözün paylaştığı gerçek zamanlı kolektif zeka. |

---

## 2. Kolektif Zeka Mekanizması
* Bir trader fırsatı görür, diğeri makro bağlamı ekler, üçüncüsü riske ve tuzaklara dikkat çeker.
* Bu sinerji, tek bir kişinin gözünden kaçabilecek kör noktaları tamamen ortadan kaldırır.

---

## 3. Tetik Çoklu Ajan Deski (Multi-Agent Desk) Mimarisi
Tetik botu, bir prop trading ofisinin kolektif zeka yapısını simüle etmek üzere tasarlanmıştır:
* `Flow Analyst`: Likidite ve hacim akışını takip eder.
* `Structure Analyst`: HTF piyasa yapısını ve rejimini çıkarır.
* `Skeptic Analyst`: Kuruluma karşı argüman üretir ve tuzakları arar.
* `Risk Manager`: Sermaye kurallarını ve drawdown sınırlarını denetler.
* `Execution Trader`: Nihai kararla tetiği çeker.
"""
    },
    {
        "file": "08_Hangi_Trading_Stratejisi_Sana_Gore.md",
        "title": "Hangi Trading Stratejisi Sana Göre? (4 Temel Zaman Dilimi)",
        "vid": "_JX74IZoEvA",
        "duration": "291s (04:51)",
        "url": "https://www.youtube.com/watch?v=_JX74IZoEvA",
        "summary": "Zamana dayalı 4 trading stili: Scalping, Day Trading, Swing Trading ve Position Trading. Grafik dilimleri, gecelik riskler, kaldıraç toleransları ve doğru tarzı seçme rehberi.",
        "content": """# 08 - Hangi Trading Stratejisi Sana Göre?

## 1. 4 Zaman Bazlı Stratejinin Karşılaştırması

```mermaid
quadrantChart
    title Trading Stratejileri Matrisi
    x-axis Düşük Karar Frekansı --> Yüksek Karar Frekansı
    y-axis Düşük Gecelik Risk --> Yüksek Gecelik Risk
    quadrant-1 "Position Trading"
    quadrant-2 "Swing Trading"
    quadrant-3 "Day Trading"
    quadrant-4 "Scalping"
```

| Strateji | Zaman Dilimi | Tutma Süresi | Gecelik Risk | Karar Frekansı | Uygun Profil |
|:---|:---|:---|:---|:---|:---|
| **Scalping** | 1m - 5m | Saniyeler - Dakikalar | **YOK** (Gün sonu flat) | Çok Yüksek | Yüksek refleks, tam gün ekran başında olanlar |
| **Day Trading** | 5m - 15m | Dakikalar - Saatler | **YOK** (Gün sonu flat) | Yüksek | Gün içi dalgaları kovalayan aktif trader'lar |
| **Swing Trading** | 1D - 1W (H4) | Günler - Haftalar | **VAR** (Gap riski) | Düşük | Çalışanlar, derin analiz yapıp alarm kuranlar |
| **Position Trading**| 1W - 1M | Haftalar - Aylar | **VAR** (Makro risk) | Çok Düşük | Trend takipçileri ("Cut losers, let winners run") |

---

## 2. Temel Prensip: "Zararları Kes, Kârları Büyüt"
Tüm stillerde geçerli evrensel Wall Street ilkesi:
$$\text{Cut your losers short, and let your winners run.}$$

---

## 3. Tetik Entegrasyonu
Tetik BTCUSDT botumuz bir **Hibrit Day/Swing** modelidir:
* Bias & Rejim Analizi: 4H ve 1D (Swing temeli).
* Setup & Tetik Seviyesi: 15m ve 1h (Day trade icrası).
* Gece riski yönetimi: Stop emirleri Binance üzerinde borsa tarafında (exchange-native) donanımlı tutulur.
"""
    },
    {
        "file": "09_Profesyonel_Traderlar_Kanamayi_Bu_Sekilde_Durdurur.md",
        "title": "Profesyonel Traderlar Kanamayı Bu Şekilde Durdurur",
        "vid": "ItTG09VLeNQ",
        "duration": "326s (05:26)",
        "url": "https://www.youtube.com/watch?v=ItTG09VLeNQ",
        "summary": "Kayıp serilerinde kanamayı durdurma protokolü. Kademeli pozisyon küçültme basamakları, ekranı kapatıp dinlenme, ellerin üzerinde oturma gücü ve form tutana kadar sahaya küçük dönme disiplini.",
        "content": """# 09 - Profesyonel Traderlar Kanamayı Bu Şekilde Durdurur

## 1. Çekirdek İlke: Kanamayı Durdurmak (De-risking Protocol)
Kayıp serileri her trader'ın başına gelir. İnternetteki stratejilerin %99'u işleme giriş üzerine odaklanırken, profesyonelleri hayatta tutan şey **zarar döneminde pozisyon boyutunu nasıl yönetecekleridir**.

> **"Çukura düştüğünüzde yapacağınız ilk şey, elinizdeki kazmayı bırakmaktır."**

---

## 2. Kademeli Pozisyon Küçültme Basamakları (Step-Down Matrix)

İşler kötü gittiğinde pozisyon büyüklüğü asla ikiye katlanmaz; aksine kademeli olarak küçültülür:

```mermaid
flowchart TD
    A["Normal Pozisyon: 1,000 Hisse / 1.0R"] -->|Üst üste 2 kayıp| B["1. Basamak: 500 Hisse / 0.5R"]
    B -->|Kayıp devam ederse| C["2. Basamak: 300 Hisse / 0.3R"]
    C -->|Kayıp devam ederse| D["3. Basamak: 100 Hisse / 0.1R"]
    D -->|Zirve Zarar Sınırı| E["TAMAMLAYICI FREN: Ekranı Kapat & 2-5 Gün Dinlen"]
```

* Bu sayede trader en kötü formda olduğu dönemde piyasaya **en küçük riskle** maruz kalır.
* Sermaye tükenmezse oyun bitmez.

---

## 3. Nakitte Beklemenin Gücü (The Superpower of Doing Nothing)
* Emeklilik fonları ve kurumsal fonlar portföylerinin %90-%95'ini sürekli yatırımlı tutmak zorundadır.
* Bireysel ve bağımsız trader'ın en büyük lüksü **%100 nakitte bekleyebilme özgürlüğüdür**.
* Piyasa toksik veya volatil olduğunda hiçbir şey yapmamak aktif ve kazançlı bir pozisyondur.

---

## 4. Geri Dönüş Protokolü (Step-Up Protocol)
* Form tutana kadar risk artırılmaz.
* Arka arkaya pozitif ve kurallara uygun işlemler geldikçe pozisyon büyüklüğü kademeli olarak (100 -> 300 -> 500 -> 1000) eski haline getirilir.

---

## 5. Tetik Botu Mimari Kuralı
* **`tetik/crates/agent/src/halt.rs`:**
  * Üst üste 3 stop işleminden sonra: `risk_multiplier` otomatik olarak `0.5`'e çekilir.
  * Üst üste 5 stop işleminden sonra: Bot 48 saat boyunca kendini `HALT` durumuna alır (`cooldown_hours = 48`).
"""
    },
    {
        "file": "10_Dogru_Trading_Mentoru_Nasil_Secilir.md",
        "title": "Doğru Trading Mentoru Nasıl Seçilir?",
        "vid": "d63KKdbeygs",
        "duration": "289s (04:49)",
        "url": "https://www.youtube.com/watch?v=d63KKdbeygs",
        "summary": "Gerçek bir mentörün portföyü, risk yaklaşımı ve öğrencisine sağladığı katma değer. Şovmenler ile gerçek fon yöneticilerinin ayrıştırılması.",
        "content": """# 10 - Doğru Trading Mentoru Nasıl Seçilir?

## 1. Temel Kıstaslar
* Bir mentörün değeri ne kadar para kazandığıyla değil, **öğrencisinin sermayesini koruma reflekslerini nasıl inşa ettiğiyle** ölçülür.
* İndikatör satanlar değil, risk modelleri ve olasılık tabloları sunanlar seçilmelidir.
* Ace Trading ekosisteminde mentörlük bir eğitim paketi değil; aynı işlem masasını paylaşarak anlık refleksleri kopyalama sürecidir.
"""
    },
    {
        "file": "11_Traderlarin_Yuzde_95i_Neden_Kaybeder_5_Kritik_Beceri.md",
        "title": "Traderların %95’i Neden Kaybediyor? Sizi Kazanan %5’e Sokacak 5 Beceri",
        "vid": "5h-nMtuRFXk",
        "duration": "337s (05:37)",
        "url": "https://www.youtube.com/watch?v=5h-nMtuRFXk",
        "summary": "Kaybeden %95 ile milyoner trader'lar arasındaki 5 kritik beceri farkı: Duygusal kontrol, pusu sabrı, sermaye koruma riski, zihinsel dayanıklılık ve piyasa adaptasyonu.",
        "content": """# 11 - Traderların %95’i Neden Kaybediyor? 5 Kritik Beceri

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
"""
    },
    {
        "file": "12_Ust_Uste_Stop_Oldugunuzda_Ne_Yapmalisiniz_Kriz_Plani.md",
        "title": "Üst Üste Stop Olduğunuzda Ne Yapmalısınız? (Kriz Planı)",
        "vid": "osNo6QPso9Q",
        "duration": "326s (05:26)",
        "url": "https://www.youtube.com/watch?v=osNo6QPso9Q",
        "summary": "Mike Tyson yumruğu: 5 kez üst üste stop olmanın varyans kesinliği. Kasanın logaritmik erime matematiği, haftalık %5 devre kesici kuralı ve risk yarıya indirme protokolü.",
        "content": """# 12 - Üst Üste Stop Olduğunuzda Ne Yapmalısınız? (Kriz Planı)

## 1. Varyans Gerçeği & Mike Tyson Kuralı
> *"Yüzüne sağlam bir yumruk yiyene kadar herkesin bir planı vardır." — Mike Tyson*

Yazı tura oyununda dağılım rastgeledir; bir yazı bir tura şeklinde gitmez. Büyük veri setlerinde ardışık kayıp serileri kaçınılmaz bir istatistiksel gerçektir.
Kusursuz bir sistemde bile **5 kez üst üste stop olmak kesin bir matematiksel olasılıktır**. Kriz yönetimi tam olarak 5. kaybın yaşandığı gün başlar.

---

## 2. Kasanın Logaritmik Erime Matematiği (Asymmetric Recovery)
Kasa erimesi aritmetik değil, **logaritmiktir**. Kayıp büyüdükçe eski seviyeye dönmek için gereken getiri eksponansiyel olarak artar:

$$\text{Gereken Kâr \%} = \left(\frac{1}{1 - \text{Kayıp Oranı}}\right) - 1$$

| Kasa Kaybı | Başa Dönmek İçin Gereken Kâr | Yorum |
|:---|:---|:---|
| **-%5** | **+%5.26** | Tolere edilebilir, rutin dalgalanma |
| **-%10** | **+%11.1** | Rahat telafi edilir |
| **-%20** | **+%25.0** | Makas açılmaya başlar |
| **-%30** | **+%42.8** | Ciddi risk artışı gerektirir |
| **-%50** | **+%100.0** | Kalan tüm parayı 2'ye katlamak gerekir! |
| **-%75** | **+%300.0** | Pratik olarak hesap iflası |

---

## 3. Kurumsal Kriz Protokolü (Devre Kesiciler)

```mermaid
flowchart TD
    A["Haftalık Kasa Kaybı >= %5.0"] -->|DEVRE KESİCİ TETİKLENDİ| B["O HAFTA TÜM İŞLEMLERİ DURDUR"]
    B --> C["Hafta Sonu İşlem Analizi & Mental Soğuma"]
    C --> D["Bir Sonraki Hafta: Risk Limitini Yarıya İndir (%1.0 -> %0.5)"]
    D --> E["Amaç Kâr Değil, Piyasayla Ritmi Yeniden Yakalamak"]
    E -->|Kasa Toparlanana Kadar| F["0.5R Riskle Devam Et"]
```

### Devre Kesici Kuralları:
1. **Haftalık %5 Kayıp Eşiği:** Hesap haftalık bazda %5 eridiğinde o haftanın tüm işlem yetkisi iptal edilir.
2. **Yarı Risk Kuralı:** Takip eden hafta risk tavanı %1'den **%0.5'e** çekilir.
3. **Zarar Eden Pozisyona Asla Ekleme Yapılmaz.**
4. **Stop Seviyesi Asla Geriye Kaydırılmaz.**

---

## 4. Tetik Botu Konfigürasyonu
* **`tetik/config/risk_policy.seed.toml`:**
```toml
[circuit_breaker]
max_daily_drawdown_pct = 2.0
max_weekly_drawdown_pct = 5.0
halt_on_weekly_breach = true
post_breach_risk_factor = 0.5
```
"""
    },
    {
        "file": "13_Islemlerin_Yarisinda_Yanilip_Yine_de_Para_Kazanmak.md",
        "title": "İşlemlerin Yarısında Yanılıp Yine de Nasıl Para Kazanılır?",
        "vid": "d5R7xP542SA",
        "duration": "297s (04:57)",
        "url": "https://www.youtube.com/watch?v=d5R7xP542SA",
        "summary": "R-multiple pozisyon boyutlandırma matematiği. Dolar bazlı düşünmekten R bazlı düşünmeye geçişin psikolojik gücü ve stop mesafesine göre lot ayarlama formülü.",
        "content": """# 13 - İşlemlerin Yarısında Yanılıp Yine de Nasıl Para Kazanılır?

## 1. Olasılık Oyunu: Hileli Zar Deneyi
* Kazanma Oranı: %45 (İşlemlerin çoğunda yanılıyoruz)
* Risk: 1R
* Kazanç: 2R
* 100 işlemde: 55 kayıp (-55R) + 45 kazanç (+90R) = **+35R Net Kâr**.

---

## 2. R-Multiple Pozisyon Boyutlandırma Formülü

$$\text{İşlem Lot Büyüklüğü} = \frac{\text{Toplam Sermaye} \times \text{Risk Yüzdesi (1R)}}{|\text{Giriş Fiyatı} - \text{Stop Loss Fiyatı}|}$$

### Somut Hesaplama Örneği:
* Toplam Portföy: 100,000$
* İşlem Başına Risk (%1): 1,000$ ($1R$)
* **Senaryo A (Dar Stop):**
  * Giriş = 50$, Stop = 48$ (Fark = 2$)
  * $\text{Lot} = \frac{1,000}{2} = \mathbf{500 \text{ Hisse}}$
* **Senaryo B (Geniş Stop):**
  * Giriş = 50$, Stop = 40$ (Fark = 10$)
  * $\text{Lot} = \frac{1,000}{10} = \mathbf{100 \text{ Hisse}}$

> Stop mesafesi genişledikçe alınan lot küçülür; daraldıkça büyür. Ancak stop vurulduğunda kaybedilen tutar her zaman **kesinlikle 1,000$ (1R)** kalır.

---

## 3. R Dilinin Psikolojik Gücü
* "Bugün 5,000 TL kaybettim" demek hayatta kalma güdüsünü ve geçim stresini tetikler.
* "1R stop oldum" demek mekanik ve istatistiksel sürecin olağan bir maliyetidir.

---

## 4. Tetik Botu Formülü
`tetik` botunun emir motoru (`crates/exec/src/orders.rs`) emir boyutunu asla sabit kontrat adediyle değil, dinamik `risk_budget / stop_distance` formülüyle hesaplar.
"""
    },
    {
        "file": "14_Trading_Kariyerini_Yukseltecek_3_Efsanevi_Kitap.md",
        "title": "Trading Kariyerinizi Bir Üst Seviyeye Taşıyacak 3 Efsanevi Trading Kitabı",
        "vid": "jZZChh99xZw",
        "duration": "297s (04:57)",
        "url": "https://www.youtube.com/watch?v=jZZChh99xZw",
        "summary": "Yüzlerce yıllık tecrübenin damıtıldığı 3 başucu kitabı: Jesse Livermore (İnsan doğası), Mark Douglas (Olasılık zihniyeti) ve Jack Schwager (Borsa sihirbazlarının ortak risk disiplini).",
        "content": """# 14 - Trading Kariyerinizi Bir Üst Seviyeye Taşıyacak 3 Efsanevi Kitap

## 1. Kitap 1: Bir Borsa Spekülatörünün Anıları (Edwin Lefèvre / Jesse Livermore)
* **Ana Fikir:** Fiyatları yönlendiren şey grafikler değil insan doğasıdır (korku, umut, açgözlülük).
* Teknoloji ve enstrümanlar değişir; ancak insan doğası değişmediği için piyasa döngüleri ve manipülasyonlar 100 yıl önce neyse bugün de odur.

## 2. Kitap 2: Güvenli Trade Sanatı / Trading in the Zone (Mark Douglas)
* **Ana Fikir:** Haklı çıkmaya çalışmayı bırakıp olasılıkları yönetmeye geçmek.
* Her işlemin sonucu bir öncekinden bağımsızdır.
* Elit sporcular gibi "akış" (zone) haline geçerek piyasayı kontrol etmeye çalışmak yerine kendi tepkilerini yönetmek.

## 3. Kitap 3: Borsa Sihirbazları Serisi (Jack Schwager)
* **Ana Fikir:** Tek bir kutsal kâse tarzı yoktur. Kimi makrocu, kimi quant, kimi trend takipçisidir.
* Hepsini birleştiren tek ortak payda: **Demir gibi risk yönetimi, öz disiplin ve sermaye koruma tutkusu**.
"""
    },
    {
        "file": "15_Hesabinizi_Sifirlayan_5_Psikolojik_Tuzak.md",
        "title": "Çoğu Trader Neden Kaybeder? Hesabınızı Sıfırlayan 5 Psikolojik Tuzak",
        "vid": "Zfu6xtNVKBk",
        "duration": "296s (04:56)",
        "url": "https://www.youtube.com/watch?v=Zfu6xtNVKBk",
        "summary": "Hesap patlatan 5 zihinsel mekanizma: İntikam işlemleri, aşırı özgüven ve dopamin partisi, analiz felci (Voltaire kuralı), FOMO ve zararı kabullenememek.",
        "content": """# 15 - Çoğu Trader Neden Kaybeder? Hesabınızı Sıfırlayan 5 Psikolojik Tuzak

## 1. 5 Zihinsel Tuzak ve Çözüm Matrisi

| Tuzak | Belirti | Neden Tehlikeli? | Çözüm Protokolü |
|:---|:---|:---|:---|
| **1. İntikam İşlemleri** | Kaybın hemen ardından egoyla daha büyük pozisyon açmak. | Duygular kontrolü ele alır, kurallar devre dışı kalır. | Ekrandan uzaklaşmak, soğuma molası vermek. |
| **2. Aşırı Özgüven** | Peş peşe kazançlardan sonra "Matrix kodunu çözdüm" hissi. | Kurallar esnetilir, "elim sıcak" denilerek risk büyütülür. | "Önceki kârım olmasaydı bu işleme girer miydim?" sorusu. |
| **3. Analiz Felci** | Düzinelerce indikatör arasında tetiği çekememek. | Mükemmel, iyinin düşmanıdır (Voltaire). Fırsatlar kaçar. | Maksimum 2-3 kuraldan oluşan sade ve net kontrol listesi. |
| **4. FOMO** | Uçan fiyatın arkasından plansızca atlamak. | Fiyat pazarlık gücünü kaybettirir, tepe/dip tuzağına iter. | "Plan yoksa işlem de yok. Kaçan işlem maliyetsizdir." |
| **5. Zararı Kabullenmemek**| "Satmadıkça zararda değilim" yanılgısı. | Küçük bir stopla kurtulacakken tüm portföy rehin kalır. | Zararı eğitim bedeli görmek; stopu mekanik icra etmek. |

---

## 2. Tetik Entegrasyonu
* Algoritmik otonom bot olmanın en büyük avantajı: **İntikam, FOMO ve aşırı özgüven hormonlarından tamamen arınmış olmasıdır.**
* Analiz felcini önlemek için her ajanın prompt'unda katı JSON çıktı şeması zorunlu kılınmıştır.
"""
    },
    {
        "file": "16_Ace_Trading_CEO_Anton_Panayatov_Bloomberg_Teardown.md",
        "title": "Ace Trading CEO Anton Panayatov talks to Bloomberg (Teardown)",
        "vid": "x2HZXLmIJow",
        "duration": "1445s (24:05)",
        "url": "https://www.youtube.com/watch?v=x2HZXLmIJow",
        "summary": "Ace Trading CEO'su Anton Panayatov'un Bloomberg röportajının kurumsal analizi: Hedge fund modeli, NYSE/NASDAQ istatistiksel arbitraj, türev ürünler, BDC/REIT/ETF mekaniği ve 70+ karlı trader ekosistemi.",
        "content": """# 16 - Ace Trading CEO Anton Panayatov Bloomberg Röportajı Teardown

## 1. Şirket Profili & Kurumsal Model
* **Şirket:** Ace Trading (Hedge Fund & Proprietary Trading Academy).
* **Kurucu:** Anton Panayatov (Eastern Europe / Sofya kökenli, Londra ve İstanbul genişlemesi).
* **Faaliyet Alanı:** NYSE, NASDAQ ve AMEX'te listelenen hisse senetleri, opsiyonlar, türevler ve ETF'ler üzerinde **İstatistiksel Arbitraj (Statistical Arbitrage)**.
* **İstanbul Tercihi:** Doğu Avrupa ve Batı Yarımküre'nin en büyük metropolü; yıllık 500,000 üniversite mezunuyla devasa analitik yetenek havuzu.

---

## 2. Temel Yatırım Felsefesi: Bilim vs Kumar
* Anton Panayatov finansal piyasaların bir bilim olduğunu, kumar olmadığını vurgular:
  * Regülasyonsuz FX, CFD veya spekülatif kripto ruletlerinden kesinlikle uzak durulur.
  * Odak noktası: Yanlış fiyatlanmış varlıklar (**mispriced assets**), istatistiksel dengesizlikler ve türev arbitrajı.
* 2005'te ABD'de 7,000 halka açık şirket ve 200-300 ETF varken, bugün 3,500 şirket ve 3,500'den fazla ETF/fon vardır. Bu durum inanılmaz bir enstrüman çeşitliliği ve arbitraj fırsatı sunmaktadır (REITs, BDCs, Enerji vb.).

---

## 3. Prop Desk Yetiştirme Modeli
1. **Yetenek Seçimi:** Analitik düşünme kabiliyetine sahip adayların tespiti.
2. **Akademi Eğitimi:** Üniversitelerin dahi öğretmediği türev matematik ve arbitraj eğitimi.
3. **Fon Yönetim Teklifi:** Mezunlara şirket sermayesi tahsis edilerek kâr ortaklığı modeliyle işlem yaptırılması (70'in üzerinde tutarlı kârlı trader).

---

## 4. Tetik Botu İçin Kurumsal Vizyon
* `tetik`'in uzun vadeli vizyonu da tekil indikatör sinyallerinden ziyade, **istatistiksel dengesizlikler (SMC/ICT likidite boşlukları) ve matematiksel risk kalkanı** ile çalışan kurumsal bir arbitraj ve price action makinesi olmaktır.
"""
    },
    {
        "file": "17_Mikro_Kurallar_ve_Shorts_Katalogu.md",
        "title": "Ace Trading Mikro Kurallar & 27 Shorts Kataloğu",
        "vid": "SHORTS_COMPILATION",
        "duration": "27 Shorts Videosu",
        "url": "https://www.youtube.com/@AceTradingTR/shorts",
        "summary": "Ace Trading Shorts serisindeki 27 mikro dersin kurallara göre tasnif edilmiş tam kataloğu ve altın ilkeler.",
        "content": """# 17 - Mikro Kurallar & 27 Shorts Kataloğu

## 1. Risk & Sermaye Kuralları
1. **Çukura Düştüğünde Kazmayı Bırak:** Formda değilsen ekranı kapat; ısrar etmek hesabı bitirir.
2. **500'e 1 Kaldıraç İntihardır:** %0.2'lik ters bir mum hesabı sıfırlar.
3. **Maksimum Risk:** Tek işlemde hesabın %1'inden fazlasını asla riske atma.
4. **2 Yıllık Masraf Kuralı:** İhtiyaç akçen olmadan işini bırakma.
5. **Kira Ödeyemeyen Hesap:** 5,000$'lık hesapla geçinmeye çalışmak kumarı tetikler.

## 2. İcra & Stop Kuralları
6. **Stop Gürültünün Dışına Konur:** Haklıydın ama stop oldun; çünkü stopun piyasa gürültüsünün içindeydi.
7. **Pazarlıksız Stop:** Fiyat stopa geldiğinde çıkılır, tartışma ve umut yoktur.
8. **Maliyet Düşürme Günahı:** 20$'dan düşen hisseye ekleme yapma; analizin çöktüğü yerde çık.
9. **Küçük Kayıp, Büyük Kazanç:** Risk/ödül oranı asimetrik tutulmalıdır.
10. **5 Şartın 4'ü Yetmez:** Tüm kurallar onay vermedikçe işlem açılmaz.

## 3. Psikoloji & Mentalite
11. **Para mı, Heyecan mı:** Dopamin arıyorsan kumarhane orada; para istiyorsan disiplin şart.
12. **FOMO Maliyeti:** Kaçan işlem bedavadır; plansız işlem sermayeyi yer.
13. **İlk Kârları Koru:** İlk kârları lüks tüketime değil, zaman satın almaya harca.
14. **Satmadıkça Zararda Değilsin Yalanı:** Pozisyonun aleyhine gitmesi sermaye kaybıdır; kabullen.
15. **Herkes Gibi Düşünme:** %95'in yaptığını yaparsan %95 gibi kaybedersin.
"""
    }
]

for item in analyses:
    out_file = ANALYSIS_DIR / item["file"]
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(item["content"].strip() + "\n")
    print(f"Generated: {out_file.name}")

print("All 17 analysis files generated successfully!")
