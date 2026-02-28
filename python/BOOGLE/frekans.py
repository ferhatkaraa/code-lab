#kelimelerin frekans değerlerini harflere indirgeyecek 
# daha sonra tüm kelimelerdeki harflerin frekans değererinin 
# aynı harflere ait olanları toplanacak
#sonuç bir listede saklanacak

print("oyun yükleniyor...")
global gecici_liste
#kelime listesi okutulur
with open("data.txt","r",encoding="utf-8") as file:
    #geçici bir liste elemanına aktarılır
    gecici_liste = file.readlines()
    
    
 #bir harf:frekans sözlüğü oluşturulur   
harf_frekans = dict()
 
 
    
#for döngüsü ile her satırdaki frekans değeri harflere atanır
#dahasonra eğerr bir harf tekrar ediyorsa eski değerine eklenir
for i in gecici_liste:
    #kelime ile frekans değeri arasındaki boşluktan faydalanarak iki parçaya bölünür
    kelime_frekans = i.split(" ")
    #ilk eleman üzerinde bir for döngüsü daha başlatılır her bir harfe frekans değeri atanır ve sözlük yapıları ile saklanır
    for j in kelime_frekans[0]:
        j = j.lower()
        if j not in harf_frekans.keys():
            #harf frekans kaydı alınır
            harf_frekans[j] = int(kelime_frekans[1])
        else:
            #tekrar eden harf durumlarında frekans üzerine eklenir
            harf_frekans[j] = harf_frekans[j] + int(kelime_frekans[1])



#frekans değerleri ortak bir sayıya bölünerek bekleme süresi düşürülür
for i,j in harf_frekans.items():
    harf_frekans[i] = j // 100000





 #yaklaşık 8 saniyede frekans değerlerini hazırlıyor.
 
 #harfler frekanslarına göre bir string üzerinde toparlanacak
frekans_string = ""
for i,j in harf_frekans.items():
    frekans_string += i*j
 

 
 
