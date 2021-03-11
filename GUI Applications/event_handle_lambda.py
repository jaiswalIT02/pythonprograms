from tkinter import *
root=Tk()
root.geometry("400x400")
root.resizable(0,0)

show1=lambda e:root.configure(background="red")
show2=lambda e:root.configure(background="green")
show3=lambda e:root.configure(background="blue")


b1=Button(root,text="click",command=show1)
b1.bind("<Button-1>",show1)#We can use Double in the place of Button.
b1.bind("<Button-2>",show2)
b1.bind("<Button-3>",show3)
b1.pack()


root.mainloop()