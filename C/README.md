# Temel C Projeleri ve Algoritma Arşivi

Bu dizin, C programlama dilinde geliştirilmiş temel seviye algoritmaları, terminal uygulamalarını ve pratik kodları içermektedir. Zamanla yeni projeler, veri yapıları ve algoritmalar eklendikçe bu arşiv genişleyecektir.

## 🚀 Projeler

### 1. ASCII Sanatı: Koyun Çizimi
`koyun.c`
Terminal ekranına yıldızlar (`*`) ve boşluklar kullanarak dinamik boyutlarda bir hayvan (koyun) figürü çizen C programıdır.
* **Özellikler:**
  * Kullanıcıdan alınan genişlik değerine göre şeklin baş, boyun, gövde ve bacak oranlarını (`gen * 0.5`, `gen * 0.4` vb.) otomatik olarak hesaplar.
  * İç içe `for` döngüleri ve koşullu ifadeler (`if-else`) kullanılarak terminal ekranında matris tabanlı geometrik çizim yapma mantığını (ASCII art) pratik etmeyi sağlar.

*(Yeni projeler eklendikçe buraya listelenecektir...)*

---

## 🛠️ Kurulum ve Kullanım

Bu dizindeki C dosyalarını derlemek ve çalıştırmak için sisteminizde bir C derleyicisi (örneğin GCC veya MinGW) kurulu olmalıdır.

1. Terminali açın ve çalıştırmak istediğiniz `.c` dosyasının bulunduğu dizine gidin.
2. Kodu derlemek için aşağıdaki komutu çalıştırın:
   ```bash
   gcc dosya_adi.c -o program_adi