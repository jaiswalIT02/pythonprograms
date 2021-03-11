from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)


b1=Button(root,text="Click",font=("Arial",30))
x=1
def show1(e):
    global x
    x=x+1
    if(x%2==0):
        root.configure(background="red")
    else:
        root.configure(background="pink")

b1.bind("<Motion>",show1)
b1.pack()
root.mainloop()