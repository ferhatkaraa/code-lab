#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>

using namespace std;

// --- GLOBAL DEÐÝÞKENLER ---
// Dosya okuma/yazma iþlemleri ve gecici veri tutmak için kullanilan degiskenler
fstream file;
ofstream ofile;
ifstream ifile;
string satir, kelime, dosya_metni;
int i;

// --- KULLANICI VERI YAPISI ---
struct users {
	char isim[15];
	int sifre;
	bool isstudent; // true ise ögrenci, false ise ögretmen
};

// ==========================================
// KULLANICI KAYIT FONKSIYONU
// ==========================================
bool regist_users(struct users user1, int giris_tipi) {
	printf("Lutfen kullanici adinizi giriniz:\n");
	scanf("%s", &user1.isim);
	printf("Lutfen sifrenizi giriniz:\n");
	scanf("%d", &user1.sifre);
	cout << "Kullanici adi = " << user1.isim << " | Sifre = " << user1.sifre << "\n";	
	
    // giris_tipi 1 (ogrenci) ise (1-2) = -1 -> bool karsiligi true'dur (C++'da 0 disi her sey true'dur)
    // giris_tipi 2 (ogretmen) ise (2-2) = 0 -> bool karsiligi false'tur.
	user1.isstudent = bool (giris_tipi - 2);

	if(user1.isstudent == true) {
        // Ogrenci ise ogrenciler.txt dosyasinin sonuna (ios::app) ekle
		ofile.open("öðrenciler.txt", ios::app);
		ofile << user1.isim << " : " << user1.sifre << "\n";
	} else if(user1.isstudent == false) {
        // Ogretmen ise ogretmenler.txt dosyasinin sonuna ekle
		ofile.open("öðretmenler.txt", ios::app);
		ofile << user1.isim << " : " << user1.sifre << "\n";
	} else {
		printf("Bir hata olustu lutfen tekrar deneyin.\n");
		return false;
	}
	ofile.close();
	printf("Tesekkurler, kaydiniz alinmistir.\n");
	return true;
}

// ==========================================
// KULLANICI GIRIS (LOGIN) KONTROL FONKSIYONU
// ==========================================
bool chack_users(struct users *usersp, int giris_tipi) {
	stringstream strsifre;
	printf("Lutfen kullanici adinizi giriniz:\n");
	scanf("%s", &usersp->isim);
	printf("Lutfen sifrenizi giriniz:\n");
	scanf("%d", &usersp->sifre);
	
	usersp->isstudent = bool (giris_tipi - 2);
	
	if(usersp->isstudent) {
        // Ogrenci girisi kontrolu
		ifile.open("öðrenciler.txt");
		while(ifile >> kelime) {
			if(kelime == usersp->isim) {
				ifile >> kelime; // ":" isaretini atla
				ifile >> kelime; // Sifreyi al
				strsifre << usersp->sifre;
				if(kelime == strsifre.str()) {
					cout << "Giris basarili." << endl;
					ifile.close();
					return true;
				} else continue;
			} else getline(ifile, satir); // Isim eslesmediyse satiri atla
		}
	} else if(!(usersp->isstudent)) {
        // Ogretmen girisi kontrolu
		ifile.open("öðretmenler.txt");
		while(ifile >> kelime) {
			if(kelime == usersp->isim) {
				ifile >> kelime;
				ifile >> kelime;
				strsifre << usersp->sifre;
				if(kelime == strsifre.str()) {
					cout << "Giris basarili." << endl;
					ifile.close();
					return true;
				} else continue;
			} else getline(ifile, satir);
		}
	}
	
    // Dongu bittiyse ve return true calismadiysa giris basarisizdir
	ifile.close();
	cout << "Kullanici adi veya sifre hatali.\nLutfen tekrar deneyin.\n";
	return false;
}

// ==========================================
// DERSLERI LISTELEME FONKSIYONU
// ==========================================
void sayfa_yenile() {
    // Ekrani temizlemek icin bosluk birak
	for(i = 0; i < 50; i++) printf("\n");
	printf("---------------------------------------\n");
    
    // dersler.txt dosyasini okuyup formatli sekilde ekrana basar
    ifile.open("dersler.txt");
	while(ifile >> kelime) {
		cout << "Ogretmenin adi : " << kelime << endl;
		ifile >> kelime;
		cout << "Ders adi       : " << kelime << endl;
		ifile >> kelime;
		cout << "Ders kodu      : " << kelime << endl;
		ifile >> kelime; // Kontenjan veya baska bir veri
		cout << "                 " << kelime << endl;
		getline(ifile, satir); // Kalan katilimcilari atla
		printf("---------------------------------------\n");
	}
	ifile.close();
}

