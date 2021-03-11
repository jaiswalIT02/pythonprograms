from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)

# Sum of two integer
def show(b):
    b["fg"]="white"
    b["bg"]="black"
    b["text"]="Champak Sir"


b1=Button(root,text="Click",font=("Arial",25),command=lambda:show(b1))
b1.pack()



root.mainloop()