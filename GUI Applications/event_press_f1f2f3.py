from tkinter import *
root=Tk()
root.geometry("400x400")
root.resizable(0,0)




root.bind("<F1>",lambda e:root.configure(background="pink"))#We can use Double in the place of Button.
root.bind("<F2>",lambda e:root.configure(background="cyan"))
root.bind("<F3>",lambda e:root.configure(background="green"))
root.bind("<Delete>",lambda e:root.configure(background="white"))
  



root.mainloop()