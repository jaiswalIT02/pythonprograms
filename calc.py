from tkinter import *

def click(event):
        global scvalue
        text= event.widget.cget("text")
        print(text)
        if text=="=":
            if scvalue.get().isdigit():
                value= int(scvalue.get())
            else:
                value=eval(screen.get())
            scvalue.set(value)
            screen.update()

        elif text=="C":
            scvalue.set("")
            screen.update()
        else:
            scvalue.set(scvalue.get()+text)
            screen.update()
root = Tk()
root.geometry("500x600")
root.title("Calculator by Tarun Jaiswal")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f1=Frame(root, bg="grey")
b= Button(f1, text="9", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="8", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="7", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)
f1.pack()

f1=Frame(root, bg="grey")
b= Button(f1, text="6", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="5", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="4", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)
f1.pack()


f1=Frame(root, bg="grey")
b= Button(f1, text="3", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="2", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="1", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)
f1.pack()

f1=Frame(root, bg="grey")
b= Button(f1, text="0", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="-", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="*", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)
f1.pack()




f1=Frame(root, bg="grey")
b= Button(f1, text="/", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="%", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="=", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)
f1.pack()




f1=Frame(root, bg="grey")
b= Button(f1, text="C", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="00", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b= Button(f1, text="+", font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)
f1.pack()



root.mainloop()