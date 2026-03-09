#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

// ==========================================
// 1. UYGULAMA: Vector ve String (yenicdosyasý.cPP)
// ==========================================
void yeni_cpp_uygulamasi() {
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    printf("hello world\n");

    for (const string& word : msg) {
        cout << word << " ";
    }
    cout << endl;
}

// ==========================================
// 2. UYGULAMA: Pointer Mantýðý (pointer.cpp)
// ==========================================
void pointer_uygulamasi() {
    int c, b = 3;
    int *q = &c, *w = &b;
    int array[5] = {1, 2, 3, 4, 5};
    int *a = array;
    int *k = &array[2];
    c = 2;
    
    // Adresleri %u ile yazdýrýyoruz
    printf("a'nin adresi: %u\n", a);
    printf("a+1: %u\n", a + 1);
    printf("a+2: %u\n", a + 2);
    printf("a+3: %u\n", a + 3);
    printf("a+4: %u\n", a + 4);
    
    printf("*a degeri: %d\n", *a);
    printf("*(k-1) degeri: %d\n", *(k - 1));

    printf("*(a+1): %d\n", *(a + 1));
    printf("*(a+2): %d\n", *(a + 2));
    printf("*(a+3): %d\n", *(a + 3));
    printf("*(a+4): %d\n", *(a + 4));
    
    printf("array adresi: %u\n", array);
    printf("array+1 adresi: %u\n", array + 1);
    
    printf("*array degeri: %d\n", *array);
    printf("*(array+1) degeri: %d\n", *(array + 1));
    printf("array[2] degeri: %d\n", array[2]);
    printf("a[3] degeri: %d\n", a[3]);
    
    printf("&c: %u, &b: %u, q: %u, w: %u\n", &c, &b, q, w);
    printf("c: %d, b: %d, *q: %d, *w: %d\n", c, b, *q, *w);
}

// ==========================================
// 3. UYGULAMA: Basit Girdi (Untitled1.cpp)
// ==========================================
void untitled1_uygulamasi() {
    int say;
    printf("Bir sayi giriniz: ");
    
    // scanf içindeki ampersand (&) eksiði giderildi
    scanf("%d", &say);
    printf("hello world! Girdiginiz sayi: %d\n", say);
}

// ==========================================
// 4. UYGULAMA: Merhaba Dunya (Untitled5.cpp)
// ==========================================
void untitled5_uygulamasi() {
    printf("hello world\n");
}

// ==========================================
// 5. UYGULAMA: Yasin - Proje Taslaðý (yasin.cpp)
// ==========================================
void yasin_proje_taslagi() {
    printf("--- Yasin: Okul/Kurs Yonetim Sistemi Taslagi ---\n");
    printf("Planlanan Veri Yapilari: Ogrenci, Ogretmen, Dersler, Borclar, Veri Tabani vs.\n");
    printf("Algoritma Adimlari:\n");
    printf("1. Uygulama acilir.\n");
    printf("2. Kullanici adi ve sifre sorgulanir (Max 5 deneme).\n");
    printf("3. Ogretmen / Ogrenci yetkisi kontrol edilir.\n");
    printf("4. Yetki Ogretmen ise: Ders acar, kapatir, ogrenci ve odeme goruntuler.\n");
    printf("5. Yetki Ogrenci ise: Derse kayit olur, borc goruntuler, odeme yapar.\n");
}

// ==========================================
// ANA FONKSÝYON VE MENÜ DÖNGÜSÜ
// ==========================================
int main() {
    int secim;
    bool devam = true;

    while(devam) {
        printf("\n=================================\n");
        printf("--- C++ KARISIK DOSYALAR ARSIVI ---\n");
        printf("1. Vector ve String Ekrana Bas (yenicdosyasi.cPP)\n");
        printf("2. Pointer Mantigi ve Bellek (pointer.cpp)\n");
        printf("3. Sayi Girisi Alma (Untitled1.cpp)\n");
        printf("4. Sadece Hello World (Untitled5.cpp)\n");
        printf("5. Proje Algoritma Taslagi Oku (yasin.cpp)\n");
        printf("0. Cikis\n");
        printf("Seciminiz: ");
        scanf("%d", &secim);
        printf("=================================\n\n");

        switch (secim) {
            case 1:
                yeni_cpp_uygulamasi();
                break;
            case 2:
                pointer_uygulamasi();
                break;
            case 3:
                untitled1_uygulamasi();
                break;
            case 4:
                untitled5_uygulamasi();
                break;
            case 5:
                yasin_proje_taslagi();
                break;
            case 0:
                devam = false;
                printf("Programdan cikiliyor. Gorusmek uzere!\n");
                break;
            default:
                printf("Gecersiz secim. Lutfen 0-5 arasi bir deger girin.\n");
                break;
        }
    }
    return 0;
}
