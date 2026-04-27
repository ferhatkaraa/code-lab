# Python Mini Projeler ve Uygulamalar

Bu depo, Python ile geliştirilmiş çeşitli seviyelerdeki mini projeleri, oyunları ve algoritmik çözümleri içermektedir. Terminal tabanlı basit uygulamalardan, Tkinter kullanılarak geliştirilmiş masaüstü oyunlarına, modüler mimariye sahip kelime bulmacalarına, güvenlik algoritmalarına, dosya otomasyonlarına ve matematiksel hesaplama araçlarına kadar uzanan geniş bir yelpazeyi kapsar.

## 🚀 Projeler

### 1. Boggle Kelime Oyunu
`BOGGLE KELİME OYUNU.py` 
Klasik Boggle kelime bulmaca oyununun Python ile geliştirilmiş, modüler bir yapıya sahip versiyonu. Oyun, farklı işlevleri yerine getiren çeşitli betiklere bölünerek tasarlanmıştır:
* **`tahta.py`:** Oyun alanının (harf ızgarasının) rastgele ve kurallara uygun şekilde oluşturulmasını sağlayan modül.
* **`frekans.py`:** Harflerin dildeki kullanım sıklıklarına (frekanslarına) göre tahtaya mantıklı bir şekilde dağıtılmasını hesaplayan algoritma.
* **`kontroller.py`:** Oyuncunun bulduğu kelimenin tahtada yan yana/çapraz harflerle oluşturulup oluşturulamadığını ve geçerli bir kelime olup olmadığını denetleyen mantık dosyası.
* **`data.txt`:** Kelime doğrulaması için kullanılan yerel sözlük (veri tabanı) dosyası.
* **`proje diyagramı.docx`:** Projenin çalışma mantığını, algalgoritmik akışını ve modüller arası ilişkileri anlatan detaylı dokümantasyon.

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
Herhangi bir boyuttaki (N x N) kare matrisin determinantını rekürsif (özyinelemeli) bir fonksiyon kullanarak hesaplayan matematiksel bir algoritma. Veri yapıları ve algoritma analizi pratiği için ideal bir örnektir.

### 5. Terminal Oyunları (Sayı ve Renk Tahmini)
`tahmin oyunu.py` 
İçerisinde iki farklı mini oyun barındıran terminal uygulaması:
* **Sayı Tahmin Oyunu:** Bilgisayarın 1 ile 10 arasında tuttuğu sayıyı, "daha büyük" veya "daha küçük" ipuçlarını kullanarak bulma.
* **Renk Tahmin Oyunu:** Belirlenen renk havuzundan rastgele seçilen rengi tahmin etme ve kaçıncı denemede bulunduğunu sayma.

### 6. Banka Simülasyonu
`banka.py` 
Sözlük (`dict`) veri yapısı kullanılarak oluşturulmuş basit bir banka yönetim sistemi.
* **Özellikler:** Yeni hesap açma, para yatırma, para çekme ve hesaplar arası para transferi yapabilma.

### 7. Zamanlayıcı ve Alarm Sistemi
`alarm.py` 
Belirtilen süre boyunca geri sayım yapan veya spesifik bir saatte tetiklenen alarm uygulaması. Süre dolduğunda sistemdeki `alarm.mp4` dosyasını otomatik olarak çalıştırarak kullanıcıyı uyarır. (Çalışması için aynı dizinde `alarm.mp4` medya dosyasının bulunması gereklidir).

### 8. RSA Şifreleme Algoritması
`RSA.py` ve `metin.txt` 
Kriptografinin temel taşlarından biri olan RSA algoritmasının Python ile uygulanmış hali. 
* **Özellikler:** İletişimi güvenli hale getirmek için asimetrik şifreleme mantığını kullanır. Şifrelenecek veya deşifre edilecek veriler, dizindeki `metin.txt` dosyası üzerinden okunup işlenebilir.

### 9. Nöbet / Sıra Çizelgeleyici
`nöbet.py` 
Kişiler veya gruplar arasında görev, nöbet veya sıraya dayalı çizelgeler oluşturmak için tasarlanmış otomasyon betiği. Organizasyonel işleri kolaylaştırmayı ve adil bir dağılım yapmayı amaçlar.

### 10. Arama Aracı
`ara.py` 
Verilen veri setleri, listeler veya metinler içerisinde hızlı arama yapmayı sağlayan, temel arama algoritmalarının mantığını barındıran script.

