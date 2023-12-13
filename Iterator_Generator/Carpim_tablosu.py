def carpim_tablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{}*{}={}".format(i,j,i*j)


for i in carpim_tablosu():
    print(i)
