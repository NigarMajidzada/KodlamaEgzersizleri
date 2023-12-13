#Problem 1

# sayi=int(input("Lutfen sayiyi giriniz: "))
# i=1
# toplam=0
#
# while(i<sayi):
#     if(sayi%i==0):
#         toplam+=i
#     i+=1
# if(toplam==sayi):
#     print("Bu sayi mukemmel bir sayidir.")
# else:
#     print("Bu sayi mukemmel sayi deyildir.")

# # Problem2
# sayi = input("Sayi: ")
# basamak_sayisi = len(sayi)
# sayi=int(sayi)
# basamak=0
# toplam=0
#
# gecici_sayi=sayi
#
# while(gecici_sayi>0):
#     basamak=gecici_sayi%10
#     toplam+=basamak**basamak_sayisi
#     gecici_sayi//=10
# if(toplam==sayi):
#     print(sayi,"bir  armstrong sayisidir.")
# else:
#     print(sayi,"bir armstrong sayisi deyildir.")
#

#Problem3
# for i in range(1,11):
#     print("***************************")
#     for j in range(1,11):
#         print("{}*{}={}".format(i,j,i*j))
#
#Problem4
# toplam=0
# while True:
#     sayi=input("Sayi: ")
#     if (sayi=="Q"):
#         break
#     else:
#         sayi    =int(sayi)
#         toplam += sayi
#         print("Toplam: ", toplam)
#
 #Problem 5
# for i in range(1,101):
#     if (i%3!=0):
#         continue
#     print(i)


#Problem 6
#1
# liste=[x for x in range(1,101) if x %2==0]
# print(liste)
#2
# for i in range(1,101):
#     if (i%2!=0):
#         continue
#     print(i)