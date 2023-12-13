'''2-ci dereceden kon tapmaq ucun  dustur
dustir:  ax^2+bx+c
detayli hesapmama: b**2 -4 4*c*c

birinci kok: (-b-delta**0.5)/(2*a)
ikinci kok: (-b+delta**0.5)/(2*a)
'''
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))

delta=b**2-4*a*c

x1=(-b-delta**0.5)/(2*a)
x2=(-b+delta**0.5)/(2*a)

print("Birinci Kok: {}\nIkinci kok: {}\n".format(x1,x2))