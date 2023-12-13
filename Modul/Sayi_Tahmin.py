
import  random
import  time


print("""Sayi Tahmini
(0 ile 15 arasinda )""")
tahmin=1
random_sayi=random.randint(1,15)
tahmin_hakki=7

while True:
    tahmin=int(input("Tahminizi Giriniz:  "))

    if (tahmin_hakki == 1):
        print("Tahmin hakkiniz bitmisdir")
        break
    elif(tahmin<0 or tahmin>15):
        print("0 ile 15 arasinda bir sayi seciniz")
    elif(tahmin<random_sayi):
        print("Tahmininiz sorgulaniyor...")
        time.sleep(1)
        print("Daha buyuk bir rakam giriniz...")
        tahmin_hakki-=1
        print("Kalan tahmin hakkiniz: {}".format(tahmin_hakki))
        continue

    elif(tahmin>random_sayi):
            print("Tahmininiz sorgulaniyor...")
            time.sleep(1)
            print("Daha kucuk bir rakam giriniz...")
            tahmin_hakki -= 1
            print("Kalan tahmin hakkiniz: ",tahmin_hakki)
            continue
    elif(tahmin==random_sayi):(
            print("Tebrikler dogru sayi {}".format(tahmin)))
    break

# #Optomize
#
#
# import random
# import time
#
# print("Sayi Tahmini\n(0 ile 15 arasinda )")
#
# random_sayi = random.randint(0, 15)
# tahmin_hakki = 7
#
# while tahmin_hakki > 0:
#     tahmin = int(input("Tahminizi Giriniz: "))
#
#     if tahmin < 0 or tahmin > 15:
#         print("0 ile 15 arasinda bir sayi seciniz")
#     elif tahmin < random_sayi:
#         print("Tahmininiz sorgulaniyor...")
#         time.sleep(1)
#         print("Daha buyuk bir rakam giriniz...")
#     elif tahmin > random_sayi:
#         print("Tahmininiz sorgulaniyor...")
#         time.sleep(1)
#         print("Daha kucuk bir rakam giriniz...")
#     else:
#         print(f"Tebrikler! Dogru sayi: {tahmin}")
#         break
#
#     tahmin_hakki -= 1
#     print(f"Kalan tahmin hakkiniz: {tahmin_hakki}")
#
# if tahmin_hakki == 0:
#     print(f"Tahmin hakkiniz bitmisdir. Doğru sayi: {random_sayi}")
