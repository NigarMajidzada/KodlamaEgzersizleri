class Kuvvet3():

    def __init__(self,max=0):
        self.max=max
        self.kuvvet=0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.kuvvet<self.max):
            sonuc=3**self.kuvvet
            self.kuvvet+=1
            return sonuc
        else:
            self.kuvvet=0 # Ikinci kullanimda yeniden baslaya bilmesi icin
            raise StopIteration

kuvvet1=Kuvvet3(6)
iterator=iter(kuvvet1)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for i in kuvvet1:
    print(i)

for j in kuvvet1:
    print(j)
