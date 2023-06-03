import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python"
)
mycursor = mydb.cursor()
mycursor.execute("Select * from tbl1")
rows = mycursor.fetchall()
for row in rows:
    print(row[0],"  ",row[1],"  ",row[2])