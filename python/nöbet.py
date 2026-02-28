import random
import pandas as pd
import time




myylist = [
    "Ali", "Ayşe", "Mehmet", "Zeynep", "Can", 
    "Elif", "Mert", "Hülya", "Yusuf", "Fatma",
    "Emre", "Gizem", "Efe", "Derya", "Deniz", 
    "Kaan", "Melis", "Burak", "Selin","ferhat", 
    "Hande"
]
mylist = range(27)
class nöbet:
    
    #belirli bir ayın hafta içi hafta sonu bilgisi ve nöbetçi öğrenci listesi eklendi
    #grupdict ise fonksiyonlar içerisinde düzenlenerek elden ele gezdirilen dict yapısını taşır 
    # ve en son hangi fonksiyonun müdahale ettiğini belirtir
    def __init__(self):
        self.weekday = 21
        self.weekend = 9
        self.nlist =myylist
        self.grupdict = ["init",self.nlist]
    
    #kişi başına ortalama düşmesi gereken nöbet saatini hesaplar
    def ortnöbet(self):
        return round(2*(self.weekday*15+self.weekend*24)/len(self.nlist))
    #her gün iki nöbet vardır tüm hafta sonu nöbet slotları bitene kadar dağıtılır
    #fazladan hafta sonu nöbeti alanlara denk sayılabilecek 2 hafta içi nöbetini de ek hafta sonu nöbeti alamayanlara verdik
    #kalan hafta içi nöbet slot sayısı bulunur
    def artik_bul(self):
        return self.weekday*2 - (len(self.nlist) - (self.weekend*2)%len(self.nlist))*2
    #en adil olacak şekilde kişi sayısını farklı nöbet türlerine ayırdık
    def grup_böl(self):
        grup_dict = {
            "0/0":[self.artik_bul()//len(self.nlist),(self.weekend*2)//len(self.nlist)],
            "0/+":(self.weekend*2)%len(self.nlist),
            "++/0":len(self.nlist) - (self.weekend*2)%len(self.nlist),
            "+/+":None,
            "+++/0":None
        }
        if (self.artik_bul()%len(self.nlist))/((self.weekend*2)%len(self.nlist)) <= 1:
            grup_dict["+/+"] = self.artik_bul()%len(self.nlist)
            grup_dict["+++/0"] = 0
        else:
            grup_dict["+/+"] = (self.weekend*2)%len(self.nlist)
            grup_dict["+++/0"] = (self.artik_bul()%len(self.nlist))-((self.weekend*2)%len(self.nlist))
        grup_dict["0/+"] -= grup_dict["+/+"]
        grup_dict["++/0"] -= grup_dict["+++/0"]
        
        return grup_dict
    #grup böl fonksiyonundaki gruplarda bulunan sayılara göre
    # self.nlist elemanlarını gruplara rastgele paylaştırır
    def sec(self):
        mydict = self.grup_böl()
        newlist = self.nlist
        for j,k in mydict.items():
            if j == "0/0":
                continue
            mydict[j] = random.sample(newlist,k=mydict[j])
            newlist = [i for i in newlist if i not in mydict[j]]
        print("seçilmeyen kişiler",newlist)
        self.grupdict = ["sec",mydict]
    #grupböl fonksiyonunda tek sayı çıkan gruplardaki elemanları manuel işlemek gerekiyor
    #önce manuel girmek gereken elemanları artan dict içinde toparlıyoruz
    #eğer 3 veya 0 artan eleman varsa düzenlenebiliyor
    #eğer daha farklı sayıda ise bazı grupların bozulması gerekebilir
    #bu yüzden kullanıcıdan ek olarak eleman isteği sorulur
    #daha sonra kalan elemanlar gruplandırılır manuel olanlar kullanıcıya bırakılır
    #daha sonra manuel olmayan elemanlar ikili guruplar haline dönüştürülür
    #elemanlar katsayıları ile çarpılarak sayıları artırılır
    #return olarak hem düzenlenenler hem de artanlar liste halinde veriliyor
    def grupla(self):
        newdict = self.grupdict[1]
        artan = {"0/0":self.grup_böl()["0/0"]}
        for i in newdict.keys():
            if len(newdict[i]) % 2 == 1:
                artan[i] = random.choice(newdict[i])
                newdict[i].remove(artan[i])
            
        if len(artan.keys()) != 4 and len(artan.keys()) != 1:
            print("bu kişi veya kişiler manuel girilecek")
            for i,j in artan.items():
                print(i,j)
            while True:
                print("hangi gruptan iki öğrenciyi manuel girmek istersin?") 
                for i in newdict.keys():
                    print(list(newdict.keys()).index(i)+1,i) 
                print("q gerek yok")      
                mysec = input("seç:")
                if mysec in [str(i) for i in range(1,len(list(newdict.keys()))+1)]:
                    if self.grup_böl()[list(newdict.keys())[int(mysec)-1]] // 2 == 0:
                        print("seçtiğiniz grupta yeterince eleman yok\nlütfen başka bir grup seçin")
                        continue
                    try:
                        eleman = artan[list(newdict.keys())[int(mysec)-1]]
                        artan[list(newdict.keys())[int(mysec)-1]] = newdict[list(newdict.keys())[int(mysec)-1]][:2] + [eleman]
                    except:
                        artan[list(newdict.keys())[int(mysec)-1]] = newdict[list(newdict.keys())[int(mysec)-1]][:2]
                    newdict[list(newdict.keys())[int(mysec)-1]] = newdict[list(newdict.keys())[int(mysec)-1]][2:]
                    break
                elif mysec == "q":
                    print("mevcut manuel girilecek kişilere ekleme yapılmadı")
                    break
                else:
                    print("lütfen geçerli bir değer gir.")                    
            
            
        for i,j in newdict.items():
           if i == "0/0":
               continue
           newdict[i] = random.shuffle(newdict[i])
           newdict[i] = [(newdict["0/0"][0] + i[:i.find("/")].count("+"))*list(zip(j[::2], j[1::2])) ,(newdict["0/0"][1] + i[i.find("/"):].count("+"))*list(zip(j[::2], j[1::2])) ]   
        
        
                              
            
        print("manuel girilecek olan kişiler ")
        for i,j in artan.items():
            print(i,j)
        self.grupdict = ["grupla",newdict,artan] 
    
    #artan kişiler bastırılırmanuel istenirse kullanıcı istenen formatta kalan kullanıcıları girer
    #otomatik istenirse bilgisayar çok iyi olmayan bir yöntemle hesaplamayı dener
    #son durumda hazırlanan elemanlarself.grupdict ile gönderilir
    def manuelekle(self):
        artan = self.grupdict[2]
        for i,j in artan.items():
            print(i,j)
        while True:
            setgrup = input("nasıl ayarlansın?\n1-manuel ayarla\n2-otomatik ayarlansın")
            if setgrup == "1":
                print(artan["kişiler"])
                try:
                    wkd = input("hafta içi gruplarını gir\nformat şu şekildedir\n(ali,ahmet)-(ayşe,mehmet)-(cengiz,salih)")
                    wkd = wkd.split("-")
                    if len(wkd) != artan["haftaiçi"]:
                        print("lütfen size verilen hafta içi gün sınırlamasına uyun")
                        continue
                    wke = input("hafta sonu gruplarını gir\nformat şu şekildedir\n(ali,ahmet)-(ayşe,mehmet)-(cengiz,salih)")
                    wke = wke.split("-")
                    if len(wke) != artan["haftasonu"]:
                        print("lütfen size verilen hafta sonu gün sınırlamasına uyun")
                        continue
                    break
                except Exception as e:
                     print("lütfen manuel eklemeyi doğru formatta yazın",e)  
                     continue
                break
            elif setgrup == "2":
                fl = [[],[],[],[]]
                for i,j in artan["kişiler"].items():
                    if type(j) == list:
                        for k in j:
                            fl[0].append(k)
                            fl[1].append(int(i[i.find(":")+1]))
                            fl[2].append(k)
                            fl[3].append(int(i[i.rfind(":")+1]))
                    else:    
                        fl[0].append(j)
                        fl[1].append(int(i[i.find(":")+1]))
                        fl[2].append(j)
                        fl[3].append(int(i[i.rfind(":")+1]))
                wkd = []
                wke = []
                while True:
                    print("hesaplanıyor...")
                    if time.time() % 5 == 0:
                        print("hesaplanıyor...")
                    if len(wkd) != artan["haftaiçi"]:
                        örnek = random.sample(fl[0],counts=fl[1],k=2)
                        if örnek[0] == örnek[1]:
                            continue
                        wkd.append(örnek)
                        fl[1][fl[0].index(örnek[0])] -= 1
                        fl[1][fl[0].index(örnek[1])] -= 1
                    elif len(wke) != artan["haftasonu"]:
                        örnek = random.sample(fl[2],counts=fl[3],k=2)
                        wke.append(örnek)
                        fl[1][fl[2].index(örnek[0])] -= 1
                        fl[1][fl[2].index(örnek[1])] -= 1
                    else:break
                break
            else:
                print("lütfen 1 ya da 2 giriniz.\a")
        self.grupdict = ["manuelekle",self.grupdict[1],artan,wkd,wke]
        print("sonradan ayarlanan gruplar")
        print("haftaiçi:",wkd)
        print("hafta sonu",wke)


    #manueller ayrıldıktan sonra elemanların hafta içi ve hafta sonu guruplandırılması yapılır 
    # artan elemanlar manuelekle fonksiyonundan hazır gelir  ve weekdaylist ve weeekendliste eklenir
    #ayın ilk günü sorulur ve pandas tablosu hazırlanır
    #satırlar eşit olması gerektiği için eksik satırlara none yazılır
    #pandas tablosu oluşturulur ve excell olarak bastırılır
    # kaç adet gurup olduğu ve guruplar bastırılır
    def tablo(self):
        weekdaylist = list()
        weekendlist = list()
        for i,j in self.grupdict[1].items():
            if i == "0/0":
                continue
            weekdaylist += j[0]
            weekendlist += j[1]
        kalan = {"haftaiçi":self.weekday-len(weekdaylist),
            "haftasonu":self.weekend-len(weekendlist),
            "kişiler":{}
        }
        for i,j in self.grupdict[2].items():
            if i == "0/0":
                continue
            kalan["kişiler"][f"hafta içi:{i[:i.find("/")].count("+")+self.grupdict[2]["0/0"][0]}-hafta sonu:{i[i.find("/"):].count("+")+self.grupdict[2]["0/0"][1]}"] = j
        self.grupdict = ["tablo",self.grupdict[1],kalan]
        self.manuelekle()
        weekdaylist += self.grupdict[3]
        random.shuffle(weekdaylist)
        weekendlist += self.grupdict[4]
        random.shuffle(weekendlist)
        hafta = ["pazartesi","salı","çarşamba","perşembe","cuma","cumartesi","pazar"]
        askday = None
        while askday not in hafta:
            askday = input("düzenlemiş olduğunuz aylık nöbet listesinin ilk günü yani ayın biri hangi güne denk gelmektedir?\nNOT:yazım hatası yapmamaya dikkat edin").lower()
        hafta = hafta[hafta.index(askday):] + hafta[:hafta.index(askday)]
        personlist = [[],[],[],[],[]] 
        for i in personlist:
            for j in hafta:
                try:
                    if j in ["cumartesi","pazar"]:
                        i.append(weekendlist[0])
                        weekendlist.pop(0)
                    else: 
                        i.append(weekdaylist[0])
                        weekdaylist.pop(0)
                except Exception as e:
                    print("none",e)
                    i.append("none")
        df = pd.DataFrame(personlist, columns=hafta)
        df.to_excel("nöbet-listesi.xlsx",index=False,sheet_name="nöbet listesi")
        print("unutulan değerler")
        print(weekdaylist,len(weekdaylist),sep="\n")
        print(weekendlist,len(weekendlist),sep="\n")
    
   
    






    def run(self):
        self.sec()
        self.grupla()
        self.tablo()








a = nöbet()
for i,j in a.grup_böl().items():
    print(i,j)

a.run()


    

    

    
