from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)

x=IntVar()  # Here we can use also Doublevar to get float type data.
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

b1=Button(root,text="Sum",font=("Arial",25),command=show)
b1.pack()

e3=Entry(root,font=("Arial",25),textvariable=z)
e3.pack()

root.mainloop()