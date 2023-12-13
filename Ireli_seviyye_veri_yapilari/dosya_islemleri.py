class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_icerigi=file.read()
            kelimeler=dosya_icerigi.split()
            self.sade_kelimeler=list()
            for i in kelimeler:
                i=i.strip(" ")
                i=i.strip(". ")
                i=i.strip("\n ")
                i=i.strip(", ")
                self.sade_kelimeler.append(i)


    def tum_kelimer(self):
        kelimeler_kumesi=set()
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
        print("Tum kelimer:   ")
        for i in kelimeler_kumesi:
            print(i)
            print("*******************")


    def kelime_frekansi(self):
        kelimeler_sozluk=dict()

        for i in self.sade_kelimeler:
            if i in kelimeler_sozluk:
                kelimeler_sozluk[i]+=1
            else:
                kelimeler_sozluk[i]=1

        for kelime,sayi in kelimeler_sozluk.items():
            print("{} kelimesi {} deaf geçiyor...".format(kelime,sayi) )
            print("-----------------------------------")



dosya1=Dosya()
dosya1.kelime_frekansi()
