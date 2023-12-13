

def eksra(fonc):
    def wrapper(sayilar):
        ciftler_toplami=0
        cift_sayilar=0
        tekler_toplami=0
        tek_sayilar=0

        for sayi in sayilar:
            if(sayi%2==0):
                ciftler_toplami+=sayi
                cift_sayilar+=1
            else:
                tekler_toplami+=sayi
                tek_sayilar+=1
        print("Teklerin ortalamas: ", tekler_toplami/tek_sayilar)
        print("Ciftlerin ortalamas: ", ciftler_toplami/cift_sayilar)

        fonc(sayilar)
    return wrapper
@eksra
def ortalama_bul(sayilar):
    toplam=0
    for i in  sayilar:
        toplam+=i
    print("Ortalam: ", toplam/len(sayilar))


ortalama_bul([1,2,5,6,9,10])
