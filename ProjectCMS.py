#BLL

listid=[]
listname=[]
listage=[]

def addCust(id,age,name):
    listid.append(id)
    listage.append(age)
    listname.append(name)
def searchCust(id):
    if (listid.count(id)==0):
        return None
    else:
        index=listid.index(id)
        return index
def deleteCust(id):
    if (listid.count(id)==0):
        return None
    else:
        index=listid.index(id)
        listid.pop(index)
        listage.pop(index)
        listname.pop(index)
def modifyCust(id,age,name):
    if (listid==0):
        return False
    else:
        index=listid.index(id)
        listage[index]=age
        listname[index]=name
        return True





#PL

print("Welcome to CMS")
while(1):
    print(" 1. Add Customer \n 2. Search Customer \n 3. Delete customer \n 4. Modify Customer \n 5. Display all \n 6. Exit")
    ch=int(input("Enter option number: "))
    if (ch==1): #Add Customer
        id=input("Enter Cust ID: ")
        age=input("Enter Cust age: ")
        name=input("Enter Cust Name: ")
        addCust(id,age,name)
        print("Customer added successfully")
    elif (ch==2): #Search Customer
        id=input("Enter Cust ID: ")
        index=searchCust(id)
        if (index==None):
            print("Incorrect ID inserted")
        else:
            def showCust(index):
                print("custid:", listid[index], "custage: ", listage[index], "custname: ", listname[index])
            showCust(index)
    elif (ch==3): #Delete
        id=input("Enter Cust ID: ")
        deleteCust(id)
        if (name==None):
            print("ID not found.")
        else:
            print("ID ",id,"with name",name,"Deleted Successfully.")
    elif (ch==4): #Modify Customers
        id=input("Enter Cust ID to modify: ")
        age=input("Enter Modified age: ")
        name=input("Enter Modified name: ")
        flag=modifyCust(id,age,name)
        if (flag==False):
            print("Incorrect ID")
        else:
            print("Customer ID modified successfully.")
    elif (ch==5): #show all customers
        for index in range(len(listid)):
            print("Cust ID : ",listid[index],"Age: ",listage[index],"Name: ",listname[index])
    elif (ch==6): #Break
        break
    else:
        print("Incorrect Option.")




