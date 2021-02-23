from tkinter import *
root=Tk()


frame=Frame(root,width=300, height=300)
button1=Button(frame,text="button 1")
button2=Button(frame,text="button 2")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
frame.pack()

root.mainloop()