#Problem 1
import sqlite3
from functools import reduce

class Sarki():

    def __init__(self,isim,sanatci,album,produksiyon,sure):
        self.isim=isim
        self.sanatci=sanatci
        self.album=album
        self.produksiyon=produksiyon
        self.sure=sure

    def __str__(self):
        return "Sarki ismi: {}\nSanatci ismi: {}\nAlbumun ismi: {}\nProduksiyon sirketi: {}\nSarki suresi: {}".format(self.isim,self.sanatci,self.album,self.produksiyon,self.sure)

class Playlist():
    def  __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("playlist.db")
        self.cursor=self.baglanti.cursor()
        sorgu="Create table if not exists Sarkilar (isim text,sanatci text,album text,produksiyon text, sure int)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()



    def toplam_sure_hesapla(self):
        sorgu="select sure from Sarkilar"
        self.cursor.execute(sorgu)
        sureler=self.cursor.fetchall()

        if  not sureler:
            print("Playlist bos...")
        else:
            toplam_sure = reduce(lambda x, y: x + y[0], sureler, 0)
            print(toplam_sure)


    def sarki_ekle(self,Sarki):
        sorgu="Insert into Sarkilar values (?,?,?,?,?)"
        self.cursor.execute(sorgu,(Sarki.isim,Sarki.sanatci,Sarki.produksiyon,Sarki.album,Sarki.sure))
        self.baglanti.commit()

    def sarki_sil(self,isim):
        sorgu="delete from Sarkilar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()


    def sarkilari_goster(self):
        sorgu="select * from Sarkilar"
        self.cursor.execute(sorgu)
        sarkilar=self.cursor.fetchall()

        if  (len(sarkilar)==0):
            print("Playlist bosdu.")
        else:
            for i in sarkilar:
                sarki=Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)
