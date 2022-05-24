#To Make CMS Using Constructor.

#BLL

class customer:
    listcus=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
    def addCust(self):
        customer.listcus.append(self)
    def searchCust(id):
        for e in customer.listcus:
            if (e.id==id):
                self.age = e.age
                self.name = e.name
                return 1
        return 0
    @staticmethod
    def deleteCustomer(id):
        if (e.id==id):
            customer.listcus.remove(e)
    def modifyCustomer(self):
        for e in customer.listcus:
            if (e.id==self.id):
                    e.age=self.age
                    e.name=self.name



#PL
while(1):
    print("Welcome to CMS v2")
    ch=input("\n 1. Add Customer \n 2. Search Customer \n 3. Delete Customer \n 4. Modify Customer \n 5. Show All Customers \n 6. Exit \n")
    if (ch=="1"):
        cus=customer()
        cus.id=input("Enter ID: ")
        cus.age=input("Enter Age: ")
        cus.name=input("Enter Name: ")
        cus.addCust()
        print("Printed Successfully.")
    elif (ch=='2'):
        cus=customer()
        cus.id=input("Enter ID: ")
        flag=cus.searchCustomer()
        if (flag==1):
            showCustomer(cus)
        else:
            print("Customer not found.")
    elif (ch=="3"):
        id=input("Enter ID: ")
        customer.deleteCustomer(id)
    elif (ch=="4"):
        cus=customer()
        cus.id = input("Enter ID: ")
        cus.age = input("Enter Age: ")
        cus.name = input("Enter Name: ")
        cus.modifyCustomer()
        print("Modified Successfully.")
    elif (ch=="5"):
        def showCustomer(cus):
            print("ID:",cus.id,"Age:",cus.age,"Name",cus.name)
            for e in customer.listcus:
                showCustomer(e)
    elif (ch=="6"):
        break
    else:
        print("Wrong Choice")






