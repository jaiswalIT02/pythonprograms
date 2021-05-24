from tkinter import *

root=Tk()

root.title("hello Tarun")
root.geometry("250x140")



from time import strftime

root=Tk()
root.title("Clock")
def time():
    string=strftime("%H:%M:%S %p")
    #label.config(text=string)
    #label.after(1000,time)

label=Label(root,font=("arial",80),background="black",foreground="cyan").pack(anchor="center")

time()

root.mainloop()
