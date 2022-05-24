class class1: #Super Parent
    def __init__(self):
        self.a=1
        self.b=2
    def showdata(self):
        print(self.a,self.b,self.c,self.d,self.e,self.f)
class class2(class1): #Class 2 inheriting from class 1.
    def __init__(self):
        self.c=3
        self.d=4
        super().__init__()
class class3(class2): #Class 3 inheriting from Class 2 & 1
    def __init__(self):
        self.e=5
        self.f=6
        super().__init__()
ob2=class3()
ob2.showdata()