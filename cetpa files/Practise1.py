import pymysql #or import pymysql.cursor
con=pymysql.connect(host="localhost",user="root",password="1234",database="cetpa")
mycursor=con.cursor()
#print(type(cursor))
#print(type(con))
qry="select * from tb1"
mycursor.execute(qry)
heading=mycursor.description #Like Desc <table name> in mysql
data=mycursor.fetchall()
#for id,name,age,mob,city in data:
    #print(id,"\t\t",name,"\t\t",age,"\t\t",mob,"\t\t",city,"\t\t")
for e in heading:
    print(e[0],"\t\t",end="")
print()
for e in data:
    print(e[0],"\t\t",e[1],"\t\t",e[2],"\t\t",e[3],"\t\t",e[4])
#print(data)
#print(heading)

con.close()

