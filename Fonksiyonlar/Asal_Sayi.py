print("""************************
 Asal sayi bulma Programi
 ************************""")
def asal_mi(sayi):
    for i in range(2,sayi):
        if  (sayi%i==0):
            return False
    return True

while True:
    sayi=input("Sayi ")
    if  (sayi=='q'):
        print("Programdan cikilir")
        break
    sayi=int(sayi)
    if(sayi==1):
        print("Asal bir sayidir. ")
    elif(sayi==2):
        print("Asal bir sayidir")
    else:
        if  (asal_mi(sayi)):
            print("Asal bir sayidir")
        else:
            print("Asal bir sayi deyildir")
