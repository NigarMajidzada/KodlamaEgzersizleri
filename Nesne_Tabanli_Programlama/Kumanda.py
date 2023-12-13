import random
import time

class Kumanda():

    def __init__(self, tv_durum="Kapali", tv_ses=0, kanal_listesi=["TRT", "AzTV"], kanal="TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "Acik":
            print("TV zaten acik")
        else:
            print("TV aciliyor...")
            self.tv_durum = "Acik"

    def tv_kapat(self):
        if self.tv_durum == "Kapali":
            print("TV zaten kapali")
        else:
            print("TV kapitiliyor...")
            self.tv_durum = "Kapali"

    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi artırmak için '1' basiniz. Sesi azaltmak için '2' basiniz. Çıkış için 'exit' -e basiniz: ")
            if cevap == '2':
                if self.tv_ses != 0:
                    self.tv_ses -= 5
                    print("Ses: ", self.tv_ses)
            elif cevap == '1':
                if self.tv_ses != 100:
                    self.tv_ses += 5
                    print("Ses: ", self.tv_ses)
            elif cevap.lower() == 'exit':
                print("Ses güncellenmedi: ", self.tv_ses)
                break
            else:
                print("Geçersiz giriş!")

    def kanal_ekle(self, kanal_ekle):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ekle)
        print("Kanal eklendi: ", self.kanal_listesi)

    def random_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Su anki kanal: ", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv durum: {}\nTv ses: {}\nkanal_listesi: {}\nSu anki kanal: {}".format(
            self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)

def menu(self,tv_durum="Kapali", tv_ses=0, kanal_listesi=["TRT", "AzTV"], kanal="TRT"):
    print("TV durum: {}\nTV ses: {}\nKanal_listesi: {}\nKanal: {}".format(tv_durum,tv_ses,kanal_listesi,kanal))
kumanda1 = Kumanda()

print("""TV programi
1.TV ac 
2.TV kapat
3.Ses ayarlari
4.Kanal ekle
5.Kanal sayisini oyrenme
6.Rastgele kanala gecme
7.TV bilgileri
8. Menu icin
Cikmak icin q basin""")

while True:
    islem = input("Isleminizi seciniz: ")
    if islem == 'q':
        print("Programiniz sonlaniyor")
        break
    elif islem == '1':
        kumanda1.tv_ac()
    elif islem == '2':
        kumanda1.tv_kapat()
    elif islem == '3':
        kumanda1.ses_ayarlari()
    elif islem == '4':
        kanal_isimler = input("Kanal isimlerini ',' ayirarak girin: ")
        kanal_isimler = kanal_isimler.split(",")
        for eklenecekler in kanal_isimler:
            kumanda1.kanal_ekle(eklenecekler)
    elif islem == '5':
        print("Kanal sayisi: ", len(kumanda1))
    elif islem == '6':
        kumanda1.random_kanal()
    elif islem == '7':
        print(kumanda1)
    elif islem=='8':
        menu(kumanda1)
    else:
        print("Gecersiz islem...")