// ==========================================
// OGRETMEN: YENI DERS EKLE
// ==========================================
void ders_ekle(string name, int code) {
	stringstream strcode;
	char ders_adi[15];
	int ders_kontenjan;
	printf("Lutfen eklemek istediginiz yeni dersin adini giriniz:\n");
	scanf("%s", &ders_adi);
	printf("Lutfen eklemek istediginiz yeni dersin kontenjan sinirini belirtiniz:\n");
	scanf("%d", &ders_kontenjan);
	
	strcode << code;
    // Dosyanin sonuna (app) yeni dersi formatli sekilde yaz
	ofile.open("dersler.txt", ios::app);
	ofile << name << " " << ders_adi << " " << code << " " << ders_kontenjan << " \n";
	ofile.close();
}

// ==========================================
// OGRETMEN: DERS SIL
// ==========================================
void ders_sil(string name, int code) {
	stringstream strcode;
	strcode << code;
    dosya_metni = ""; // (UYARI: Global degisken oldugu icin her seferinde temizlenmeli)
    
	file.open("dersler.txt");
	while(getline(file, satir)) {
        // Eger satirda hem ders kodu hem de ogretmen adi varsa o satiri atla (sil)
		if (satir.find(strcode.str()) != string::npos && satir.find(name) != string::npos) {
			cout << "Ders silinmistir." << endl;
			continue;
		} else {
            // Silinmeyecek satirlari gecici metinde topla
			dosya_metni += satir + "\n";
		}
	}
	file.close();
    
    // Dosyayi bastan yaz (ios::out) ve sadece silinmeyen satirlari kaydet
	file.open("dersler.txt", ios::out);
	file << dosya_metni;
	file.close();	
}

// ==========================================
// OGRENCI: DERSE KATIL
// ==========================================
void derse_katil(string name, int code) {
	stringstream strcode;
	strcode << code;
    dosya_metni = ""; 

	file.open("dersler.txt");
	while(getline(file, satir)) {
        // Ilgili dersi bulursan satir sonuna ogrenci adini ekle
		if (satir.find(strcode.str()) != string::npos) {
			dosya_metni += (satir + name + ",\n");
			cout << "Ders kaydiniz alinmistir." << endl;
		} else {
            dosya_metni += (satir + "\n");
        }
	}
	file.close();
	file.open("dersler.txt", ios::out);
	file << dosya_metni;
	file.close();	
}

// ==========================================
// OGRENCI: DERSTEN AYRIL
// ==========================================
void dersten_ayril(string name, int code) {
	stringstream strcode;
    dosya_metni = "";
	strcode << code;
	
    file.open("dersler.txt");
	while(getline(file, satir)) {
        // Icerisinde ders kodu ve ogrenci adi gecen satiri bul
		if(satir.find(strcode.str()) != string::npos && satir.find(name) != string::npos) {
			size_t index = satir.find(name);
			if (index != string::npos) {
                // Ogrencinin adini satirdan keserek cikar
				string yeni_satir = satir.substr(0, index) + satir.substr(index + name.length() + 1);
				dosya_metni += (yeni_satir + "\n");
				cout << "Dersten basarili bir sekilde ayrildiniz." << endl;
			}
		} else {
            dosya_metni += (satir + "\n");
        }
	}
	file.close();
	file.open("dersler.txt", ios::out);
	file << dosya_metni;
	file.close();
}	

// ==========================================
// DERSE KAYITLI KISILERI GORUNTULEME
// ==========================================
void katilimcilari_gor(bool isstu, int code) {
	stringstream strcode;
	strcode << code;
	
    ifile.open("dersler.txt");
	while(ifile >> kelime) {
		ifile >> kelime; // Ogretmen adini gec
		ifile >> kelime; // Ders adini gec
        
        // Ders kodu eslesiyorsa
		if (kelime == strcode.str()) {
			ifile >> kelime; // Kontenjani gec
			ifile >> kelime; // Katilimci listesine gel
			
            // Isimleri virgullerden ayirarak yazdir
			while(true) {
				size_t kes_index = kelime.find(",");
				cout << kelime.substr(0, kes_index) << endl;
				kelime = kelime.substr(kes_index + 1, kelime.length());		
				if(kelime.length() <= 1) break;
			}	
		} else {
			getline(ifile, satir);
			continue;
		}
	}
	ifile.close();
}

// ==========================================
// ALT MENU (HATA VEYA CIKIS YONETIMI)
// ==========================================
int cikis_menusu() {
	int a;
	printf("1-Tekrar dene\n2-Ana menuye don\n3-Uygulamayi kapat\n");
	scanf("%d", &a);
	return a;
}

