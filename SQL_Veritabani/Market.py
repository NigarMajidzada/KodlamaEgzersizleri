import  sqlite3

class Urun():
    def __init__(self,isim,fiyat):
        self.isim=isim
        self.fiyat=fiyat

    def  __str__(self):
        return "Urunun ismi {}\nFiyati: ".format(self.isim,self.fiyat)


class Market():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("supermarket.db")
        self.cursor=self.baglanti.cursor()
        sorgu="Create table if not exists Market(isim text,fiyat int)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()


    # def urunler(self):
    #     sorgu="select isim from Market"
    #     isim=self.cursor.execute(sorgu)
    #     print("Urunler: {}".format(isim))
    #
    # def fiyat(self):
    #     sorgu="select fiyat from Market"
    #     fiyat=self.cursor.execute(sorgu)
    #     print("Fiyatlar: {}".format(fiyat))

    def butun_bilgiler(self):
        sorgu="select * from Market"
        self.cursor.execute(sorgu)
        urunler=self.cursor.fetchall()

        if not urunler:
            print("Market bos")
        else:
            for i in urunler:
                print("Urun ismi: {}\nUrun fiyati: {}".format(i[0],i[1]))

    def urun_ekle(self,urun):
        sorgu="Insert into Market values(?,?)"
        self.cursor.execute(sorgu,(urun.isim,urun.fiyat))
        self.baglanti.commit()

    def urun_sil(self,urun):
        sorgu="delete from Market where isim=?"
        self.cursor.execute(sorgu,(urun,))
        self.baglanti.commit()
        # print("Urun silindi: {}".format(urun))
