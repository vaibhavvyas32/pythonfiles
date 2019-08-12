#Program for Employee Management System

#BLL
class Employee:
    listemp=[]
    def __init__(self):
        self.id=0
        self.age=0
        self.name=0
        self.type=0 #For Director/Manager/Trainer Type
    def addEmployee(self):
        Employee.listemp.append(self)

    @staticmethod
    def searchEmployee(id):
        for e in Employee.listemp:
            if(e.id==id):
                return e
    @staticmethod
    def deleteEmployee(id):
        for i in Employee.listemp:
            if (i.id==id):
                Employee.listemp.remove(i)
                return 1
        return 0


#Director
class Director(Employee):
    def __init__(self):
        self.share=0
        super().__init__()
    def addEmployee(self):
        super().addEmployee()
#Manager
class Manager(Employee):
    def __init__(self):
        self.area=0
        super().__init__()
    def addEmployee(self):
        super().addEmployee()
#Manager
class Trainer(Employee):
    def __init__(self):
        self.course=0
        super().__init__()
    def addEmployee(self):
        super().addEmployee()





#PL
def showEmployee(y):
    print("Employee ID: ",y.id,"Employee Age: ",y.age,"Employee Name: ",y.name,"Employee Share: ",y.type,end="")
    if (y.type=="Director"):
        print(y.share)
    elif (y.type=="Manager"):
        print(y.area)
    elif (y.type=="Trainer"):
        print(y.course)



while(1):
    ch=input("\n 1. Add Employee \n 2. Search Employee \n 3. Delete Employee \n 4. Modify Employee \n 5. Display All \n 6. Exit \n ")
    if (ch == '1'): #Add Employee
        cht=input("\n 1. Director \n 2. Manager \n 3. Trainer")
        if (cht == '1'): #Add Director
            dir=Director()
            dir.id=input("Enter ID: ")
            dir.age=input("Enter Age: ")
            dir.name=input("Enter Name: ")
            dir.share=input("Enter Share: ")
            dir.type="Director"
            dir.addEmployee()
            print("DIRECTOR ADDED SUCCESSFULLY")
        if (cht == 2): #Add Manager
            mgr=Manager()
            mgr.id=input("Enter ID: ")
            mgr.age=input("Enter Age: ")
            mgr.name=input("Enter Name: ")
            mgr.area=input("Enter Area: ")
            mgr.type="Manager"
            mgr.addEmployee()
            print("MANAGER ADDED SUCCESSFULLY")
        if (cht == 3): #Add Trainer
            tir=Director()
            tir.id=input("Enter ID: ")
            tir.age=input("Enter Age: ")
            tir.name=input("Enter Name: ")
            tir.course=input("Enter Course: ")
            tir.type="Trainer"
            tir.addEmployee()
            print("TRAINER ADDED SUCCESSFULLY")
    elif (ch=='2'): #Search
        id=input("Enter ID: ")
        y=Employee.searchEmployee(id)
        showEmployee(y)
    elif (ch=='3'):
        id=input("Enter ID: ")
        ob=Employee()
        ob.deleteEmployee(id)
        print("Deleted Successfully.")
    #elif (ch=='4'):
    elif (ch=='5'):
        for e in Employee.listemp:
            showEmployee(e)
    elif (ch=='6'):
        break
    else:
        print("Wrong Choice :( ")





