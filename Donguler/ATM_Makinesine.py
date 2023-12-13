print("""******************************
       ATM  Makinesine Hisgeldiniz
       
       1 Bakiye Sorgulama
       2 Para Yatirma
       3 Para Cekme
         Programdan Cikmak icin "Q" basiniz.
      ********************************""")

bakiye=1000
while True:
    islem=input("Islemi seciniz...")
    if  (islem=="Q"):
        print("Yine Bekleriz...")
        break
    elif (islem=="1"):
        print("Bakiyeniz {} tl dir".format(bakiye))
    elif(islem=="2"):
        miktar=int(input("Miktarinizi giriniz: "))
        bakiye+=miktar
        print("Yeni Bakiye {} tl dir ".format(bakiye))
    elif(islem=="3"):
        miktar = int(input("Miktarinizi giriniz: "))
        if(bakiye<miktar):
            print("Hesabinizda yeteri kadar para yok...")
            continue
        bakiye -= miktar
        print("Yeni Bakiye {} tl dir ".format(bakiye))
    else:
        print("Gecersiz islem")

