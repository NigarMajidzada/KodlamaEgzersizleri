sayi1= int(input("Lutfen sayi1-i giriniz: "))
sayi2= int(input("Lutfen sayi2-i giriniz: "))

islem = int(input("Lutfen  isleminizi giriniz: "))

if(islem==1):
    print("Islem 1 secildi: {} ".format(sayi1+sayi2))
elif(islem==2):
    print("Islem 2 secildi: {} ".format(sayi1-sayi2))
elif(islem==3):
    print("Islem 3 secildi: {} ".format(sayi1*sayi2))
elif(islem==4):
    print("Islem 4 secildi: {} ".format(sayi1/sayi2))
else:
    print("Gecersiz islem")
