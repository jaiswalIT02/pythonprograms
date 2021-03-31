from tkinter import *

t=Tk()
t.title("My IDE")
 
a=StringVar()
def show():
    print(a.get())

s1=Spinbox(font=("",15),textvariable=a,from_=0,to=100).pack()
b1=Button(text="Click",font=("",15),command=show).pack()

t.geometry("400x400")
t.mainloop()