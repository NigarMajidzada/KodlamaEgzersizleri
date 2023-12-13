print("""**********************
Fatoriel Bulam Programi

Not: Cikmak icin "Q"-ya basiniz.
**********************""")

while True:
    sayi=input("Lutfen sayi giriniz. ")
    if  (sayi=="Q"):
        print("Program sona erdi...")
        break
    else:
        sayi=int(sayi)
        faktoriel=1
        for i in range(2,sayi+1):
            faktoriel*=i
        print("Faktoriel ",faktoriel)