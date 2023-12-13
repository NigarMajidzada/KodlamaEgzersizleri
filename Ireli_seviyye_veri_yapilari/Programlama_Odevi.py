# #Problem1 Frekans Bulma
#
# class frek():
#     def frekans_bulma(self):
#         self.string1 = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
#         kelimeler_sozluk=dict  ()
#
#         for i in self.string1:
#             if i in kelimeler_sozluk:
#                 kelimeler_sozluk[i]+=1
#             else:
#                 kelimeler_sozluk[i]=1
#
#         for kelime,sayi in kelimeler_sozluk.items():
#             print("Kelime: {}, Sayi: {}".format(kelime,sayi))
#
#
# frek1=frek()
# frek1.frekans_bulma()


#Problem2

# class Siir( ):
#     def __init__(self):
#         with open("siir.txt","r",encoding="utf-8") as file:
#             siir_icerigi=file.read()
#             kelimeler=siir_icerigi.split()
#             self.sade_kelimeler=list()
#             for i in kelimeler:
#                 i=i.strip("\n")
#                 i=i.strip("")
#                 self.sade_kelimeler.append(i)
#
#     def birlestir(self,satirlar):
#         birlesik_string=' '.join([satir[0] for satir in satirlar])
#         return birlesik_string
#
#
# siir1=Siir()
# tam_string=siir1.birlestir(siir1.sade_kelimeler)
# print(tam_string)



# #Problem2
# bas_harfler = ""
#
# with open("siir.txt","r",encoding="utf-8") as file:
#     for satır in file:
#         bas_harfler += satır[0]
# print(bas_harfler)


# #probelm3
#
# with open("mailler.txt", "r", encoding="utf-8") as file:
#     for satır in file:
#         satır = satır[:-1]
#         if (satır.endswith(".com") and satır.find("@") != -1):
#             print(satır)

# #Problem4
# isim=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
# soyisim=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
#
# sortlu_isim=sorted(isim)
# info=list (zip(sortlu_isim,soyisim))
# print(info)
#
# for i,j in info:
#     print(i,' ',j )
