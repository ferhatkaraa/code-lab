import tkinter as p
import random
import time
pencere1 = p.Tk()
pencere1.title("TAŞ KAĞIT MAKAS")
pencere1.geometry("2000x900")
pencere1.config(bg="#e6e6fa",highlightbackground="red",highlightthickness=5)

resim = p.PhotoImage(file="tkm.png")
tresim = p.PhotoImage(file="tas.png")
kresim = p.PhotoImage(file="kağıt.png")
mresim = p.PhotoImage(file="makas.png")
tresim.configure(palette=0,gamma=0,height=200,width=300)
kresim.configure(palette=0,gamma=0,height=200,width=300)
mresim.configure(palette=0,gamma=0,height=200,width=300)
res = p.Label(bg="#e6e6fa")
res.place(relx=0.3,rely=0.4,relwidth=0.2,relheight=0.2)
pencere1.iconphoto(False,resim)
çer1 = p.Frame(pencere1,background="#6495ed")
çer1.place(relx=0.8,relwidth=0.2,rely=0,relheight=1)
çer2 = p.Frame(pencere1,background="#607b8b")
çer2.place(rely=0.6,relheight=0.4,relx=0,relwidth=0.8)
Oyuncu1 = "Oyuncu1"
Oyuncu2 = "Oyuncu2"
puan1 = 0
puan2 = 0
et1 = p.Label(highlightbackground="#aa33aa",highlightthickness=10,background="#cd5c5c",text="{}".format(Oyuncu1),font="verdana 30 bold")
et1.place(relx=0.03,rely=0.05,relwidth=0.35,relheight=0.35)
et2 = p.Label(highlightbackground="#aa33aa",highlightthickness=10,background="#cd5c5c",text="{}".format(Oyuncu2),font="verdana 30 bold")
et2.place(relx=0.41,rely=0.05,relwidth=0.35,relheight=0.35)
boş1 = "---"
boş2 = "---"
et15 = p.Label(background="#cd5c5c",text="{}".format(boş1),font="verdana 30 bold")
et15.place(relx=0.12,rely=0.25,relwidth=0.15,relheight=0.15)
et25 = p.Label(background="#cd5c5c",text="{}".format(boş2),font="verdana 30 bold")
et25.place(relx=0.51,rely=0.25,relwidth=0.15,relheight=0.15)


p.Label(pencere1,text="sonuçlar",font="15",background="#6495ed").place(relx=0.81,relwidth=0.18,rely=0,relheight=0.05)

et35 = p.Label(bg="#e6e6fa",text="oynama sırası",font="15")
et35.place(relx=0.55,rely=0.4,relwidth=0.1,relheight=0.05)
et3 = p.Label(bg="#e6e6fa",text="------",font="15")
et3.place(relx=0.55,rely=0.45,relwidth=0.1,relheight=0.05)

sonuç = p.LabelFrame(çer1,text="{}:{}\n{}:{}".format(Oyuncu1,puan1,Oyuncu2,puan2),bg="#7fffd4",font="verdana 20 bold")
sonuç.place(relx=0.15,relheight=0.51,rely=0.06,relwidth=0.7)
isim1 = p.Text(font="15")
isim1.place(relx=0.03,rely=0,relwidth=0.2,relheight=0.05)
isim2 = p.Text(font="15")
isim2.place(relx=0.41,rely=0,relwidth=0.2,relheight=0.05)
isbuton1 =p.Button(font="15",bg="grey",fg="black",text="değiştir")
isimhak = 1
def isim():
    if isimhak == 1:
        et1.config(text=isim1.get(1.0,p.END))
        global Oyuncu1
        Oyuncu1 = isim1.get(1.0,p.END)
        sonuç.config(text="{}:{}\n{}:{}".format(Oyuncu1,puan1,Oyuncu2,puan2))
def risim():
    if isimhak == 1:
        et2.config(text=isim2.get(1.0,p.END))
        global Oyuncu2
        Oyuncu2 = isim2.get(1.0,p.END)
        sonuç.config(text="{}:{}\n{}:{}".format(Oyuncu1,puan1,Oyuncu2,puan2))
