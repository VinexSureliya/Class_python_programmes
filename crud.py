import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='',
    database='python2'
)
mycursor = mydb.cursor()
print("insert")
print("----------------------------------")
rno = input("Roll no:")
name = input("Name:")
city = input("City:")
args = (rno,name,city)
mycursor.execute("insert into tbl1 values(%s,%s,%s)",args)
print()
print("record inserted sucessfully...")
mydb.commit()

print("select ")
print("----------------------------------")
mycursor.execute("select * from tbl1")
rows = mycursor.fetchall()
for row in rows:
    print(row[0],"  ",row[1],"  ",row[2])
print("select specific record")
print("----------------------------------")
rno = input("Roll no: ")
args = (rno,)
sql = "select * from tbl1 where id=%s"
mycursor.execute(sql,args)
rows = mycursor.fetchall()
for row in rows:
    print(row[0],"  ",row[1],"  ",row[2])
print("Update")
print("----------------------------------")
rno = input("Roll no: ")
nm = input("Name: ")
city = input("City: ")
args = (nm,city,rno)
sql = "Update tbl1 set nm=%s,city=%s where id=%s"
mycursor.execute(sql,args)
print("Record update successfully")
mydb.commit()

print("Delete")
print("----------------------------------")
rno = input("Roll no: ")
args = (rno,)
sql = "delete from tbl1 where id=%s"
mycursor.execute(sql,args)
print("Record Deleted successfully")
mydb.commit()