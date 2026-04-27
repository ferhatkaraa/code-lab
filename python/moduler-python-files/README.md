# Python Comprehensive Library

Kapsamlı Python modülleri koleksiyonu - çeşitli alanlarda hazır fonksiyonlar ve sınıflar içeren tam özellikli bir kütüphane.

## 📋 İçerik

Bu proje, Python programlama dilinde sık kullanılan çeşitli işlevleri bir araya getiren modüllerden oluşur. Her modül belirli bir alanda uzmanlaşmıştır ve kolay kullanım için hazır fonksiyonlar sunar.

## 🗂️ Modüller

### 1. [advanced_concepts.py](advanced_concepts.py)
**İleri Düzey Python Konseptleri**
- **İteratörler ve Generatörler**: Özel iterator sınıfları, sayı ve Fibonacci generatörleri
- **Dekoratörler**: Zaman ölçme, önbelleğe alma, yeniden deneme, tip doğrulama
- **Closure'lar ve Yüksek Seviyeli Fonksiyonlar**: Çarpıcı, toplayıcı, fonksiyon kompozisyonu
- **İleri Düzey Algoritmalar**: Quick sort, merge sort, arama algoritmaları
- **Fonksiyonel Programlama**: Map-filter-reduce, curry fonksiyonları
- **Metaprogramlama**: Method logger metaclass

### 2. [applications.py](applications.py)
**Özelleştirilmiş Uygulamalar**
- **Web Otomasyonu**: Selenium WebDriver tabanlı tarayıcı otomasyonu
- **Bluetooth Ekran Yönetimi**: Cihaz keşfi ve ekran görüntüleme
- **OCR İşlemci**: Tesseract ile metin çıkarma, görüntü ön işleme
- **Not Hesaplama Sistemi**: Akademik not yönetimi ve GPA hesaplama
- **Cihaz Sınıfı**: Magic methods ile cihaz temsili

### 3. [data_management.py](data_management.py)
**Veri Yönetimi**
- **Veri İşlemci**: JSON ve CSV dosya işlemleri, filtreleme, sıralama
- **Dosya Yöneticisi**: Dosya oluşturma, kopyalama, taşıma, silme
- **Veri Analiz Araçları**: Yapı analizi, veri temizleme, birleştirme
- **Güvenlik**: Dosya hash hesaplama (MD5, SHA vb.)

### 4. [date_time_utils.py](date_time_utils.py)
**Tarih ve Saat Araçları**
- **Temel İşlemler**: Mevcut tarih/saat, formatlama, ayrıştırma
- **Tarih Hesaplamaları**: Gün ekleme, tarih farkı, yaş hesaplama
- **Yardımcı Fonksiyonlar**: Hafta sonu kontrolü, çeyrek belirleme, artık yıl
- **Formatlama**: Ay isimleri, gün isimleri, özel formatlar

### 5. [email_services.py](email_services.py)
**E-posta Servisleri**
- **Gmail API**: OAuth2 kimlik doğrulama ile e-posta gönderme
- **SMTP İstemcileri**: Yandex, Gmail için çoklu destek
- **HTML E-posta**: Zengin içerikli e-postalar
- **Toplu E-posta**: Çoklu alıcı gönderimi
- **Ek Dosya**: Resim ve dosya ekleme desteği

### 6. [math_operations.py](math_operations.py)
**Matematiksel İşlemler**
- **Temel İşlemler**: Toplama, çıkarma, çarpma, bölme, üs alma
- **İleri Matematik**: Asal sayı kontrolü, GCD, LCM, Armstrong sayıları
- **Sayı Analizi**: Basamak toplamı, ters çevirme, faktör bulma
- **Algoritmalar**: İkili arama, bubble sort, lineer arama
- **Özel Sayılar**: Fibonacci, faktöriyel, mükemmel kareler

### 7. [ssh_operations.py](ssh_operations.py)
**SSH Operasyonları**
- **SSH İstemci Yönetimi**: Bağlantı, komut çalıştırma, çıktı kaydetme
- **Yedekleme Sistemi**: Otomatik yapılandırma yedeklemeleri
- **Ağ Tarama**: Aktif cihaz keşfi, port tarama
- **Cihaz Yönetimi**: Cihaz tipi belirleme, versiyon takibi
- **Toplu İşlemler**: Çoklu cihaz yönetimi

