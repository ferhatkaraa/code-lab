# Python Mini Projeler ve Uygulamalar

Bu depo, Python ile geliştirilmiş çeşitli seviyelerdeki mini projeleri, oyunları ve algoritmik çözümleri içermektedir. Terminal tabanlı basit uygulamalardan, Tkinter kullanılarak geliştirilmiş masaüstü oyunlarına, modüler mimariye sahip kelime bulmacalarına ve matematiksel hesaplama araçlarına kadar uzanan geniş bir yelpazeyi kapsar.

## 🚀 Projeler

### 1. Boggle Kelime Oyunu
`BOOGLE KELİME OYUNU.py`
Klasik Boggle kelime bulmaca oyununun Python ile geliştirilmiş, modüler bir yapıya sahip versiyonu. Oyun, farklı işlevleri yerine getiren çeşitli betiklere bölünerek tasarlanmıştır:
* **`tahta.py`:** Oyun alanının (harf ızgarasının) rastgele ve kurallara uygun şekilde oluşturulmasını sağlayan modül.
* **`frekans.py`:** Harflerin dildeki kullanım sıklıklarına (frekanslarına) göre tahtaya mantıklı bir şekilde dağıtılmasını hesaplayan algoritma.
* **`kontroller.py`:** Oyuncunun bulduğu kelimenin tahtada yan yana/çapraz harflerle oluşturulup oluşturulamadığını ve geçerli bir kelime olup olmadığını denetleyen mantık dosyası.
* **`data.txt`:** Kelime doğrulaması için kullanılan yerel sözlük (veri tabanı) dosyası.
* **`proje diyagramı.docx`:** Projenin çalışma mantığını, algoritmik akışını ve modüller arası ilişkileri anlatan detaylı dokümantasyon.

### 2. Taş-Kağıt-Makas Oyunu (GUI)
`taş-kağıt-makas.py`
Tkinter kütüphanesi kullanılarak tasarlanmış grafiksel bir arayüze (GUI) sahip klasik Taş-Kağıt-Makas oyunu. 
* **Özellikler:** * Bilgisayara karşı (PvE) veya aynı ekranda arkadaşınla (PvP) oynayabilme seçeneği.
  * Oyuncu isimlerini kişiselleştirebilme.
  * Skor takibi ve hamle geçmişini ekranda görebilme.
* **Gereksinimler:** Çalıştırmak için aynı dizinde `tas.png`, `kağıt.png`, `makas.png` ve `tkm.png` görsellerinin bulunması gerekir.

### 3. İl - Plaka Tahmin Oyunu
`baskent.py`
Türkiye'deki illerin ve plaka kodlarının tahmin edilmesine dayalı, zamana karşı yarışılan bir terminal oyunu.
* **Özellikler:**
  * 10 dakikalık (600 saniye) süre sınırı.
  * İki farklı mod: İlden plaka kodu tahmin etme veya plakadan il tahmin etme.
  * 50 soruluk setler halinde rastgele soru üretimi ve anlık doğru/yanlış/boş istatistikleri.

### 4. Matris Determinant Hesaplayıcı
`matriscoz.py`
Herhangi bir boyuttaki ($N \times N$) kare matrisin determinantını rekürsif (özyinelemeli) bir fonksiyon kullanarak hesaplayan matematiksel bir algoritma. Veri yapıları ve algoritma analizi pratiği için ideal bir örnektir.

### 5. Terminal Oyunları (Sayı ve Renk Tahmini)
`tahmin oyunu.py`
İçerisinde iki farklı mini oyun barındıran terminal uygulaması:
* **Sayı Tahmin Oyunu:** Bilgisayarın 1 ile 10 arasında tuttuğu sayıyı, "daha büyük" veya "daha küçük" ipuçlarını kullanarak bulma.
* **Renk Tahmin Oyunu:** Belirlenen renk havuzundan rastgele seçilen rengi tahmin etme ve kaçıncı denemede bulunduğunu sayma.

### 6. Banka Simülasyonu
`banka.py`
Sözlük (`dict`) veri yapısı kullanılarak oluşturulmuş basit bir banka yönetim sistemi.
* **Özellikler:** Yeni hesap açma, para yatırma, para çekme ve hesaplar arası para transferi yapabilme.

### 7. Zamanlayıcı ve Alarm Sistemi
`alarm.py`
Belirtilen süre boyunca geri sayım yapan veya spesifik bir saatte tetiklenen alarm uygulaması. Süre dolduğunda sistemdeki `alarm.mp4` dosyasını otomatik olarak çalıştırarak kullanıcıyı uyarır. (Çalışması için aynı dizinde `alarm.mp4` medya dosyasının bulunması gereklidir).

---

## 🛠️ Kurulum ve Kullanım

Bu depodaki projeleri kendi bilgisayarınızda çalıştırmak için:

1. Depoyu klonlayın:
   ```bash
   git clone [https://github.com/kullaniciadin/repo-adi.git](https://github.com/kullaniciadin/repo-adi.git)