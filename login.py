import tkinter
from tkinter import messagebox
import Database

win = tkinter.Tk()
win.geometry("500x500")

#UDF

def login():
        Username = v_user
        Password = v_password

        if v_user != Username and v_password != Password:
                messagebox.showinfo("Error","Login Failed")
        else:
                messagebox.showinfo("Successful","Login Successfully...")
#decler variable

v_user = tkinter.StringVar()
v_password = tkinter.StringVar()

#Design

lblusername = tkinter.Label(win,text="Username:")
lblusername.place(x=10,y=50)
lblpassword = tkinter.Label(win,text="Password:")
lblpassword.place(x=10,y=90)

txt1 = tkinter.Entry(win,textvariable=v_user)
txt1.place(x=100,y=50)

txt2 = tkinter.Entry(win,textvariable=v_password)
txt2.place(x=100,y=90)

btn = tkinter.Button(win,text="Login",command=login)
btn.place(x=125,y=120)
win.mainloop()