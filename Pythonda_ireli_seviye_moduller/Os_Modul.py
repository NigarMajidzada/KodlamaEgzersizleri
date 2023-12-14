import os
from _datetime import  datetime

print(os.getcwd())

# os.mkdir("Deneme1")
# os.makedirs("Deneme2/Deneme3")
# os.rmdir("Deneme2/Deneme3")
# os.makedirs("Deneme2/Deneme3")
# os.rmdir("Deneme1")
# os.removedirs("Deneme2/Deneme3")

# os.rename("Test.txt","Test2.txt")
# print(datetime.fromtimestamp(os.stat("Test2.txt").st_mtime))

# for KloserYolu, Kloser_isimleri, Dosya_isimleri  in os.walk("C:/Users/nigar/PycharmProjects/Kodlama Egzersizleri/Pythonda_ireli_seviye_moduller"):
#     print("KloserYolu",KloserYolu)
#     print("Kloser isimleri:",Kloser_isimleri)
#     print("Dosya isimleri: ",Dosya_isimleri)
#     print("**************************************")

# for KloserYolu, Kloser_isimleri, Dosya_isimleri  in os.walk("C:/Users/nigar/PycharmProjects/Kodlama Egzersizleri"):
#     for i in Dosya_isimleri:
#         if i.endswith("txt"):
#             print(i)
