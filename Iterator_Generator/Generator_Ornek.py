def finobacci():
    a=1
    b=1
    yield a
    yield b

    while True:
        a,b=b,a+b
        yield b

for sayi in finobacci():
    if  (sayi>100000):
        break
    else:
        print(sayi)
