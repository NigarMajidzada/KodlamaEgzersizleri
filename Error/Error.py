# #Problem 1
# liste = ["345","sadas","324a","14","kemal",456]
#
# for i in liste:
#     try:
#         i=int(i)
#         print(i)
#     except:
#         pass
#Problem2
# def tekcift():
#     sayi=int(input("Sayi: "))
#     if(sayi%2==0):
#         print(sayi)
#         return sayi
#     else:
#       raise  ValueError ("Bu sayi cift deyil")

# def tekcift():
#     sayi=int(input("Sayi: "))
#     list=[]
#     list.append(sayi)
#     try:
#         for i in list:
#             if (i%2==0):
#                 print(i)
#             else:
#                 raise ValueError
#     except:
#         raise ValueError("Bu cift sayi deyil")
#
# tekcift()


def tekcift():
    sayi=int(input("Sayi: "))
    try:
            if (sayi%2==0):
                print("Bu sayi cift")
            else:
                raise ValueError
    except:
        raise ValueError("Bu cift sayi deyil")

tekcift()
