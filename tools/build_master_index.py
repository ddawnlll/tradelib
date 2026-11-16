#!/usr/bin/env python3
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ANALYSIS_DIR = BASE_DIR / "analysis"
CLEAN_DIR = BASE_DIR / "data" / "transcripts" / "cleaned"
INDEX_PATH = BASE_DIR / "MASTER_INDEX.md"

items = [
    {
        "id": "01",
        "file": "01_Profesyonel_Trader_Olmak_Icin_Gercekte_Ne_Gerekir.md",
        "title": "Profesyonel Trader Olmak İçin Gerçekte Ne Gerekir?",
        "vid": "Pbh_XGFYQ4E",
        "tags": ["Prop Desk", "Disiplin", "Rutin", "Biyoloji", "Kasa Zihniyeti"],
        "core_rule": "Günün sorusu 'Bugün para kazandım mı?' değil, 'Bugün planıma uydum mu?' olmalıdır."
    },
    {
        "id": "02",
        "file": "02_Kasa_Her_Zaman_Kazanir_Trader_Kasa_Olabilir_mi.md",
        "title": "Kasa Her Zaman Kazanır. Trader Kasa Olabilir mi?",
        "vid": "J-6bHLN-D70",
        "tags": ["Olasılık", "Rulet", "Edge", "Mark Douglas", "Büyük Sayılar"],
        "core_rule": "Küçük avantaj (%2.7 edge) + çok sayıda tekrar + katı masa limiti = Kasa Zihniyeti."
    },
    {
        "id": "03",
        "file": "03_Yanlis_Mentorla_Yillari_Kaybetmek_5_Filtre.md",
        "title": "Trader'ların Çoğu Yıllarını Yanlış Mentorla Kaybediyor (5 Filtre)",
        "vid": "K7TldQMEMEw",
        "tags": ["Mentörlük", "Prop Desk", "Risk Takıntısı", "Süreç", "Erişilebilirlik"],
        "core_rule": "Riske takıntılı olmayan, sadece giriş anlatan bir mentörden derhal uzaklaşılmalıdır."
    },
    {
        "id": "04",
        "file": "04_Traderlarin_Cogu_Neden_Ilk_Yilda_Birakiyor.md",
        "title": "Trader'ların Çoğu Neden İlk Yılda Bırakıyor?",
        "vid": "WIyUKrAyE_c",
        "tags": ["Day Trading", "Kaldıraç", "Strateji Atlamak", "Maliyet Düşürme"],
        "core_rule": "Kaldıraç sermaye imha aracıdır (500:1'de %0.2 ters hareket sıfırlar); maliyet düşürme cinayettir."
    },
    {
        "id": "05",
        "file": "05_Trader_Olmak_Ne_Kadar_Surer_Durust_Cevap.md",
        "title": "Trader Olmak Ne Kadar Sürer? (Dürüst Cevap)",
        "vid": "NDENGqeOPog",
        "tags": ["Runway", "Hava Yastığı", "Sermaye Baskısı", "Zaman"],
        "core_rule": "2 yıllık yaşam gideri hava yastığı olmadan iş bırakılmaz; 5.000$ hesap kira ödeyemez."
    },
    {
        "id": "06",
        "file": "06_Hala_Para_Kazanamamana_Sebep_Olan_5_Trading_Hatasi.md",
        "title": "Hâlâ Para Kazanamamana Sebep Olan 5 Trading Hatası",
        "vid": "Go19JcFyUDM",
        "tags": ["Seykota", "Plansızlık", "İndikatör Tuzağı", "Pusu"],
        "core_rule": "Herkes piyasadan istediğini alır (macera vs para); stop seviyesi olmadan lot hesaplanamaz."
    },
    {
        "id": "07",
        "file": "07_Evden_Trade_Neden_Pahaliya_Patlar_Ofisin_5_Avantaji.md",
        "title": "Evden Trade Yapmak Neden Pahalıya Patlar? Trading Ofisinin 5 Avantajı",
        "vid": "8dq2UEboEfY",
        "tags": ["Prop Ofisi", "Kolektif Zeka", "Sermaye Güvencesi", "Çevre"],
        "core_rule": "Şirket parasıyla işlem yapmak iflas riskini sıfırlar; 10 çift göz 1 çift gözü daima yener."
    },
    {
        "id": "08",
        "file": "08_Hangi_Trading_Stratejisi_Sana_Gore.md",
        "title": "Hangi Trading Stratejisi Sana Göre? (4 Temel Zaman Dilimi)",
        "vid": "_JX74IZoEvA",
        "tags": ["Scalping", "Day Trading", "Swing Trading", "Position Trading"],
        "core_rule": "Tek bir doğru stil yoktur; yaşam tarzına ve risk toleransına uygun tek stile sadık kalınmalıdır."
    },
    {
        "id": "09",
        "file": "09_Profesyonel_Traderlar_Kanamayi_Bu_Sekilde_Durdurur.md",
        "title": "Profesyonel Traderlar Kanamayı Bu Şekilde Durdurur",
        "vid": "ItTG09VLeNQ",
        "tags": ["Kanamayı Durdurma", "Step-Down Matrix", "Çukuru Bırak", "Nakit"],
        "core_rule": "Kayıp serisinde vites küçültülür (1000->500->300->100 hisse); çukurdayken kazma bırakılır."
    },
    {
        "id": "10",
        "file": "10_Dogru_Trading_Mentoru_Nasil_Secilir.md",
        "title": "Doğru Trading Mentoru Nasıl Seçilir?",
        "vid": "d63KKdbeygs",
        "tags": ["Mentör Seçimi", "Canlı Masada Öğrenme", "Filtre"],
        "core_rule": "Mentörlük paket video değil, aynı işlem masasını paylaşarak anlık refleksleri kopyalamaktır."
    },
    {
        "id": "11",
        "file": "11_Traderlarin_Yuzde_95i_Neden_Kaybeder_5_Kritik_Beceri.md",
        "title": "Traderların %95’i Neden Kaybediyor? (5 Kritik Beceri)",
        "vid": "5h-nMtuRFXk",
        "tags": ["Duygusal Kontrol", "Ekran Kapalı Karar", "Sabır", "Rejim"],
        "core_rule": "Kararları ekran kapalıyken al; 5 şartın 4'ü varsa o işlem kesinlikle pas geçilir."
    },
    {
        "id": "12",
        "file": "12_Ust_Uste_Stop_Oldugunuzda_Ne_Yapmalisiniz_Kriz_Plani.md",
        "title": "Üst Üste Stop Olduğunuzda Ne Yapmalısınız? (Kriz Planı)",
        "vid": "osNo6QPso9Q",
        "tags": ["Devre Kesici", "Haftalık %5", "Logaritmik Erime", "Varyans"],
        "core_rule": "Haftalık %5 kayıpta işlem durdurulur; sonraki hafta risk %1'den %0.5'e indirilir."
    },
    {
        "id": "13",
        "file": "13_Islemlerin_Yarisinda_Yanilip_Yine_de_Para_Kazanmak.md",
        "title": "İşlemlerin Yarısında Yanılıp Yine de Nasıl Para Kazanılır?",
        "vid": "d5R7xP542SA",
        "tags": ["R-Multiple", "Pozisyon Boyutu", "1R Kuralı", "Asimetrik Kazanç"],
        "core_rule": "Lot = Riske Edilen $ / (Giriş - Stop). Risk sabit kalır, stop mesafesine göre lot ayarlanır."
    },
    {
        "id": "14",
        "file": "14_Trading_Kariyerini_Yukseltecek_3_Efsanevi_Kitap.md",
        "title": "Trading Kariyerinizi Bir Üst Seviyeye Taşıyacak 3 Efsanevi Kitap",
        "vid": "jZZChh99xZw",
        "tags": ["Jesse Livermore", "Mark Douglas", "Jack Schwager"],
        "core_rule": "Livermore'dan sabır, Douglas'tan olasılık inancı, Schwager'dan demir gibi risk disiplini."
    },
    {
        "id": "15",
        "file": "15_Hesabinizi_Sifirlayan_5_Psikolojik_Tuzak.md",
        "title": "Çoğu Trader Neden Kaybeder? Hesabınızı Sıfırlayan 5 Psikolojik Tuzak",
        "vid": "Zfu6xtNVKBk",
        "tags": ["İntikam İşlemi", "Aşırı Özgüven", "FOMO", "Analiz Felci"],
        "core_rule": "Kaçan işlem bedavadır, plansız işlem sermayeyi yer; intikam işlemini ekrandan kalkarak kes."
    },
    {
        "id": "16",
        "file": "16_Ace_Trading_CEO_Anton_Panayatov_Bloomberg_Teardown.md",
        "title": "Ace Trading CEO Anton Panayatov talks to Bloomberg (Teardown)",
        "vid": "x2HZXLmIJow",
        "tags": ["Anton Panayatov", "Hedge Fund", "İstatistiksel Arbitraj", "Bloomberg"],
        "core_rule": "Finansal piyasalar bir bilimdir; regülasyonsuz kumar değil, türev ve arbitraj dengesi esastır."
    },
    {
        "id": "17",
        "file": "17_Mikro_Kurallar_ve_Shorts_Katalogu.md",
        "title": "Ace Trading Mikro Kurallar & 27 Shorts Kataloğu",
        "vid": "SHORTS",
        "tags": ["Shorts", "Mikro Kurallar", "Özet İlkeler"],
        "core_rule": "Gürültü dışına stop koy; satmadıkça zararda değilim yalanını terk et; ilk kârları koru."
    }
]

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write("# Tradelib: Master Index & Research Catalog\n\n")
    f.write("Ace Trading TR kurumsal prop desk video kütüphanesi, kurumsal risk kuralları ve kantitatif icraat haritası.\n\n")
    f.write("---\n\n")
    f.write("| ID | Başlık | Video ID | Odak Kavramlar | Temel Kurumsal Kural & Aksiyon |\n")
    f.write("|:---|:---|:---|:---|:---|\n")
    for it in items:
        link = f"[{it['title']}](analysis/{it['file']})"
        tags = ", ".join([f"`{t}`" for t in it["tags"]])
        f.write(f"| **{it['id']}** | {link} | `{it['vid']}` | {tags} | {it['core_rule']} |\n")
    f.write("\n---\n\n")
    f.write("## Kategoriye Göre Hızlı Erişim\n\n")
    f.write("- **Kasa Yönetimi & Olasılık Matematiği:** [02 - Kasa Her Zaman Kazanır](analysis/02_Kasa_Her_Zaman_Kazanir_Trader_Kasa_Olabilir_mi.md) | [13 - İşlemlerin Yarısında Yanılmak](analysis/13_Islemlerin_Yarisinda_Yanilip_Yine_de_Para_Kazanmak.md)\n")
    f.write("- **Kriz Yönetimi & Drawdown Protokolleri:** [09 - Kanamayı Durdurma](analysis/09_Profesyonel_Traderlar_Kanamayi_Bu_Sekilde_Durdurur.md) | [12 - Üst Üste Stop Kriz Planı](analysis/12_Ust_Uste_Stop_Oldugunuzda_Ne_Yapmalisiniz_Kriz_Plani.md)\n")
    f.write("- **Prop Desk Disiplini & Rutinler:** [01 - Profesyonel Trader](analysis/01_Profesyonel_Trader_Olmak_Icin_Gercekte_Ne_Gerekir.md) | [07 - Ofis Avantajı](analysis/07_Evden_Trade_Neden_Pahaliya_Patlar_Ofisin_5_Avantaji.md) | [16 - Anton Panayatov](analysis/16_Ace_Trading_CEO_Anton_Panayatov_Bloomberg_Teardown.md)\n")
    f.write("- **Psikolojik Tuzaklar & Bilişsel Hatalar:** [11 - %95 Neden Kaybeder](analysis/11_Traderlarin_Yuzde_95i_Neden_Kaybeder_5_Kritik_Beceri.md) | [15 - 5 Psikolojik Tuzak](analysis/15_Hesabinizi_Sifirlayan_5_Psikolojik_Tuzak.md)\n")
    f.write("- **Kariyer Eğrisi & Sermaye Hazırlığı:** [04 - İlk Yılda Bırakma](analysis/04_Traderlarin_Cogu_Neden_Ilk_Yilda_Birakiyor.md) | [05 - Trader Olmak Ne Kadar Sürer](analysis/05_Trader_Olmak_Ne_Kadar_Surer_Durust_Cevap.md)\n")
    f.write("- **Mikro Kurallar & Shorts:** [17 - 27 Shorts Kataloğu](analysis/17_Mikro_Kurallar_ve_Shorts_Katalogu.md)\n")

print(f"Master index created successfully: {INDEX_PATH.name}")
