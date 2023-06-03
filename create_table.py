import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python"
)
mycursor = mydb.cursor()
mycursor.execute("create table tbl1(id int(11),nm varchar(20),city varchar(10))")
print("Table created successfully...")