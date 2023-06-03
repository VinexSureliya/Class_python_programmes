import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="python"
    )
    mycursor = mydb.cursor()
    mycursor.execute("insert into tbl1 values(4,'viraj','junagadh')")
    print("record inserted sucessfully...")
except:
    print("Error")

mycursor.execute("Select * from tbl1")
rows = mycursor.fetchall()
for row in rows:
    print(row[0],"  ",row[1],"  ",row[2])