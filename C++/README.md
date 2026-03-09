# C++ Algoritma ve Mini Proje Arşivi

Bu depo, C++ ile geliştirilmiş çeşitli seviyelerdeki mini projeleri, terminal tabanlı oyunları ve algoritmik çözümleri içermektedir. Temel matematiksel işlemlerden başlayarak; matris manipülasyonları, bellek yönetimi (pointers), veri yapıları (`struct`, `vector`) ve dosya giriş/çıkış (File I/O) işlemlerine kadar geniş bir yelpazede pratikler barındırır.

## 🚀 Projeler ve Uygulamalar

### 1. Online Ders Giriş ve Yönetim Sistemi (Mini Veritabanı)
Dosya işlemleri (`<fstream>`) ve `struct` yapısı kullanılarak tasarlanmış, terminal tabanlı kapsamlı bir otomasyon sistemidir.
* **Özellikler:**
  * Öğrenci ve Öğretmenler için ayrı yetkilendirme (authorization) ve giriş yapısı.
  * Yeni kullanıcı kaydı oluşturma ve şifre doğrulama (Kayıtlar `.txt` dosyalarında tutulur).
  * **Öğretmen Yetkileri:** Sisteme yeni ders ekleme ve mevcut dersleri silme.
  * **Öğrenci Yetkileri:** Açılan derslere kayıt olma (derse katılma) ve dersten ayrılma.
  * Derslere kayıtlı öğrencilerin listesini dosya üzerinden okuyarak dinamik bir şekilde ekranda görüntüleyebilme.

### 2. Gelişmiş Sayı Tahmin Oyunu
Kullanıcının 0 ile 100 arasında rastgele belirlenen veya sabitlenen bir sayıyı bulmaya çalıştığı terminal oyunudur.
* **Özellikler:**
  * Toplam 5 tahmin hakkı bulunur.
  * Kullanıcının girdiği tahmine göre aranacak min/max aralığı dinamik olarak daraltılır ve ekrana yazdırılır.
  * **Hata Kontrolü (Edge Case):** Kullanıcı belirlenen aralığın dışında bir sayı girerse uyarılır ve o turdaki tahmin hakkı eksiltilmez.

### 3. C++ Algoritma Arşivi - 1 (Matematik ve Matrisler)
Birçok küçük matematiksel uygulamanın tek bir `switch-case` menüsü altında toplandığı modüler arşiv dosyasıdır.
* **İçerik:**
  * **Fibonacci Hesaplayıcı:** İstenilen basamağa kadar Fibonacci dizisini diziler (`array`) kullanarak oluşturur.
  * **Matris İşlemleri:** İki boyutlu ($2 \times 2$) matrisler üzerinde toplama, matris çarpımı ve transpoz (devrik) alma işlemlerini gerçekleştirir.
  * **2. Dereceden Denklem Çözücü:** Kullanıcıdan alınan katsayılara ($a, b, c$) göre diskriminant ($\Delta$) hesaplar ve `<math.h>` kütüphanesi yardımıyla kökleri ($x_1, x_2$) bulur.
  * **Not Hesaplayıcı:** Vize ve final ağırlıklarına göre harf/geçme notu hesaplar.

### 4. C++ Algoritma Arşivi - 2 (Bellek ve Veri Yapıları)
C++'ın bellek yönetimi ve standart şablon kütüphanesi (STL) özelliklerini barındıran menü tabanlı arşivdir.
* **İçerik:**
  * **Pointer Mantığı:** Değişkenlerin ve dizilerin (array) bellekteki adreslerini (`&`), pointer atamalarını (`*`) ve bellek aritmetiğini (`a+1`) gösteren detaylı bir bellek okuma pratiği.
  * **Vector ve String İşlemleri:** C++ STL `<vector>` ve `<string>` yapılarını kullanarak veri listeleme ve ekrana yazdırma testleri.
  * **Proje Taslakları:** Algoritma planlama ve sözde kod (pseudo-code) pratikleri.

---

## 🛠️ Kurulum ve Kullanım

Projeleri kendi yerel makinenizde derlemek ve çalıştırmak için sisteminizde bir C++ derleyicisi (örneğin `g++` veya `MinGW`) kurulu olmalıdır.

1. Depoyu bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/kullaniciadin/repo-adi.git](https://github.com/kullaniciadin/repo-adi.git)