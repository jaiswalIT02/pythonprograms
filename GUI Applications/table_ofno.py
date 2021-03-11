from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)

x=IntVar()

e1=Entry(root,font=("Arial",25),textvariable=x)
e1.pack()

# Sum of two integer
def show(op):
    a=x.get()
    for i in range(1,11):
        print(i*a,end=",")




b1=Button(root,text="Click",font=("Arial",25),command=lambda:show(1))
b1.pack()



root.mainloop()