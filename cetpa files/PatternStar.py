# Program to print pattern.

num=int(input("Enter Number of rows: "))
for i in range(1,num+1):
    for j in range(1,i+1):
            print("*",end="~")
    print()
