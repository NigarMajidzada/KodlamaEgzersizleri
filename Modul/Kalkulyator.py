from riyaziyyat import *
print("Calculator")
print("""1.Cem(+)
2.Cixma(-)
3.Vurma(*)
4.Bolem(//)
5.Quvvet
0.Cixis""")

emeliyyat=int(input("Emeliyyati secin: "))
if(emeliyyat!=0):
    eded1=int(input("eded1: "))
    eded2=int(input("eded2: "))

while True:
    if(emeliyyat==1):
            print(f"Cem:{cem(eded1,eded2)}")
            break
    elif(emeliyyat==2):
            print(f"Cixma: {ferq(eded1,eded2)}")
            break
    elif(emeliyyat==3):
        print(f"Vurma: {hasil(eded1,eded2)}")
    elif(emeliyyat==4):
        if(eded2==0):
            print("Error: 0-a bolme")
            break
        print(f"Bolme: {bolme(eded1,eded2)}")
        break
    elif(emeliyyat==5):
        print(f"Quvvet: {quvvet(eded1,eded2)}")
        break
    if(emeliyyat==0):
        print("Cixis...")
        break
