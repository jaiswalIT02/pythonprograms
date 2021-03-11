from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)


e1=Entry(root,font=("Arial",25))
e1.pack()

def show():
    s=e1.get()
    print(s)

b1=Button(root,text="click",font=("Arial",25),command=show)
b1.pack()
root.mainloop()