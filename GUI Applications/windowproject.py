from tkinter import *
t=Tk()
t.geometry("425x350")

def login():
    f2=Frame(bg="#091e42")
    f2.place(x=0,y=0,width=425,height=350)
    u1=Label(f2,font=("",12),text="Login Page",bg="#091e42",fg="white").place(x=150,y=20)
    e1=Entry(f2,font=("",12)).place(x=200,y=80,width=120)

    u1=Label(f2,font=("",12),text="Enter Name:",bg="#091e42",fg="white").place(x=100,y=80)
    e1=Entry(f2,font=("",12)).place(x=200,y=80,width=120)

    u2=Label(f2,font=("",12),text="Enter Pass:",bg="#091e42",fg="white").place(x=100,y=130)
    e2=Entry(f2,font=("",12),show="*").place(x=200,y=130,width=120)
    
    #e2=Entry(f2)
    #e2.pack()
    b2=Button(f2,text="Login").place(x=200,y=200)
    
    b3=Button(f2,text="<-",command=home).place(x=2,y=3)
    
def register():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=425,height=350)

    u1=Label(f1,font=("",12),text="Registration Page",bg="#091e42",fg="white").place(x=150,y=20)
    e1=Entry(f1,font=("",12)).place(x=200,y=80,width=120)

    u1=Label(f1,font=("",12),text="Enter Name:",bg="#091e42",fg="white").place(x=100,y=80)
    e1=Entry(f1,font=("",12)).place(x=200,y=80,width=120)

    
    u2=Label(f1,font=("",12),text="Enter Email:",bg="#091e42",fg="white").place(x=100,y=130)
    e2=Entry(f1,font=("",12)).place(x=200,y=130,width=120)

    u3=Label(f1,font=("",12),text="Enter Pass:",bg="#091e42",fg="white").place(x=100,y=180)
    e3=Entry(f1,font=("",12),show="*").place(x=200,y=180,width=120)

    b2=Button(f1,text="Regis").place(x=200,y=240)
    
    b3=Button(f1,text="<-",command=home).place(x=2,y=3)
    
def home():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=425,height=350)

    b1=Button(f1,text="Login",command=login)
    b1.place(x=100,y=50,width=80,height=30)
    b2=Button(f1,text="Register",command=register)
    b2.place(x=200,y=50,width=80,height=30)

home()


t.mainloop()
