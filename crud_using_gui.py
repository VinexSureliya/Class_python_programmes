import tkinter as tk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="crud"
)
mycursor = mydb.cursor()

#UDF
#button
def btn_insert():
    var_id = v_id.get()
    var_name = v_name.get()
    var_city = v_city.get()
    args = (var_id,var_name,var_city)
    mycursor.execute("insert into tbl1 values(%s,%s,%s)",args)
    mydb.commit()
    messagebox.showinfo("Successfull","Record Inserted")

def btn_update():
    var_id = v_id.get()
    var_name = v_name.get()
    var_city = v_city.get()
    args = (var_name,var_city,var_id)
    sql = "Update tbl1 set name=%s,city=%s where id=%s"
    mycursor.execute(sql,args)
    mydb.commit()
    messagebox.showinfo("Successfull","Record Update")

def btn_delete():
    var_id = v_id.get()
    args = (var_id,)
    sql = "delete from tbl1 where id=%s"
    mycursor.execute(sql,args)
    messagebox.showinfo("Successfull","Record Deleted")
    mydb.commit()

def btn_fatch():
    var_id = v_id.get()
    args = (var_id,)
    sql = "select * from tbl1 where id=%s"
    mycursor.execute(sql,args)
    rows = mycursor.fetchall()
    for row in rows:
        print(row[0],"  ",row[1],"  ",row[2])

# Input design

def window_insert():


    lblid = tk.Label(win,text="ID:")
    lblid.place(x=10,y=50)
    txtid = tk.Entry(win,textvariable=v_id)
    txtid.place(x=70,y=50)

    lblname = tk.Label(win,text="Name")
    lblname.place(x=10,y=100)
    txtname = tk.Entry(win,textvariable=v_name)
    txtname.place(x=70,y=100)

    lblcity = tk.Label(win,text="City")
    lblcity.place(x=10,y=150)
    txtcity = tk.Entry(win,textvariable=v_city)
    txtcity.place(x=70,y=150)

    btn = tk.Button(win,text="Insert",command=btn_insert)
    btn.place(x=70,y=200)

def window_update():
    
    lblid = tk.Label(win,text="ID:")
    lblid.place(x=10,y=50)
    txtid = tk.Entry(win,textvariable=v_id)
    txtid.place(x=70,y=50)

    lblname = tk.Label(win,text="Name")
    lblname.place(x=10,y=100)
    txtname = tk.Entry(win,textvariable=v_name)
    txtname.place(x=70,y=100)

    lblcity = tk.Label(win,text="City")
    lblcity.place(x=10,y=150)
    txtcity = tk.Entry(win,textvariable=v_city)
    txtcity.place(x=70,y=150)

    btn = tk.Button(win,text="Update",command=btn_update)
    btn.place(x=70,y=200)

def window_delete():
    lblid = tk.Label(win,text="ID:")
    lblid.place(x=10,y=50)
    txtid = tk.Entry(win,textvariable=v_id)
    txtid.place(x=70,y=50)

    btn = tk.Button(win,text="Delete",command=btn_delete)
    btn.place(x=100,y=90)

def window_fatch():
    lblid = tk.Label(win,text="ID:")
    lblid.place(x=10,y=50)
    txtid = tk.Entry(win,textvariable=v_id)
    txtid.place(x=70,y=50)
    btn = tk.Button(win,text="Display",command=btn_fatch)
    btn.place(x=100,y=90)

#window design

win = tk.Tk()
win.geometry("500x500")

v_id =tk.StringVar()
v_name =tk.StringVar()
v_city =tk.StringVar()

#Menu design

menubar = tk.Menu(win)
insertmenu = tk.Menu(menubar,tearoff=False)
insertmenu.add_command(label="Insert",command=window_insert)
menubar.add_cascade(label="Insert",menu=insertmenu)

updatemenu = tk.Menu(menubar,tearoff=False)
updatemenu.add_command(label="Update",command=window_update)
menubar.add_cascade(label="Update",menu=updatemenu)

deletemenu = tk.Menu(menubar,tearoff=False)
deletemenu.add_command(label="Delete",command=window_delete)
menubar.add_cascade(label="Delete",menu=deletemenu)

fatchmenu = tk.Menu(menubar,tearoff=False)
fatchmenu.add_command(label="Display",command=window_fatch)
menubar.add_cascade(label="Display",menu=fatchmenu)

win.config(menu=menubar)

win.mainloop()