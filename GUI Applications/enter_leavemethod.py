from tkinter import *
root=Tk()
root.geometry("400x400")
root.resizable(0,0)




b1=Button(root,text="click")
b1.bind("<Enter>",lambda e:root.configure(background="pink"))
#We can use Double in the place of Button.
b1.bind("<Leave>",lambda e:root.configure(background="cyan"))

b1.pack()


root.mainloop()