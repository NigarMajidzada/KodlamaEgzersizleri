import  random
import time

print("""           Sayi Tahmini Oyunu 
(1 ile 40 arasinda sayi tahmin edin)""")

rasgele_sayi=random.randint(1,40)
tahmin_hakki=7

while True:
    tahmin=int(input("Tahmininiz:  "))
    print("Tahmininiz Sorgulaniyor...")
    time.sleep(0.5)
    tahmin_hakki-=1
    print(" Tahmininiz Yalnis  {} Tahmin  Hakkiniz Kaldi.".format(tahmin_hakki))


    if (tahmin==rasgele_sayi ):
        print("Tebrikler Dogru Tahmin Etdiniz...")
        break
    elif(tahmin_hakki==0 ):
        print("Tahmin Hakkiniz Bitmisdir...")
        break
    elif(tahmin<0  or tahmin>40):
        print("Verilmis Aralikda bir Tahmin Soyleyiniz...")

    # else:
    #     continue
