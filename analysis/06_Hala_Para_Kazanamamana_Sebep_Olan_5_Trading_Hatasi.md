# 06 - Hâlâ Para Kazanamamana Sebep Olan 5 Trading Hatası

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
