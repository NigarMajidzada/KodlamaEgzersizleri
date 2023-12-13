#generator kullanmadan
def kareleri_al():
    sonuc=[]
    for i in range(1,6):
        sonuc.append(i**2)
    return sonuc
# print(kareleri_al())

#generatorla

def kareleri_al2():
    for i in range(1,6):
        yield i**2

generator=kareleri_al2()
print(generator)
iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
