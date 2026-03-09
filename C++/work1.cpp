#include <stdio.h>
#include <iostream>
#include <math.h> // Denklem çözümündeki sqrt() (karekök) fonksiyonu için eklendi

using namespace std;

// ==========================================
// 1. UYGULAMA: Fibonacci (fibonacci.cpp)
// ==========================================
void fibonacci_uygulamasi() {
    int array[100] = {1, 1, 2};
    int i, siradaki;
    
    printf("Ilk kac fibonacci sayisini gormek istersiniz: ");
    scanf("%d", &siradaki);
    
    for (i = 3; i <= siradaki - 1; i++) {
        array[i] = array[i - 1] + array[i - 2];
    }
    
    for (i = 0; i <= siradaki - 1; i++) {
        printf("%d. sayi: %d\n", i + 1, array[i]);
    }
}

// ==========================================
// 2. UYGULAMA: Not Hesaplama (fonk.cpp)
// ==========================================
bool not_hesapla(int vize, int final) {
    float ort;
    ort = vize * 0.4 + final * 0.6;
    printf("Notunuz: %f \n", ort);

    if (ort >= 55)
        return true;
    else
        return false;
}

void topla(int a, int b) {
    printf("Sayilarin toplami %d\n", a + b);
}

void not_hesapla_uygulamasi() {
    int x1, x2;
    printf("Vize notunu gir: ");
    scanf("%d", &x1);
    printf("Final notunu gir: ");
    scanf("%d", &x2);

    if (not_hesapla(x1, x2))
        printf("Tebrikler gectiniz.\n");
    else
        printf("Malesef kaldiniz.\n");
}

// ==========================================
// 3. UYGULAMA: Matris Ýþlemleri (ilk.cpp)
// ==========================================
void matris_bastir(int matris[2][2]) {
    int i, j;
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%d ", matris[i][j]);
        }
        printf("\n");
    }
    printf("--------\n");
}

void matris_islemleri_uygulamasi() {
    printf("--- Matris Islemleri ---\n");
    int m1[2][2] = {{1, 2}, {3, 4}};
    int m2[2][2] = {5, 6, 7, 8};
    int toplam[2][2];
    int carpim[2][2];
    int m3[2][2]; // Transpoz (devrik) için kullanýlacak matris
    int i, j, k, eleman = 0;

    printf("Matris 1:\n");
    matris_bastir(m1);
    printf("Matris 2:\n");
    matris_bastir(m2);

    // Toplama Ýþlemi
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            toplam[i][j] = m1[i][j] + m2[i][j];
        }
    }

    // Çarpma Ýþlemi
    for (i = 0; i < 2; i++) {
        for (k = 0; k < 2; k++) {
            eleman = 0;
            for (j = 0; j < 2; j++) {
                eleman += m1[i][j] * m2[j][k];
            }
            carpim[i][k] = eleman;
        }
    }

    // Transpoz (Yer Deðiþtirme) Ýþlemi
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            m3[i][j] = m2[j][i];
        }
    }

    printf("Carpim Sonucu:\n");
    matris_bastir(carpim);
    
    printf("Matris 2'nin Transpozu:\n");
    matris_bastir(m3);

    printf("Toplam Sonucu:\n");
    matris_bastir(toplam);
}

// ==========================================
// 4. UYGULAMA: Sayý Kontrol (kontrol.cpp)
// ==========================================
void sayi_kontrol_uygulamasi() {
    int sayi;
    printf("Bir sayi giriniz: ");
    scanf("%d", &sayi);
    printf("Girilen sayi: %d\n", sayi);
}

// ==========================================
// 5. UYGULAMA: 2. Dereceden Denklem (newc.cpp)
// ==========================================
void denklem_cozme_uygulamasi() {
    int a, b, c;
    float delta, x1, x2;

    printf("Ikinci dereceden bir bilinmeyenli denklem\n");
    printf("*****************************************\n");
    printf("Katsayilari sirasi ile giriniz (a b c formatinda, ornegin 1 -5 6): ");
    
    // Deðiþkenlerin hafýza adreslerine yazýlabilmesi için '&' eklendi.
    scanf("%d %d %d", &a, &b, &c); 

    // C++'da üs almak için ** kullanýlamaz. (b * b) pratik çözümdür.
    delta = (b * b) - (4 * a * c); 

    if (delta < 0) {
        printf("Delta sifirdan kucuk (Delta = %f). Reel kok yoktur!\n", delta);
    } else {
        // sqrt() fonksiyonu karekök alýr. 
        x1 = (-b - sqrt(delta)) / (2 * a);
        x2 = (-b + sqrt(delta)) / (2 * a);
        printf("x1: %f\n", x1);
        printf("x2: %f\n", x2);
    }
    printf("*****************************************\n");
}

// ==========================================
// ANA FONKSÝYON (MAIN)
// ==========================================
int main() {
    int secim;

    printf("--- C++ MINI PROJELER ARSIVI ---\n");
    printf("1. Fibonacci Hesapla\n");
    printf("2. Vize/Final Notu Hesapla\n");
    printf("3. Matris Islemleri (Carpim, Toplam, Transpoz)\n");
    printf("4. Basit Sayi Kontrolu\n");
    printf("5. 2. Dereceden Denklem Cozucu\n");
    printf("Calistirmak istediginiz programi secin (1-5): ");
    
    scanf("%d", &secim);
    printf("\n");

    // Kullanýcýnýn seçimine göre ilgili fonksiyonu çaðýrýyoruz
    switch (secim) {
        case 1:
            fibonacci_uygulamasi();
            break;
        case 2:
            not_hesapla_uygulamasi();
            break;
        case 3:
            matris_islemleri_uygulamasi();
            break;
        case 4:
            sayi_kontrol_uygulamasi();
            break;
        case 5:
            denklem_cozme_uygulamasi();
            break;
        default:
            printf("Gecersiz bir secim yaptiniz. Lutfen programi yeniden baslatin.\n");
            break;
    }

    return 0;
}
