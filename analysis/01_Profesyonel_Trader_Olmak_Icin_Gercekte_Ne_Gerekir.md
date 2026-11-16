# 01 - Profesyonel Trader Olmak İçin Gerçekte Ne Gerekir?

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
   $$	ext{Max Risk} = 	ext{Normal Risk} 	imes 0.50$$
3. **Maksimum 3 Fikir Kuralı:** Seans açılışından önce en fazla 3 adet doğrulanmış kurulum belirlenir. Bu 3 enstrüman haricinde gün içinde gelişen hiçbir fırsata girilmez.

---

## 4. Tetik Botu Mimari Entegrasyonu
* **`tetik/config/risk_policy.seed.toml`:**
  * Günlük maksimum aktif kurulum sayısı 3 ile sınırlandırılmalıdır (`max_active_setups = 3`).
  * API latency veya execution slippage anomalilerinde otomatik risk yarıya düşürme kuralı.
* **`tetik/crates/agent/src/realized.rs`:**
  * Gün sonu raporunda sadece gerçekleşen PnL değil, setup uyum oranı ve kural ihlali bayrakları (`violation_count`) metrikleştirilmelidir.
