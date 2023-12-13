class Kareler():
    def __init__(self,max=0):
        self.max=max
        self.quvvet=0
    def __iter__(self):
        return self

    def __next__(self):
        if  (self.quvvet<self.max):
            sonuc=2**self.quvvet
            self.quvvet+=1
            return  sonuc
        else:
            self.quvvet=0
            raise StopIteration

kareler1=Kareler(5)

iterator=iter(kareler1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