// ==========================================
// KULLANICI ISLEM YONLENDIRICISI
// ==========================================
int kontrol(struct users *users) {
	int code = 0;
	int kont;
	scanf("%d", &kont);
	
    // Eger secim 3, 4 veya 5 ise ders kodu gereklidir
	if (kont > 2 && kont < 6) {
		printf("Lutfen islem yapacaginiz dersin kodunu giriniz:\n");
		scanf("%d", &code);
	}
		
	switch(kont) {
		case 1:
			return 2; // Cikis
		case 2:
			sayfa_yenile();
			return 1;
		case 3:
			katilimcilari_gor(users->isstudent, code);
			return 1;
		case 4:
			if(users->isstudent) derse_katil(users->isim, code);
			else ders_ekle(users->isim, code);
			return 1;
		case 5:
			if(users->isstudent) dersten_ayril(users->isim, code);
			else ders_sil(users->isim, code);
			return 1;
		default:
			printf("Lutfen verilen sayilardan birini giriniz.\n");
			return 1;
	}
}

// ==========================================
// GIRIS SONRASI KULLANICI PANELI
// ==========================================
int open_page(bool func, struct users *users, int hata, int cikis) {
	if (func) {
        // Giris basariliysa
		sayfa_yenile();
		printf("HOSGELDINIZ\n");
		while(cikis == 1) {
			printf("1-Cikis\n2-Sayfayi yenile\n3-Katilimcilari gor\n");
			if(users->isstudent) {
				printf("4-Derse katil\n5-Dersten ayril\nLutfen bir secim yapiniz:\n");
			} else {
				printf("4-Ders ekle\n5-Ders sil\nLutfen bir secim yapiniz:\n");
			}
			cikis = kontrol(users);
		}
		return 1;
	} else {
        // Giris basarisizsa
		printf("HATA\nGIRMIS OLDUGUNUZ KULLANICI ADI VEYA SIFRE HATALIDIR.\nLUTFEN TEKRAR DENEYIN.\n");
		hata++;
		return hata; // Hata sayacini artirarak geri dondur
	}
}

// ==========================================
// ANA FONKSIYON
// ==========================================
int main() {
	int hata_sayisi = 1;
	int giris_tipi = 0;
	int giris_kayit = 0;
	int cikis = 1;
	struct users user1;

	printf("Hosgeldiniz\n************************\n");
	printf("Online Ders Giris Sistemi\n");
	
	while(giris_kayit != 1 && giris_kayit != 2 && cikis != 3) {
		
		printf("1-Giris yap\n2-Kayit ol\n");
		scanf("%d", &giris_kayit);
		
		printf("1-Ogrenci\n2-Ogretmen\nLutfen seciminizi yapiniz:\n");
		scanf("%d", &giris_tipi);
		
		if((giris_kayit == 1 || giris_kayit == 2) && (giris_tipi == 1 || giris_tipi == 2)) {
			
            // --- KAYIT OLMA DONGUSU ---
			while(giris_kayit == 2) {
				if(regist_users(user1, giris_tipi)) {
					giris_kayit = 0;
					hata_sayisi = 1;
					printf("Ana menuye donuluyor...\n");
					break;
				} else {
					hata_sayisi++;
					cikis = cikis_menusu();
					if(cikis != 2 && cikis != 3) {
						if(hata_sayisi == 6) {
							printf("Malesef cok fazla hatali kayit denemesinde bulundunuz, sizi ana menuye aktariyorum.\n");
							cikis = 2;
							break;
						} else if(hata_sayisi == 10) {
							printf("Malesef cok fazla hatali kayit denemesinde bulundunuz. Lutfen daha sonra tekrar deneyin.\n");
							cikis = 3;
							break;
						}
					} else break;
				}
			}
			
            // --- GIRIS YAPMA DONGUSU ---
			while(giris_kayit == 1) {
				cikis = 1;
				hata_sayisi = open_page(chack_users(&user1, giris_tipi), &user1, hata_sayisi, cikis);
				
                // Eger giris basarisiz olduysa ve open_page hata_sayisi dondurduyse
                if(hata_sayisi > 1 && cikis == 1) cikis = cikis_menusu(); 
                
				if(cikis == 2 || cikis == 3) {
					giris_kayit = 0;
					break;
				}
				if(hata_sayisi >= 6 && hata_sayisi < 10) {
					printf("Malesef cok fazla hatali giris denemesinde bulundunuz, sizi ana menuye aktariyorum.\n");
					cikis = 2;
					break;
				} else if(hata_sayisi >= 10) {
					printf("Malesef cok fazla hatali giris denemesinde bulundunuz. Lutfen daha sonra tekrar deneyin.\n");
					cikis = 3;
					break;
				}
			}
					
		} else {
			giris_kayit = 0;
			printf("Lutfen 1 ya da 2 giriniz.\n");
		}
	}

	return 0;
}
