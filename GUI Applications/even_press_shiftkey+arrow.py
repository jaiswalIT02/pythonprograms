from tkinter import *
root=Tk()
root.geometry("400x400")
root.resizable(0,0)



root.bind("<Shift-Up>",lambda e:root.configure(background="pink"))#We can use Double in the place of Button.
root.bind("<Shift-Down>",lambda e:root.configure(background="cyan"))#if we wnat use no as thisfunction key we type only no without angular baracket.
root.bind("<Shift-Left>",lambda e:root.configure(background="green"))
root.bind("<Shift-Right>",lambda e:root.configure(background="red"))

root.bind("<Delete>",lambda e:root.configure(background="white"))




root.mainloop()








