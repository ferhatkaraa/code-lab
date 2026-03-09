import pandas as pd
import os

# CSV'yi okuyoruz. Yorum satırlarını (#) atlamak için comment parametresi ekledik.
df = pd.read_csv("alfabe.csv", comment="#")

# CSV'de olmayan ama düzeltilmesi gereken Türkçe karakterler
others = {
    "ğ": "g", "Ğ": "G",
    "ı": "i", "İ": "I"
}

# Dosya yoksa oluştur
if not os.path.exists("mesaj.txt"):
    with open("mesaj.txt", "w", encoding="utf-8") as file:
        pass

def encode_message(mode="Mors"):
    """
    mode parametresi "Mors" veya "Ikili" değerlerini alabilir.
    Metni ilgili koda dönüştürür.
    """
    if mode not in ["Mors", "Ikili"]:
        print("Hata: mode parametresi 'Mors' veya 'Ikili' olmalıdır.")
        return

    with open("mesaj.txt", "r", encoding="utf-8") as file:
        content = file.read()

    encoded_text = ""
    for char in content:
        # Türkçe karakter düzeltmeleri
        if char in others:
            char = others[char]
        
        char_upper = char.upper()

        # Karakter CSV'de (Harf sütununda) var mı?
        if char_upper in df["Harf"].values:
            code = df.loc[df["Harf"] == char_upper, mode].values[0]
            encoded_text += str(code) + " "
        else:
            # ÇÖZÜM BURADA:
            # CSV'de olmayan \n veya noktalama işaretlerinin
            # kendinden sonraki şifreyle birleşik yazılmasını önlemek için
            # sonlarına bir boşluk (ayraç) ekliyoruz.
            if char == " ":
                encoded_text += " "
            else:
                encoded_text += char + " "

    with open("mesaj.txt", "w", encoding="utf-8") as file:
        file.write(encoded_text)
    
    print(f"Mesaj başarıyla {mode} formatında şifrelendi!")


def decode_message(mode="Mors"):
    """
    Şifrelenmiş mesajı tekrar normal harflere dönüştürür.
    """
    if mode not in ["Mors", "Ikili"]:
        print("Hata: mode parametresi 'Mors' veya 'Ikili' olmalıdır.")
        return

    decode_dict = dict(zip(df[mode].astype(str), df["Harf"]))

    with open("mesaj.txt", "r", encoding="utf-8") as file:
        content = file.read()

    decoded_text = ""
    parts = content.split(" ")

    for part in parts:
        if part in decode_dict:
            decoded_text += decode_dict[part]
        elif part == "":
            decoded_text += " "
        else:
            decoded_text += part

    # Her şifrenin sonuna ayraç olarak boşluk eklediğimiz için,
    # decode işlemi bittiğinde en sonda oluşan o tek fazladan boşluğu siliyoruz.
    if decoded_text.endswith(" "):
        decoded_text = decoded_text[:-1]

    with open("mesaj.txt", "w", encoding="utf-8") as file:
        file.write(decoded_text)
    
    print(f"Mesaj {mode} formatından normal metne başarıyla geri çevrildi!")

encode_message()  
decode_message()


# TEST İÇİN:
# encode_message("Ikili")  
# decode_message("Ikili")