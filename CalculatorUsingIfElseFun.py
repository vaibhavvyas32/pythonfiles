# Program for calculator using functions & if else.

def add():
    add=a+b
    return add
def sub():
    sub=a-b
    return sub
def mul():
    mul=a*b
    return mul
def div():
    div=a/b
    return div
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=input("Enter the operators add/sub/mul/div: ")
if (c=="add"):
    c=add()
    print(c)
elif (c=="sub"):
    c=sub()
    print(c)
elif (c=="mul"):
    c=mul()
    print(c)
else:
    c=div()
    print(c)