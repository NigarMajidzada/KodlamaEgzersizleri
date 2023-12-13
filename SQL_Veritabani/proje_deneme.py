import time

import kutuphane
from kutuphane import *

print("""*****************************
Kutuphane Programina Hosgeldiniz.

Islemler
1.Kitaplari goster 
2.Kitap Sorgula
3.Kitap Ekle
4.Kitap Sil
5. Baskiyi Yukselt
6. Kitap yili
Cikmak icin  'q' basin
*********************
""")

kutuphane1=Kutuphane()
# kitap1=Kitap()


while True:
    islem   = input("Yapacaginiz Islemi Seciniz: ")

    if(islem=='q'or islem=='Q'):
        print("Programdan Cikiliyor...")
        break
    elif    (islem=="1"):
        kutuphane1.kitaplari_goster()
    elif    (islem=="2"):
        isim=input("Kitap adi giriniz: ")
        print("Kitab sorgualniyor...")
        time.sleep(1)
        kutuphane1.kitap_sorgula(isim)

    elif    (islem=="3"):
        isim=input("Kitabin ismi: ")
        yazar=input("Yazarin ismi: ")
        yayinevi=input("Yayinevi ismi: ")
        tur=input("Turu: ")
        baski=int(input("Baskisi: "))
        yeni_kitap=Kitap(isim, yazar, yayinevi, tur, baski)
        print("Kitap ekleniyor...")
        time.sleep(1)
        kutuphane1.kitap_ekle(yeni_kitap)
        print("Kitap eklendi ")


    elif    (islem=="4"):
        isim=input("Hangi kitabi silmek istiyorsunuz? ")
        cevap=input("Silmek istediyinizden emin misiniz?")
        if cevap=='E':
            kutuphane1.kitap_sil(isim)
            print("Kitap silindi...")
        else:
            print("Kitap silme islemi yapilmamisdir" )
    elif    (islem=="5"):
        isim=input("Hangi kitabin baskisini yukseltmek istiyorsunuz? ")
        print("Baski yukseltiliyo...")
        time.sleep(1)
        kutuphane1.baskiyi_yukselt(isim)
        print("Baski yukseltildi.")

    else:
        print("Gecersiz Islem...")
