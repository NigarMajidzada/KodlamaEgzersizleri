def not_hesaplama(satir ):
    satir=satir[:-1]
    liste=satir.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])

    son_not=not1*(3/10)+not2*(3/10)+not3*(4/10)

    if  (son_not>90):
        harf="AA"
    elif( son_not>85):
        harf="AB"
    elif (son_not > 80):
        harf = "BB"
    elif (son_not > 75):
        harf = "CB"
    elif (son_not > 70):
        harf = "CC"
    elif (son_not > 65):
        harf = "DC"
    elif (son_not > 60):
        harf = "DD"
    elif (son_not > 50):
        harf = "FD"
    else:
        harf="FF"

    return isim+"---------------------->"+harf+"\n"


with open("Dosya","r",encoding="utf-8") as file:
    eklenecekler=[]
    for i in file:
        eklenecekler.append(not_hesaplama(i))
    print(eklenecekler)


with open("notlar.txt","w",encoding="utf-8") as file2:
    for i in eklenecekler:
        file2.write(i)

with open("kalanlar.txt","w",encoding="utf-8") as file3:
    for i in eklenecekler:
        file3.write(i)
