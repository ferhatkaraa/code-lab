

"""
   00000000 --> 8'li kod
   1:noktalama/harf
   2:capclock
   3:noktalı harf
   45678:harfin kodu 
    
    
    
    
"""
import os






global DATA
DATA = {
    " ":"10000000",
    "a":"00000001",
    "A":"01000001",
    "b":"00000010",
    "B":"01000010",
    "c":"00000011",
    "C":"01000011",
    "ç":"00100011",
    "Ç":"01100011",
    "d":"00000100",
    "D":"01000100",
    "e":"00000101",
    "E":"01000101",
    "f":"00000110",
    "F":"01000110",
    "g":"00000111",
    "G":"01000111",
    "ğ":"00100111",
    "Ğ":"01100111",
    "h":"00001000",
    "H":"01001000",
    "ı":"00001001",
    "I":"01001001",
    "i":"00101001",
    "İ":"01101001",
    "j":"00001010",
    "J":"01001010",
    "k":"00001011",
    "K":"01001011",
    "l":"00001100",
    "L":"01001100",
    "m":"00001101",
    "M":"01001101",
    "n":"00001110",
    "N":"01001110",
    "o":"00001111",
    "O":"01001111",
    "ö":"00101111",
    "Ö":"01101111",
    "p":"00010000",
    "P":"01010000",
    "q":"00010001",
    "Q":"01010001",
    "r":"00010010",
    "R":"01010010",
    "s":"00010011",
    "S":"01010011",
    "ş":"00110011",
    "Ş":"01110011",
    "t":"00010100",
    "T":"01010100",
    "u":"00010101",
    "U":"01010101",
    "ü":"00110101",
    "Ü":"01110101",
    "v":"00010110",
    "V":"01010110",
    "w":"00010111",
    "W":"01010111",
    "x":"00011000",
    "X":"01011000",
    "y":"00011001",
    "Y":"01011001",
    "z":"00011010",
    "Z":"01011010",
    ".":"10011011",
    ":":"11011011",
    ",":"10011100",
    ";":"11011100",
    "*":"10011101",
    "?":"11011101",
    "<":"10011110",
    ">":"11011110",
    "!":"10011111",
    "=":"11011111"
    
}

def gizle(metin: str):
   yeni_metin = ""
   
   
   for i in metin:
       for j in DATA.keys():
           if i == j:
               yeni_metin += DATA[j]
               break
           elif DATA[j] == "11011111":
               yeni_metin += f"({i})"
          
          
               
   
   return yeni_metin 

def çöz(gizli_metin: str):
    yeni_metin = ""
    index = 0
    
    while index < len(gizli_metin):
        if gizli_metin[index] == "0" or gizli_metin[index] == "1":
            for j in DATA.keys():
                if DATA[j] == gizli_metin[index:index+8]:
                    yeni_metin += j
                    index += 8
                    break
        else:
            yeni_metin += gizli_metin[index]
            index += 1 
            
    return yeni_metin 
                    
def dosya_donustur():
    cumle = ""
    sayfalar =os.listdir()
    for i in sayfalar:
        if ".txt" in i:
            if "$.txt" in i:
                with open(i,"r",encoding="utf-8")as file:
                    cumle = file.read()
                    cumle = çöz(cumle)
                with open(i,"w",encoding="utf-8")as file:
                    file.write(cumle)
                os.rename(i,i[:i.find("$")]+ ".txt")
            else:
                with open(i,"r",encoding="utf-8")as file:
                    cumle = file.read()
                    cumle = gizle(cumle)
                with open(i,"w",encoding="utf-8")as file:
                    file.write(cumle)
                os.rename(i,i[:i.find(".")]+ "$.txt")


print(os.listdir())
dosya_donustur()