### 11. Mors ve İkili Sistem Dönüştürücü (Encoder/Decoder)
`alfabe.csv` ve `mesaj.txt` 
Metinleri Mors alfabesine veya İkili (Binary) sisteme çeviren ve şifrelenmiş metinleri tekrar normal yazıya dönüştüren veri işleme aracı.
* **Özellikler:**
  * `pandas` kütüphanesi kullanılarak `alfabe.csv` dosyasındaki eşleşmelere göre hızlı dönüştürme (parsing) işlemi yapar.
  * Türkçe karakter desteği, büyük/küçük harf duyarlılığı ve yeni satır (`\n`) gibi istisnai (edge case) durumların kontrolünü içerir.
  * Tüm okuma ve yazma işlemleri `mesaj.txt` dosyası üzerinden otomatik olarak gerçekleşir.

### 12. Özel 8-Bit Metin Şifreleme Aracı
`sakla.py` 
Klasördeki metin dosyalarını bulup, baştan tasarlanmış özel bir 8-bitlik (1 byte) formatlama algoritması ile şifreleyen veya çözen otomasyon betiği.
* **Özellikler:**
  * Kendi içerisinde tanımlı `DATA` sözlüğünü kullanarak her karakteri (noktalama, büyük/küçük harf durumları dahil) özel bir 8-bitlik diziye çevirir.
  * Bulunduğu dizindeki tüm `.txt` dosyalarını `os` modülü ile otomatik olarak tarar.
  * Şifrelediği dosyaların ismine `$` işareti ekleyerek işaretler, kod çözme (decode) işleminde bu işareti tanıyarak dosyaları otomatik olarak orijinal haline döndürür.

---

## 📁 PYT Klasörü - Modüler Python Kütüphaneleri

`pyt/` klasörü, Python programlama dilinde sık kullanılan fonksiyonları ve sınıfları modüler bir yapıda bir araya getiren kapsamlı bir kütüphane koleksiyonudur. Her modül, belirli bir alana odaklanmış şekilde tasarlanmıştır ve geniş dokümantasyon ile birlikte gelmektedir.

### 🧮 Matematiksel İşlemler (`math_operations.py`)
Temel ve gelişmiş matematiksel fonksiyonları içeren kapsamlı modül.
* **Temel İşlemler:** Toplama, çıkarma, çarpma, bölme, üs alma, faktöriyel, Fibonacci dizisi
* **Gelişmiş Fonksiyonlar:** Asal sayı kontrolü, GCD/LCM hesaplama, Armstrong sayıları, faktör bulma
* **Algoritmalar:** Binary search, bubble sort, linear search, min/max bulma
* **Özellikler:** 20+ satır kod, detaylı docstring'ler, örnek kullanımlar

### 📧 E-posta Servisleri (`email_services.py`)
Gmail API ve SMTP protokollerini destekleyen tam özellikli e-posta yönetim sistemi.
* **Gmail API Entegrasyonu:** OAuth2 kimlik doğrulama, dosya ekli e-postalar, HTML format desteği
* **SMTP Çoklu Sağlayıcı:** Yandex, Gmail ve diğer SMTP sağlayıcıları için tek arayüz
* **Özellikler:** Toplu e-posta gönderimi, HTML e-postalar, e-posta şablonları, hata yönetimi
* **Kütüphaneler:** `smtplib`, `yagmail`, `google-api-python-client`

### 🔐 SSH Operasyonları (`ssh_operations.py`)
Uzak sunucu yönetimi ve otomatik yedekleme için gelişmiş SSH araç seti.
* **SSH Client:** Bağlantı yönetimi, komut çalıştırma, dosya transferi
* **Yedekleme Sistemi:** Ağ cihazları için otomatik yedekleme, zamanlanmış görevler
* **Ağ Tarama:** Aktif IP tespiti, port tarama, cihaz tipi belirleme
* **Özellikler:** Hata yönetimi, çoklu cihaz desteği, raporlama

### 📝 Metin İşleme (`text_processing.py`)
String manipülasyonu ve veri doğrulama için kapsamlı araç seti.
* **String Utilities:** String ters çevirme, palindrome kontrolü, kelime frekansı, URL/eposta ayıklama
* **Doğrulama Fonksiyonları:** E-posta, telefon, URL, şifre güçlüğü, kredi kartı doğrulama
* **Gelişmiş İşlemler:** Metin temizleme, anahtar kelime çıkarımı, okunabilirlik skoru, metin benzerliği
* **Özellikler:** Regex desenleri, çoklu dil desteği, istatistiksel analiz

### 💾 Veri Yönetimi (`data_management.py`)
Dosya işlemleri ve veri işleme için entegre yönetim sistemi.
* **DataProcessor:** JSON/CSV dosya işleme, veri filtreleme, sıralama, istatistiksel analiz
* **FileManager:** Dosya oluşturma, kopyalama, taşıma, hash hesaplama, içerik arama
* **Veri Analizi:** Veri yapısı analizi, veri temizleme, veri kaynaklarını birleştirme
* **Özellikler:** Hata yönetimi, çoklu format desteği, veri doğrulama

