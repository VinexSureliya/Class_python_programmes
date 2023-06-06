import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root",password='',
    database="python2"
)
mycursor= mydb.cursor()
rno = input("Roll no: ")
args = (rno,)
sql = "delete from tbl1 where id=%s"
mycursor.execute(sql,args)
print("Record Deleted successfully")
mydb.commit()