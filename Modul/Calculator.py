import math
from math import *
print("Calculator")
print("""1.Addition(+)
2.Subtraction(-)
3.Multiplication(*)
4.Division(//)
5.Square Root (sqrt)
0.Exit""")

operation=int(input("Select operation: "))
if(operation!=0):
    number1=int(input("Number1: "))
    number2=int(input("Number2: "))

while True:
    if(operation==1):
            print(f"Sum: {number1+number2}")
            break
    elif(operation==2):
            print(f"Subtraction: {number1-number2}")
    elif(operation==3):
        print(f"Multiplication: {number1*number2}")
    elif(operation==4):
        if(number2==0):
            print("Error: Division by zero.")
            break
        print(f"Division: {number1//number2}")
        break
    elif(operation==5):
        print(f"SQRT: {number1**number2}")
        break
    if(operation==0):
        print("Exit...")
        break
