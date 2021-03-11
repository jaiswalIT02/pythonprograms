from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)

x=IntVar()
y=IntVar()
z=IntVar()

e1=Entry(root,font=("Arial",25),textvariable=x)
e1.pack()
e2=Entry(root,font=("Arial",25),textvariable=y)
e2.pack()

# Sum of two integer
def show():
    a=x.get()
    b=y.get()
    c=a+b
    z.set(c)

def show1():
    a=x.get()
    b=y.get()
    c=a-b
    z.set(c)

def show2():
    a=x.get()
    b=y.get()
    c=a*b
    z.set(c)

b1=Button(root,text="Sum",font=("Arial",25),command=show)
b1.pack()

b2=Button(root,text="Sub",font=("Arial",25),command=show1)
b2.pack()

b3=Button(root,text="Multiply",font=("Arial",25),command=show2)
b3.pack()

e3=Entry(root,font=("Arial",25),textvariable=z)
e3.pack()

root.mainloop()