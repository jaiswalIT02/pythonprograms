from tkinter import *
root=Tk()
root.geometry("400x400")
root.resizable(0,0)

def show1():
    root.configure(background="red")

def show2():
    root.configure(background="green")

def show3():
    root.configure(background="blue")


b1=Button(root,text="click",command=show1)
b1.pack()

b2=Button(root,text="click",command=show2)
b2.pack()

b3=Button(root,text="click",command=show3)
b3.pack()

root.mainloop()