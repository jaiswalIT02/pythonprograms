from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar

t=Tk()
t.title("Tarun Jaiswal")
t.geometry("425x300")
t.resizable(0,0)

t.configure(background="black")#back ground color

a=StringVar()
def show(c):
    a.set(a.get()+c)


def equal():
    x=a.get()
    a.set(eval(x))

def clear():
    a.set("")
    

e1=Entry(font=("",30),justify="right",textvariable=a)
e1.place(x=0,y=0,width=425,height=50)

b=[Button()]*16
data=["7","8","9","+","4","5","6","-","1","2","3","*","C","0","=","/"]
k=0
x=5
y=55
for i in range(4):
    for j in range(4):
        b[k]=Button(text="8",font=("",25),bg="gray",fg="white",activebackground="yellow",command=show)
        b[k].place(x=x,y=y,width=100,height=50)
        k+=1
        k+=105
    x=5
    y+=55


t.mainloop()