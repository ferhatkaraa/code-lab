import os
import time

masaüstü = os.listdir()






def ara():
    sor = input("arama yap:\n").lower() + "."
    os.system("cls")
    print(f"C:\\Users\\FERHAT KARA\\OneDrive\\Masaüstü\\{sor}")
    if os.path.exists(sor):
        os.startfile(f"C:\\Users\\FERHAT KARA\\OneDrive\\Masaüstü\\{sor}")
    else:
        isit=[]
        for i in masaüstü:
            i = i.lower()
            if sor in i:
                isit.append((i,1.0))
                continue
            d = 0
            for j in range(len(sor[:sor.find(".")])):
                try:
                    if sor[j] == i[j]:
                        d+=1
                except IndexError:
                    break
            if d/len(sor[:sor.find(".")]) >= 0.5:
                isit.append((i,d/len(sor[:sor.find(".")])))
        if len(isit) == 1:
            os.system("cls")
            for i in range(10):
                print(f"çalıştırmak istediğin program {isit[0][0]} olabilir eğer değilse CTRL+C tuşlarına bas")
                print(f"programınçalışmasına son {10-i} saniye")
                time.sleep(1)
                os.system("cls")
            os.startfile(f"C:\\Users\\FERHAT KARA\\OneDrive\\Masaüstü\\{isit[0][0]}") 
            return
        else:
            for i,j in sorted(isit,key=lambda x: x[1], reverse=True):
                print(i,j) 
        ara()
ara()
                