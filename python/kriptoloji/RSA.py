

print("RSA şifreleme algoritması...")

#input değer olarak 12,234 gibi ik sayı aralarında virgül olacak şekilde yazılır
password = input("şifrelenecek anahtarı gir:(e,n)")
password = password.split(",")

pass1,pass2 = int(password[0]),int(password[1])


with open("metin.txt","r+",encoding="utf-8") as file:
    old_file = file.read()
    new_file = ""
    for i in old_file:
        new_file += chr((ord(i)**pass1) % pass2)
    file.seek(0)
    file.truncate(0)            # Dosya içeriğini siler
    file.seek(0) 
    file.write(new_file)
    