isbuton1.config(command=isim)



isbuton1.place(relx=0.24,rely=0,relwidth=0.1,relheight=0.04)
isbuton2 =p.Button(font="15",bg="grey",fg="black",text="değiştir")
isbuton2.place(relx=0.62,rely=0,relwidth=0.1,relheight=0.04)
isbuton2.config(command=risim)
tbuton = p.Button(çer2,bg="#8b4513",fg="white",font="verdana 40 bold",text="TAŞ")
tbuton.place(relx=0.01,rely=0.1,relwidth=0.32,relheight=0.8)
kbuton = p.Button(çer2,bg="#8b4513",fg="white",font="verdana 40 bold",text="KAĞIT")
kbuton.place(relx=0.34,rely=0.1,relwidth=0.32,relheight=0.8)
mbuton = p.Button(çer2,bg="#8b4513",fg="white",font="verdana 40 bold",text="MAKAS")
mbuton.place(relx=0.67,rely=0.1,relwidth=0.32,relheight=0.8)
seç = p.IntVar()
kişi1 = p.Radiobutton(variable=seç,value=1,bg="#e6e6fa",text="bilgisayara karşı oyna",fg="black",font="15")
kişi1.place(relx=0.05,relwidth=0.15,rely=0.4,relheight=0.1)
kişi2 = p.Radiobutton(variable=seç,value=0,bg="#e6e6fa",text="arkadaşınla karşı oyna",fg="black",font="15")
kişi2.place(relx=0.05,relwidth=0.15,rely=0.5,relheight=0.1)
hamle = ""
kullan = 3
def taş():
    global boş1
    global boş2
    et25["text"] = "-???-"
    if kullan == 1:
        if et3["text"] == Oyuncu1:
            boş1 = "TAŞ"
            et15["text"] = boş1
            et3["text"] = Oyuncu2
            if et3["text"] == Oyuncu2:
                if random.randint(1,3) == 1:
                    boş2 = "TAŞ"
                elif random.randint(1,4) == 2:
                    boş2 = "KAĞIT"
                elif random.randint(1,4) == 3:
                    boş2 = "MAKAS"
                et25["text"] = boş2
                et3["text"] = Oyuncu1
    elif kullan == 0:
        if et3["text"] == Oyuncu1:
            boş1 = "TAŞ"
            et15["text"] = "-???-"
            et3["text"] = Oyuncu2
        elif et3["text"] == Oyuncu2:
            boş2 = "TAŞ"
            et15["text"] = boş1
            et25["text"] = boş2
            et3["text"] = Oyuncu1
    if kullan != 3 and kullan != 4:
        oyun()
def kağıt():
        global boş1
        global boş2
        et25["text"] = "-???-"
        if kullan == 1:
            if et3["text"] == Oyuncu1:
                boş1 = "KAĞIT"
                et15["text"] = boş1
                et3["text"] = Oyuncu2
                if et3["text"] == Oyuncu2:
                    if random.randint(1,3) == 1:
                        boş2 = "TAŞ"
                    elif random.randint(1,4) == 2:
                        boş2 = "KAĞIT"
                    elif random.randint(1,4) == 3:
                        boş2 = "MAKAS"
                    et25["text"] = boş2
                    et3["text"] = Oyuncu1
        elif kullan == 0:
            if et3["text"] == Oyuncu1:
                boş1 = "KAĞIT"
                et15["text"] = "-???-"
                et3["text"] = Oyuncu2
            elif et3["text"] == Oyuncu2:
                boş2 = "KAĞIT"
                et15["text"] = boş1
                et25["text"] = boş2
                et3["text"] = Oyuncu1
        if kullan != 3 and kullan != 4:
            oyun()
