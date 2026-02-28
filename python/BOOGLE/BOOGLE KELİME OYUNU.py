#bu bütün modüllerin birleşim kümesi olacak
#oyun bu sayfa üzerinde oynanacak
import frekans
import tahta
import kontroller
import time





#oyuncunun ismi alınır eğer yazmazsa default olarak isim olarak oyuncu atanır
print("BOOGLE KELİME OYUNU")
oyuncu = input("hoş geldiniz\nlütfen adınızı girin\noyuncu:")
if len(oyuncu) == 0:
    oyuncu = "oyuncu"
print("bilgileriniz işleniyor...")
print("NOT:oyunumuzda 60 saniye içerisinde tabloda bulabildiğiniz kadar kelime bulacaksınız.")


#tablo verilir her deneme ardından doğru olup olmadığı güncel puan ve güncel kalan süre görüntülenir 
#süre biterse tekrar oynamak istenip istenmediği sorulur istenirse puan ve süre sıfırlanır oyun bir tur daha oynanır
kalan_süre = 60
puan = 0
oyun = True
while oyun == True:
    harf_tablosu = tahta.tablo_hazırla(tahta.harf_üret(frekans.frekans_string))
    if kontroller.tahta_kontrol(harf_tablosu,frekans.gecici_liste) == False:
        continue
    while True:
        print(puan)
        tahta.tablo_yazdır(harf_tablosu)
        baslama_zamanı = time.time()
        print(f"kalan süre:{int(kalan_süre)}")
        oyuncunun_kelimesi = input("tahtada gördüğün kelimeyi gir:")
        #burada puanlama fonksiyonuna kelime kontrol fonksiyonu parametre olarak verilir
        puan = kontroller.puanla(kontroller.kelime_kontrol(oyuncunun_kelimesi,harf_tablosu,frekans.gecici_liste,kontroller.A),puan,oyuncunun_kelimesi)
        bitis_zamanı = time.time()
        #her hamleden sonra kalan süreyi hesaplar
        kalan_süre = kontroller.zaman_kontrol(baslama_zamanı,bitis_zamanı,kalan_süre)
        if kalan_süre <= 0:
            print(f"oyun bitti\n{oyuncu}:{puan}\nTEBRİKLER")
            time.sleep(2)
            break
    while True:    
        oyun = input("tekrar oynamak ister misin?\n1-devam\n2-hayır teşekkürler") 
        if oyun == "1" or oyun == "devam" or oyun == "evet":
            print("oyun hazırlanıyor...")
            oyun = True
            kalan_süre = 60
            puan = 0
            break
        elif oyun == "2" or oyun == "hayır" or oyun == "hayır teşekkürler" or oyun =="hayir":
            print(f"güzel oyundu {oyuncu} görüşmek üzere❤️")
            oyun = False
            break
        else:
            print("bir seçim belirtmediniz")


