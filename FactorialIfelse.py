# Program for factorial of a number.

def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)

num=int(input("Enter Number: "))

if (num<0):
    print("INVALID")
elif (num==0):
    print("Zero")
else:
    print("Factorial is ",fact(num))