def makas():
        global boş1
        global boş2
        et25["text"] = "-???-"
        if kullan == 1:
            if et3["text"] == Oyuncu1:
                boş1 = "MAKAS"
                et15["text"] = boş1
                et3["text"] = Oyuncu2
                if et3["text"] == Oyuncu2:
                    if random.randint(1,3) == 1:
                        boş2 = "TAŞ"
                    elif random.randint(1,4) == 2:
                        boş2 = "KAĞIT"
                    elif random.randint(1,4) == 3:
                        boş2 = "MAKAS"
                    et25["text"] = boş2
                    et3["text"] = Oyuncu1
        elif kullan == 0:
            if et3["text"] == Oyuncu1:
                boş1 = "MAKAS"
                et15["text"] = "-???-"
                et3["text"] = Oyuncu2
            elif et3["text"] == Oyuncu2:
                boş2 = "MAKAS"
                et15["text"] = boş1
                et25["text"] = boş2
                et3["text"] = Oyuncu1
        if kullan != 3 and kullan != 4:
            oyun()
tbuton.config(command=taş)
kbuton.config(command=kağıt)
mbuton.config(command=makas)


def oyun():
    global isimhak
    global Oyuncu1
    global Oyuncu2
    global puan1
    global puan2
    global hamle
    global kullan
    if kullan == 3:
        kullan = seç.get()
    if et3["text"] == "------":
        et3["text"] = Oyuncu1
        isimhak = 0
    if kullan == 4:
        sıfırla()
    if et15["text"] != "---" and et25["text"] != "---" and et25["text"] != "-???-":
        hamle += boş1 + "-" + boş2 + "\n"
        if boş1 == "TAŞ" and boş2 == "KAĞIT":
            puan2 += 1
            res["image"] = kresim
        elif boş2 == "TAŞ" and boş1 == "KAĞIT":
            puan1 += 1
            res["image"] = kresim
        elif boş1 < boş2:
            puan2 += 1
            if boş2 == "TAŞ":
                res["image"] = tresim
            elif boş2 == "MAKAS":
                res["image"] = mresim
        elif boş1 > boş2:
            puan1 += 1
            if boş1 == "TAŞ":
                res["image"] = tresim
            elif boş1 == "MAKAS":
                res["image"] = mresim
        sonuç["text"] = "{}:{}\n{}:{}\n{}".format(Oyuncu1,puan1,Oyuncu2,puan2,hamle)
        if abs(puan1 - puan2) > 1:
                if puan1 >= 5 or puan2 >= 5:
                    et35["text"] = "\2 VE KAZANAN...\2"
                    if puan1 > puan2:
                        et3["text"] = Oyuncu1
                    elif puan2 > puan1:
                        et3["text"] = Oyuncu2
                    kullan = 4
                    başlabuton.config(text="Yeniden Oyna")
                    et15["text"] = "-???-"
                    et25["text"] = "-???-"
                    
def sıfırla():
    global isimhak
    global Oyuncu1
    global Oyuncu2
    global puan1
    global puan2
    global kullan
    global hamle
    isimhak = 1
    et35["text"] = "Oynama Sırası"
    et3["text"] = "------"
    et15["text"] = "---"
    et25["text"] = "---"
    puan1 = 0
    puan2 = 0    
    isim1.delete(1.0,p.END)
    isim2.delete(1.0,p.END)
    isim()
    risim()
    Oyuncu1 = "Oyuncu1"
    Oyuncu2 = "oyuncu2"
    et1["text"] = Oyuncu1
    et2["text"] = Oyuncu2
    hamle = ""
    kullan = 3
    sonuç["text"] = "{}:{}\n{}:{}".format(Oyuncu1,puan1,Oyuncu2,puan2)
    başlabuton.config(text="BAŞLA")

başlabuton = p.Button(çer1,bg="grey",font="15",text="BAŞLA",fg="black")
başlabuton.config(command=oyun)
başlabuton.place(relx=0.15,rely=0.645,relwidth=0.65,relheight=0.1)






p.Button(çer1,bg="grey",font="15",text="KAPAT",fg="black",command=pencere1.quit).place(relx=0.15,rely=0.755,relwidth=0.65,relheight=0.1)


pencere1.mainloop()