### 🧠 Gelişmiş Konseptler (`advanced_concepts.py`)
Python'un ileri düzey özelliklerini gösteren kapsamlı koleksiyon.
* **Iterator'lar ve Generator'lar:** Özel iterator sınıfları, generator fonksiyonları, Fibonacci/asal sayı generator'ları
* **Decorator'lar:** Zaman ölçümü, önbellekleme, yeniden deneme, tip doğrulama decorator'ları
* **Fonksiyonel Programlama:** Map-filter-reduce, fonksiyon kompozisyonu, currying
* **Algoritmalar:** Quick sort, merge sort, metaprogramming, magic methods
* **Özellikler:** Performans optimizasyonu, bellek verimliliği, kod yeniden kullanımı

### 🌐 Uzmanlaşmış Uygulamalar (`applications.py`)
Farklı alanlarda kullanılabilen özel uygulamalar koleksiyonu.
* **Web Otomasyonu:** Selenium WebDriver ile tarayıcı otomasyonu, sayfa navigasyonu
* **Bluetooth Ekran:** Bluetooth cihaz keşfi, Pygame ile ekran görüntüleme
* **OCR İşlemci:** Tesseract ile metin tanıma, PIL/OpenCV desteği, toplu işleme
* **Not Hesaplama:** Akademik not yönetimi, GPA hesaplama, istatistikler
* **Cihaz Sınıfı:** Magic methods ile cihaz temsili, iterator desteği
* **Özellikler:** GUI entegrasyonu, çoklu platform desteği, hata yönetimi

### 📅 Tarih/Saat İşlemleri (`date_time_utils.py`)
Tarih ve zaman manipülasyonu için pratik fonksiyonlar.
* **Temel İşlemler:** Mevcut tarih/saat, formatlama, parsing
* **Hesaplama:** Gün farkı, yaş hesaplama, çeyrek belirleme, artık yıl kontrolü
* **Formatlama:** Özel formatlar, ay/gün isimleri, saat dilimi desteği
* **Özellikler:** Uluslararası destek, esnek formatlama, istatistiksel işlemler

---

## 🛠️ Kurulum ve Kullanım

Bu depodaki projeleri kendi bilgisayarınızda çalıştırmak için:

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/kullaniciadin/repo-adi.git
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. İstediğiniz projeyi çalıştırın:
   ```bash
   python proje_adi.py
   ```

### 📋 Gerekli Kütüphaneler

Projelerde kullanılan temel kütüphaneler:
- `selenium` - Web otomasyonu
- `pygame` - Oyun geliştirme
- `tkinter` - GUI uygulamaları
- `pandas` - Veri işleme
- `paramiko` - SSH bağlantıları
- `opencv-python` - Görüntü işleme
- `pytesseract` - OCR metin tanıma
- `google-api-python-client` - Gmail API
- `yagmail` - E-posta gönderimi
- `bluetooth` - Bluetooth cihaz yönetimi

---

## 📖 Kullanım Örnekleri

### Matematiksel İşlemler
```python
from pyt.math_operations import *

# Temel işlemler
print(add(5, 3))  # 8
print(factorial(5))  # 120

# Gelişmiş fonksiyonlar
print(is_prime(17))  # True
print(find_factors(36))  # [1, 2, 3, 4, 6, 9, 12, 18, 36]
```

### E-posta Gönderimi
```python
from pyt.email_services import create_yandex_client

# Yandex e-posta client oluştur
client = create_yandex_client()
client.send_email_smtplib("alici@example.com", "Konu", "İçerik")
```

### SSH Bağlantısı
```python
from pyt.ssh_operations import SSHManager

# SSH bağlantısı kur
ssh = SSHManager("192.168.1.1", 22, "kullanici", "sifre")
if ssh.connect():
    success, output, error = ssh.execute_command("ls -la")
    print(output)
    ssh.disconnect()
```

---

## 🤝 Katkıda Bulunma

Projelere katkıda bulunmak için:

1. Bu depoyu fork edin
2. Yeni bir özellik dalı oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Dalınıza push edin (`git push origin feature/yeni-ozellik`)
5. Bir Pull Request oluşturun

---

## 📄 Lisans

Bu proje MIT Lisansı ile korunmaktadır. Detaylı bilgi için `LICENSE` dosyasını inceleyin.

---

## 📞 İletişim

Sorularınız veya önerileriniz için:
- E-posta: kullanici@example.com
- GitHub: @kullaniciadi

---

## 🔮 Gelecek Planlar

- [ ] Web tabanlı arayüz geliştirme
- [ ] Mobil uygulama desteği
- [ ] Bulut entegrasyonu
- [ ] Makine öğrenmesi modülleri
- [ ] API geliştirme

---

**Not:** Her modül kendi içinde detaylı dokümantasyon ve örnek kullanımlar içerir. Modülleri doğrudan projelerinizde kullanabilir veya kendi ihtiyaçlarınıza göre özelleştirebilirsiniz.
