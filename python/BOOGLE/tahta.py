import random
#frekanslardan faydalanılarak 16'lıharf tablolarının harf üretme fonksiyonu yazılacak
#randımize oluşturulan harfler tabloya eklenecek







def harf_üret(frekans_string):
    #shuffle fonksiyonu için frekans stringi listeye çevilir
    frekans_string = list(frekans_string)
    random.shuffle(frekans_string)
    return frekans_string




#rastgele harfler ile 4x4 tablo hazırlama
def tablo_hazırla(frekans_listesi):
    tablo = []
    for i in range(4):
        satır = [random.choice(frekans_listesi) for i in range(4)]
        tablo.append(satır)
    return tablo

#tablonun ekrana bastırılması
def tablo_yazdır(tablo_matrisi:list):
    print("***************",flush=True)
    for i in tablo_matrisi:
        for j in i:
            print(end="|")
            print(f"{j}",end="|")
        print()
    print("***************",flush=True)
 
 
