from tkinter import *
from tkinter import ttk

t=Tk()
t.geometry("425x350")
n=ttk.Notebook().place(x=0,y=0,width=425,height=350)

f1=Frame()
n.add(f1,text="Insert")

t.mainloop()