

#kontrol fonksiyonları burada olacak
#zaman kontrol fonksiyonu
#tahtanın içinde en az 25 kelime mevcut mu fonksiyonu
#yazılan kelime kurallara uyularak yazıldı mı fonksiyonu
#kelime doğru mu fonksiyonu

#bu fonksiyon her hamleden sonra kalan süreyi hesaplar
def zaman_kontrol(basla,bit,kalan):
    kalan -= (bit - basla)
    return kalan


#puanlama fonksiyonu parametresi doğru ise puan ekler yanlış ise puan eksiltir
def puanla(kelime,mevcut_puan,girilen_kelime):
    if kelime == True:
        print("doğru cevap")
        if len(girilen_kelime) <4:
            return mevcut_puan + 5
        else:
            return mevcut_puan + (2 + len(girilen_kelime))
    elif kelime == False:
        print("yanlış cevap")
        return mevcut_puan - 3
    else:
        return mevcut_puan




#bu fonksiyon tahtadan en az 25 kelime çıkıp çıkmadığını kontrol eder eğer çıkmazsa tahtayı yeniler
def tahta_kontrol(harf_tablosu:list,kıyas_listesi:list):
    #bu döngüde 32 ayrı string gurubu kurulur ve sonra bu guruptan en az 25 tane uyumlu kelime çıkıp çıkmadığına bakılır
    global A
    global string_kontrol
    string_kontrol = ""
    for i in range(4):
        for j in range(4): 
            string_kontrol +=  harf_tablosu[i][j]
        string_kontrol += " "
    for i in range(4):
        for j in range(4): 
            string_kontrol +=  harf_tablosu[j][i]
        string_kontrol += " "
    for i in range(4):
        for j in range(4):
            if i < 2 and j < 2:
                while i != 3 or j != 3:
                    string_kontrol += harf_tablosu[i][j]
                    if i != 3:
                        i += 1
                    string_kontrol += harf_tablosu[i][j]
                    if j != 3:
                        j += 1
                    string_kontrol += harf_tablosu[i][j]
            elif i < 2 and j > 1:
                while i != 3 or j != 0:
                    string_kontrol += harf_tablosu[i][j]
                    if i != 3:
                        i += 1
                    string_kontrol += harf_tablosu[i][j]
                    if j != 0:
                        j -= 1
                    string_kontrol += harf_tablosu[i][j]
            elif i > 1 and j < 2:
                while i != 0 or j != 3:
                    string_kontrol += harf_tablosu[i][j]
                    if i != 0:
                        i -= 1
                    string_kontrol += harf_tablosu[i][j]
                    if j != 3:
                        j += 1
                    string_kontrol += harf_tablosu[i][j]
            elif i > 1 and j > 1:
                while i != 0 or j != 0:
                    string_kontrol += harf_tablosu[i][j]
                    if i != 0:
                        i -= 1
                    string_kontrol += harf_tablosu[i][j]
                    if j != 0:
                        j -= 1
                    string_kontrol += harf_tablosu[i][j]
            string_kontrol += " "
    string_kontrol += string_kontrol[::-1]
    A = string_kontrol
    kelime_sayısı = 0
    for i in kıyas_listesi:
        if i[:i.find(" ")] in string_kontrol or i[:i.find(" "):-1] in string_kontrol:
            kelime_sayısı += 1
    if kelime_sayısı >= 25:
        return True
    else:
        return False

global kelime_listesi
kelime_listesi = list()
#bu fonksiyon yazılan kelimenin tahtadki mevcut kelimelerden olup olmadığına ve kurallara uygun yazılmasına bakar daha sonra bir bool döndürür
#önce kelimenin yazmının kurala uygunluğu daha sonra da datada mevcut olup olmadığı kontrol edilir
#girilen eski kelimelerden puan kırılmaz
def kelime_kontrol(girilen_kelime,aratılan_tablo:list,data:list,kelime_analizi):
    #tahtadan böyle bir kelime yazımı mümkün müdür kontrolü
    #data ile uyum kontrol edilir
    if len(girilen_kelime) == 0:
        return "kelime girilmedi"
    girilen_kelime = girilen_kelime.lower()
    if girilen_kelime not in kelime_listesi:
        kelime_listesi.append(girilen_kelime)
    else:
        print("bu kelime daha önce yazıldı")
        return "Tekrar hatası"
    for i in data:
        if girilen_kelime == i[:i.find(" ")] or girilen_kelime == i[:i.find(" "):-1]:
            for i in range(len(girilen_kelime)-1):
                if girilen_kelime[i:i+2] in kelime_analizi:
                    continue
                else:
                    return False
            return True
        else:
            continue
    return False    



