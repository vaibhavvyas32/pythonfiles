import pymysql #or import pymysql.cursor
con=pymysql.connect(host="localhost",user="root",password="1234",database="cetpa")
mycursor=con.cursor()
id=input("Enter ID: ")
name=input("Enter Name: ")
age=input("Enter age: ")
mob=input("Enter Mobile no: ")
city=input("Enter City: ")
qry="insert into tb1 values('%s','%s','%s','%s','%s')"%(id,age,name,mob,city)
mycursor.execute(qry)
con.commit()
print(mycursor.mogrify(qry)) #Tell what query will go in database