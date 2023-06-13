from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("500x500")
#UDF

def btn_click():
    var_bca = v_bca.get()
    var_bscit = v_bscit.get()
    var_mca = v_mca.get() 
    output = ""
    if var_bca == 1:
        output = "BCA is Selected"
    else:
        output = "BCA is not Selected"
    if var_bscit == 1:
        output += "\nBscit is Selected"
    else:
        output += "\nBscit is not Selected"
    if var_mca == 1:
        output += "\nMCA is Selected"
    else:
        output += "\nMCA is not Selected"
    messagebox.showinfo("Output",output)

v_bca = BooleanVar()
v_bscit = BooleanVar()
v_mca = BooleanVar()   
ckb_bca = Checkbutton(win,text="BCA",variable=v_bca)
ckb_bscit = Checkbutton(win,text="Bscit",variable=v_bscit)
ckb_mca = Checkbutton(win,text="MCA",variable=v_mca)
btn = Button(win,text="Confim",command=btn_click)

ckb_bca.pack()
ckb_bscit.pack()
ckb_mca.pack()
btn.pack()

win.mainloop()