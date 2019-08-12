import pymysql
con=pymysql.connect(host="localhost",id="root",password="1234",database="cetpa")
mycursor=con.cursor()