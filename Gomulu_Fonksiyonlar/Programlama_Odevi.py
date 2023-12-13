#Porblem1
#Dikdortgenin  alanini hesaplayan fonsiyon ve liste
# def alan(demet):
#     return demet[0]*demet[1]
#
# liste=  [(3,4),(10,3),(5,6),(1,9)]
#
# print(list(map(alan,liste)))

#
# #Kendim
#
# def sahe(s):
#     return s[0]*s[1]
#
# reqem=[(1,2),(3,5),(5,9)]
#
# print(list(map(sahe,reqem)))

#Problem2
# def ucgen_mi(demet):
#     if  (abs(demet[0]+demet[1]>demet[2]) and abs(demet[0]+demet[2]>demet[1] ) and abs  (demet[1]+demet[2]>demet[0])):
#         return True
#     else:
#         return False
# liste= [(3,4,5),(6,8,10),(3,10,7)]
#
# print(list(filter(ucgen_mi,liste)))


# # Problem3
#
# from functools import reduce
#
# def cift_mi(sayi):
#     return sayi%2==0
#
# def toplama(x, y):
#     return x+y
#
# liste=[1,2,3,4,5,6,7,8,9,10]
# cift_list=list(filter(cift_mi,liste))
# print(cift_list)
# #
# print(reduce(toplama,cift_list))


#Problem4

isimler=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

info=zip(isimler,soyisimler)

for i, j in info :
    print(i,j)
