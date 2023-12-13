# #Problem1
# boy=float(input("Boyunuzu giriniz: "))
# kilo=float(input("Kilonuzu giriniz: "))
# bki=kilo/(boy**2)
#
# if bki<18.5:
#     print("Zayif:{}".format(bki))
# elif bki >=18.5 and  bki    <25:
#     print("Normal")
# elif bki >=25 and  bki    <30 :
#     print("Fazla Kilolu")
# elif bki >30:
#     print("Obez")

# #Problem2
# sayi1=int(input("Sayi1: "))
# sayi2=int(input("Sayi2: "))
# sayi3=int(input("Sayi3: "))
#
# liste=[sayi1,sayi2,sayi3]
# liste==liste.sort()
# print(liste[-1])

# #Problem3
#
# vize1 =int(input("Vize1:"))
# vize2 =int(input("Vize2:"))
# final =int(input("Final:"))
#
# toplam_not=vize1*3/10+vize2*3/10+final*4/10
#
# if toplam_not >=90:
#     print("AA")
# elif toplam_not>=85:
#     print("BA")
# elif  toplam_not>=80:
#     print("BB")
# elif toplam_not>=75:
#     print("CB")
# elif toplam_not>=70:
#     print("CC")
# elif toplam_not >= 65:
#     print("DC")
# elif toplam_not>=55:
#     print("FD")
# elif toplam_not<70:
#     print("FF")

# #Problem4
#
# geo=int(input("Dortgen  icin 1-e Ucgen icin 2-ye basin: "))
# if geo==1:
#             a=int(input("Kenar1: "))
#             b=int(input("Kenar2: "))
#             c=int(input("Kenar3: "))
#             d=int(input("Kenar5: "))
# if (a == b and a == c and a == d):
#     print("Kare dortgendir. ")
#
# elif(a==c and b==d):
#
#     print("Dikdortgen ")
# else:
#     print("Dortgen")
#
# elif  geo==2:
#     a = int(input("Kenar-1:"))
#     b = int(input("Kenar-2:"))
#     c = int(input("Kenar-3:"))
#     if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
#         if (a == b and a == c):
#             print("Eşkenar Üçgen...")
#         elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
#             print("İkizkenar Üçgen....")
#         else:
#             print("Çeşitkenar Üçgen...")
#     else:
#         print("Üçgen belirtmiyor...")
#
# else:
#     print("Geçersiz Şekil...")
# Problem4 solution

şekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz?")

if (şekil == "Dörtgen"):
    print("Lütfen kenarları sırayla giriniz.")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-4:"))

    if (a == b and a == c and a == d):
        print("Kare")
    elif (a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")



elif (şekil == "Üçgen"):
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")

else:
    print("Geçersiz Şekil...")