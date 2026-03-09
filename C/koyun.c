#include <stdio.h>
#include <stdlib.h>

int main() {
    int gen;
    int i, j, k;
    int bacak, bacak2, boyun;
    
    // Kullanıcıdan çizimin boyutunu belirleyecek temel genişlik değerini alıyoruz.
    printf("Koyun genisligi ne olsun? (Cift tam sayi girin)\n");
    scanf("%d", &gen);
    
    // Girilen değeri 2'ye bölerek şeklin oranlarını koruyacak bir temel birim oluşturuyoruz.
    gen = gen / 2;
    printf("\n");
    
    // ==========================================
    // 1. BÖLÜM: BAŞ KISMI
    // ==========================================
    
    // Başın üst sınırını çiziyoruz (Düz bir yıldız satırı)
    for(i = 0; i < gen; i++) {
        printf("*");
    }
    printf("\n");
    
    // Başın orta kısmını çiziyoruz (Kenarlarda yıldız, ortada boşluk)
    for(i = 2; i < gen; i++) {
        printf("*"); // Sol kenar
        for(j = 2; j < gen; j++) {
            printf(" "); // İç boşluk
        }
        printf("*\n"); // Sağ kenar ve alt satıra geçiş
    }
    printf("\n");
    
    // Başın alt sınırını çiziyoruz (Düz bir yıldız satırı)
    for(i = 0; i < gen; i++) {
        printf("*");
    }
    printf("\n");


    // ==========================================
    // 2. BÖLÜM: BOYUN KISMI
    // ==========================================
    
    // Boynun başa göre nerede konumlanacağını hesaplıyoruz (genişliğin yarısı)
    boyun = gen * 0.5;
    
    // Boynun dikey kısmını çiziyoruz
    for(i = 1; i < gen; i++) {
        for(j = 0; j < gen; j++) {
            if (j == boyun) {
                printf("*"); // Sadece boyun hizasına denk gelince yıldız koy
            } else {
                printf(" "); // Diğer yerleri boş bırak
            }
        }
        printf("\n");
    }
    
    // Boynu gövdeye bağlayan yatay kısmı çiziyoruz
    for(i = 0; i < gen; i++) {
        if (i >= boyun) {
            printf("*"); // Boyun hizasından başlayarak sağa doğru çiz
        } else {
            printf(" "); // Sol tarafı boş bırak
        }
    }
    printf("\n");   
    
    // ==========================================
    // 3. BÖLÜM: GÖVDE (VÜCUT) KISMI
    // ==========================================
    
    // Gövde, baştan ve boyundan daha sağda başlamalı. 
    // Bu yüzden önce boşluk bırakıp sonra yıldızlardan oluşan bir blok çiziyoruz.
    for(i = 0; i < gen * 2; i++) { // Gövdenin yüksekliği
        for(k = 0; k < gen; k++) {
            printf(" "); // Gövdeyi sağa kaydırmak için baştaki boşluklar
        }
        for(j = 0; j < gen * 2; j++) {
            printf("*"); // Gövdenin genişliği kadar yıldız bas
        }
        printf("\n");
    }
    
    // ==========================================
    // 4. BÖLÜM: BACAKLAR
    // ==========================================
    
    // Bacaklar arası mesafeyi belirliyoruz (genişliğin %40'ı)
    bacak2 = gen * 0.4;
    bacak = bacak2;
    
    for(j = 0; j < gen * 2; j++) { // Bacakların yüksekliği (Gövde ile aynı oranda)
        
        for (k = 0; k < gen; k++) {
            printf(" "); // Bacakların gövde hizasından başlaması için soldan boşluk bırak
        }
        
        for(i = 0; i < gen * 2; i++) {
            // Eğer mevcut konum bacak hizasına geldiyse yıldız bas
            if(i == bacak) {
                printf("*");
                bacak += bacak2; // Bir sonraki bacağın konumunu hesapla
            } else {
                printf(" ");
            }
        }
        printf("\n");
        
        // Alt satıra geçerken bacak konumlayıcıyı tekrar sıfırla/başlangıca getir
        bacak = gen * 0.4; 
    }
    
    return 0;
}