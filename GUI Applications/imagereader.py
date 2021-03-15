
 
from tkinter import *
root = Tk()  
root.geometry("400x400") 
  
login_btn = PhotoImage(file = "E:\pythonprograms\GUI Applications\schhol.jpg") 
  
 
img = Button(root, image = login_btn, 
             borderwidth = 0) 
  
img.pack() 
  
 
root.mainloop()