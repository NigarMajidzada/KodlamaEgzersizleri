from Market import *
print("""****************
Market Programi
****************
1. Tum Urun bilgileri
2. Urun ekle
3. Urun sil

Programdan cikmak icin q basin
""")
market1=Market()

while True:
    islem=input("Islem seciniz: ")

    if islem=="q":
        print("Program sonlandiriliyor...")
        break
    elif islem=="1":
        market1.butun_bilgiler()

    elif islem=="2":
        isim=input("Urunun ismini giriniz: ")
        fiyat=int(input("Urunun fiyatini giriniz: "))
        yeni_urun=Urun(isim,fiyat)
        market1.urun_ekle(yeni_urun)
        print("Urun eklendi")

    elif islem=="3":
        isim=input("Silmek istediginiz urunun ismini giriniz: ")
        market1.urun_sil(isim)
        print("Urun silindi")

    else:
        print("Gecersiz islem...")
        break
