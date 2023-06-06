import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root",password='',
    database="python2"
)
mycursor= mydb.cursor()
rno = input("Roll no: ")
nm = input("Name: ")
city = input("City: ")
args = (nm,city,rno)
sql = "Update tbl1 set nm=%s,city=%s where id=%s"
mycursor.execute(sql,args)
print("Record update successfully")
mydb.commit()