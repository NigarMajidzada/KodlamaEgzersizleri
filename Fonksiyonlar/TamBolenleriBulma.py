print("""********************
Tam Bolenleri Bulma
********************""")

def tambolebenbulma(sayi):
    bolen_listesi=[]
    for i in range(1,sayi+1):
        if(sayi%i==0):
            bolen_listesi.append(i)
    return  bolen_listesi

while True:
    sayi=input("Sayi giriniz:")
    if(sayi=='q'):
        print("Programdan cikiliyor...")
        break
    else:
        sayi=int(sayi)
        print("Tam bolenler: ",tambolebenbulma(sayi))