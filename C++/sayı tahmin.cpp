#include <stdio.h>

int main() {
    // Tahmin edilmesi gereken gizli sayi
    int sayi = 74;
    
    // Kullanicinin toplam tahmin hakki ve dongu sayaci
    int hak = 5, i;
    
    // Kullanicinin girdigi deger ve gecerli tahmin araliginin sinirlari
    int tahmin, min_aralik = 0, max_aralik = 100;
    
    printf("0-100 ARASINDAKI SAYIYI TAHMIN ET\n");
    printf("---------------------------------\n");
    
    // Kullaniciya verdigimiz hak kadar donecek ana oyun dongusu
    for(i = 1; i <= hak; i++) {
        printf("Bir sayi tahmin et: ");
        scanf("%d", &tahmin);
        
        // Girilen degerin mevcut min ve max araliginda olup olmadigini kontrol ediyoruz
        if (tahmin < max_aralik && tahmin > min_aralik) {
            
            if (tahmin > sayi) {
                // Eger tahmin gizli sayidan buyukse, ust siniri (max_aralik) asagi cekiyoruz
                max_aralik = tahmin;
                printf("Daraltilan aralik: %d - %d \n", min_aralik, max_aralik);
                printf("Kalan hakkin: %d\n\n", (hak - i));
            } 
            else if (tahmin < sayi) {
                // Eger tahmin gizli sayidan kucukse, alt siniri (min_aralik) yukari cekiyoruz
                min_aralik = tahmin;
                printf("Daraltilan aralik: %d - %d \n", min_aralik, max_aralik);
                printf("Kalan hakkin: %d\n\n", (hak - i));	
            } 
            else {
                // Tahmin tam olarak gizli sayiya esitse donguden cikis yapiyoruz
                printf("\nTebrikler, dogru bildin! Sayi: %d\n", tahmin);
                break;
            }
            
        } else {
            // Kullanici belirlenen aralik disinda bir deger girerse hakkini eksiltmiyoruz (i--)
            printf("\nLutfen sadece gecerli aralikta (%d - %d) tahmin yapin!\n\n", min_aralik, max_aralik);
            i--; // Gecersiz giris oldugu icin dongu sayacini bir geri aliyoruz
        }
    }
    
    // Dongu bittikten sonra eger kullanicinin son tahmini hala sayiyla eslesmiyorsa oyunu kaybetmistir
    if (tahmin != sayi) {
        printf("\nKAYBETTIN! :(\nDogru sayi %d olacakti.\n", sayi);
    }
    
    return 0;
}
