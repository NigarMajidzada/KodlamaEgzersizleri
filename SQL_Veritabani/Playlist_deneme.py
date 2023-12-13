import Playlist
from Playlist import *
import time
print("""**************
Playlist Projesi
***************
1. Sarki eklemek 
2. Sarki silmek 
3.Toplam sure 
4.Butun playlist 

Cikmak icin q basin

""")

playlist1=Playlist()
# sarki1=Sarki()

while True:

    islem=input("Yapacaginiz Islemi Secin: ")

    if  islem=='q':
        print("Programdan cikiliyor...")
        time.sleep(1)
        break
    elif islem=="1":
        isim=input("Sarki ismi: ")
        sanatci=input("Sanatci ismi: ")
        album=input("Album ismi: ")
        produksiyon=input("Produksiyon Sirkerti: ")
        sure=int(input("Sarki suresi: "))
        yeni_sarki=Sarki(isim,sanatci,album,produksiyon,sure)
        print("Yeni sarki ekleniyor...")
        time.sleep(1)
        playlist1.sarki_ekle(yeni_sarki)
        print("Sarki eklendi.")

    elif    islem=="2":
        isim=input("Silmek istediyiniz sarkinin ismini giriniz...")
        playlist1.sarki_sil(isim)
        print("Sarki silindi")
    elif islem=="3":
        playlist1.toplam_sure_hesapla()

    elif islem=="4":
        playlist1.sarkilari_goster()

    else:
        print("Gecersiz islem...")
        break
