# #Problem1
#
# """1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
#
# Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)."""
#
# def  mukemmel_mi(sayi):
#     bolenler_toplami=0
#     for i in range(1,sayi):
#         if sayi%i==0:
#             bolenler_toplami+=i
#     return  bolenler_toplami==sayi
#
# for sayi in range(1,30001):
#     if (mukemmel_mi(sayi)):
#         print(sayi)

# #Problem2
# print("""EBOB bulma Programi""")
#
#
# def ebob_bulma(sayı1, sayı2):
#     i = 1
#     ebob = 1
#     while (i <= sayı1  and  i <= sayı2):
#
#         if (not (sayı1 % i) and not (sayı2 % i)):
#             ebob = i
#         i += 1
#     return ebob
#
# sayı1 = int(input("Sayı-1:"))
# sayı2 = int(input("Sayı-2:"))
#
# print("Ebob:", ebob_bulma(sayı1, sayı2))

# #Problem3
# def EKOK_bulma(sayi1,sayi2):
#     i=2
#     ekok=1
#     while   True:
#
#         if( sayi1 % i == 0   and   sayi2 % i == 0):
#             ekok*=i
#
#             sayi1 //= i
#             sayi2 //= i
#
#
#         elif    ( sayi1  %  i  == 0  and  sayi2  %   i  != 0):
#
#             ekok    *=i
#
#             sayi1 //= i
#
#
#         elif ( sayi1  %  i  !=  0  and  sayi2  %  i  ==  0):
#             ekok *= i
#
#             sayi2 //= i
#
#         else:
#             i += 1
#         if  (sayi1 == 1  and  sayi2 == 1):
#             break
#     return ekok
#
#
# sayi1=int(input("Sayi1: "))
# sayi2=int(input("Sayi2: "))
#
# print("EKOK",EKOK_bulma(sayi1,sayi2))

#Problem 4
#
# print("""Sayilarin Okunusu Icin Program""")
# birler=[' ',"bir","iki","uc",'dord','bes','alti','yedi','sekiz','dokuz']
# onlar=[' ',"on","iyirmi","otuz",'kirk','elli','altmis','yetmis','seksen','doksan']
#
#
# def okunusu(sayi):#15
#     qaliq=sayi%10#5
#     tam=sayi//10#1
#     return onlar[tam]+" "+ birler[qaliq]
#
# sayi=int(input("Sayi giriniz:"))
# print(okunusu(sayi))

# #Problem5
# print("Pisagor Bulma Programi")
# def pisagor_bulma():
#     pisagor_listei=list()
#     for i in range(1,101):
#         for j in range(1,101):
#             c=(i**2+j**2)**0.5
#
#             if( c ==int(c) ):
#                 pisagor_listei.append((i,j,int(c)))
#     return pisagor_listei
#
# for i in pisagor_bulma():
#     print(i)
