from tkinter import *

root=Tk()
root.geometry("300x300")
root.resizable(0,0)

un=Label(root,text="Enter Name",font="20")
un.pack()
e=Entry(root,font="20")
e.pack()

un=Label(root,text="Enter Password",font="20")
un.pack()
e=Entry(root,show="*",font="20")
e.pack()

b1=Button(root,text="Login",fg="white",bg="red")
b1.pack()

root.mainloop()