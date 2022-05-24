#To Make CMS Using Constructor.

#BLL
import pymysql
class customer:
    con = pymysql.connect(host="localhost", user="root", password="1234", database="cetpa")
    mycursor = con.cursor()
    listcus=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
    def addCust(self):
        customer.listcus.append(self)
        qry="insert into cust values('%s','%s','%s')"%(self.id,self.name,self.age)
        customer.mycursor.execute(qry)
        customer.con.commit()
    def searchCust(self):
        qry="select * from cust where id=%s"%(self.id)
        customer.mycursor.execute(qry)
        data=customer.mycursor.fetchone()
        return data
        

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
        data=cus.searchcust()
        print("Cust ID: ",data[0],"cust name",data[1],"cust age",data[2])
    elif (ch=="3"):
        cus=customer()
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






