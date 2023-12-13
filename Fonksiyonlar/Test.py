# Problem3

from functools import reduce

def cift_mi(sayi):
    return sayi%2==0

# def toplama(x, y):
#     return x+y

liste=[1,2,3,4,5,6,7,8,9,10]
cift_list=list(filter(cift_mi,liste))


print(cift_list)
#
print(reduce(sum(cift_list),cift_list))
