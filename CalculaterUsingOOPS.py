#Making Calculator Using OOPS

#BLL

import operator
class class1:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
    def add(self):
        self.z=operator.add(self.x,self.y)
    def sub(self):
        self.z=operator.sub(self.x,self.y)
    def mul(self):
        self.z=operator.mul(self.x,self.y)
    def div(self):
        self.z=operator.div(self.x,self.y)
    def power(self):
        self.z=operator.pow(self.x,self.y)

#PL

ob=class1()
print("Welcome To Simple Calculator v2")
garb=input("\n 1. Start \n 2. Exit")
if (garb=='1'):
    while(1):
        ob.x=int(input("Enter First No: "))
        ob.y=int(input("Enter Second No: "))
        ch=input("\n 1. Add (+) \n 2. Subtract (-) \n 3. Multiply (*) \n 4. Divide (/) \n 5. Power (**) \n")
        if (ch=='1'or '+'):
            ob.add()
            print(ob.z)
        elif (ch=='2'or'-'):
            ob.sub()
            print(ob.z)
        elif (ch=='3'or'*'):
            ob.mul()
            print(ob.z)
        elif (ch=='4'or'/'):
            ob.div()
            print(ob.z)
        elif (ch=='5'or'**'):
            ob.power()
            print(ob.z)
        else:
            print("Wrong Keyword inserted")
else:
    print("Invalid Keyword inserted.")