### 8. [text_processing.py](text_processing.py)
**Metin İşleme**
- **String Araçları**: Ters çevirme, palindrom, harf sayımı
- **Metin Çıkarma**: E-posta, telefon, URL çıkarma
- **Doğrulama**: E-posta, telefon, URL, şifre gücü
- **İleri İşleme**: Metin temizleme, anahtar kelime çıkarma
- **Metrikler**: Okunabilirlik skoru, metin benzerliği

## 🚀 Kurulum

### Gerekli Kütüphaneler

```bash
# Standart kütüphaneler (genellikle önceden kuruludur)
pip install pywin32-bootstrap pygame bluetooth selenium tesseract pillow opencv-python yagmail paramiko google-api-python-client google-auth-oauthlib google-auth-httplib2
```

### Notlar
- **Tesseract OCR**: Ayrı olarak kurulmalı ve PATH'e eklenmeli
- **Selenium WebDriver**: Tarayıcı sürücüleri gereklir
- **Bluetooth**: Donanım desteği gerektirir

## 📖 Kullanım Örnekleri

### İleri Düzey Konseptler
```python
from advanced_concepts import fibonacci_generator, timer_decorator

@timer_decorator
def test_function():
    fib_gen = fibonacci_generator(10)
    return list(fib_gen)

result = test_function()
print(result)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Veri Yönetimi
```python
from data_management import DataProcessor

processor = DataProcessor()
data = processor.load_json('data.json')
filtered = processor.filter_data('age', 25)
stats = processor.get_statistics('age')
```

### E-posta Gönderme
```python
from email_services import create_gmail_smtp_client

client = create_gmail_smtp_client()
client.send_email_smtplib('alici@example.com', 'Konu', 'Mesaj içeriği')
```

### SSH Operasyonları
```python
from ssh_operations import SSHManager

ssh = SSHManager('192.168.1.1', 22, 'admin', 'password')
if ssh.connect():
    success, output, error = ssh.execute_command('show version')
    ssh.disconnect()
```

## 🔧 Özellikler

### ✅ Avantajlar
- **Modüler Tasarım**: Her modül belirli bir alanda uzmanlaşmış
- **Hazır Fonksiyonlar**: Hemen kullanılabilir fonksiyonlar
- **Geniş Kapsam**: Matematikten ağ yönetimine kadar birçok alan
- **Türkçe Destek**: Yerel dilde yorum ve hata mesajları
- **Demo Fonksiyonları**: Her modülde örnek kullanım

### 🎯 Kullanım Alanları
- **Otomasyon**: Web, SSH, Bluetooth otomasyonları
- **Veri Analizi**: CSV, JSON işlemleri ve analiz
- **İletişim**: E-posta gönderme ve yönetimi
- **Matematik**: Hesaplama ve algoritma implementasyonları
- **Metin İşleme**: Doğal dil işleme ve doğrulama

## 📊 Modül İstatistikleri

| Modül | Satır Sayısı | Fonksiyon Sayısı | Sınıf Sayısı |
|-------|--------------|------------------|--------------|
| advanced_concepts.py | 534 | 25+ | 4 |
| applications.py | 750 | 30+ | 5 |
| data_management.py | 496 | 20+ | 2 |
| date_time_utils.py | 157 | 12 | 0 |
| email_services.py | 359 | 15+ | 2 |
| math_operations.py | 352 | 25+ | 0 |
| ssh_operations.py | 460 | 20+ | 2 |
| text_processing.py | 398 | 30+ | 0 |

## 🛠️ Geliştirme

### Kod Standartları
- **PEP 8**: Python kodlama standartlarına uyum
- **Type Hints**: Fonksiyon parametreleri ve dönüş değerleri
- **Docstrings**: Detaylı fonksiyon açıklamaları
- **Error Handling**: Kapsamlı hata yönetimi

### Test Etme
Her modülün sonunda bulunan demo fonksiyonları ile test yapabilirsiniz:

```bash
python advanced_concepts.py
python applications.py
python data_management.py
# ... diğer modüller
```

## 📝 Lisans

Bu proje açık kaynaklıdır ve özgürce kullanılabilir.

## 🤤 Katkı

Katkıda bulunmak isterseniz:
1. Yeni özellikler ekleyebilirsiniz
2. Mevcut kodları iyileştirebilirsiniz
3. Hata raporları oluşturabilirsiniz
4. Dokümantasyon güncellemeleri yapabilirsiniz

## 📞 İletişim

Sorular ve öneriler için proje iletişim kanallarını kullanabilirsiniz.

---

**Python Comprehensive Library (PYT)** - Her şeyi bir arada tutan Python kütüphanesi! 🐍✨
