from tkinter import*
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,bg=bg_color,relief=GROOVE,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)


#======================Customer deatails============================
        f1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",fg="gold",bg=bg_color,font=("times new roman",16,"bold"))
        f1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(f1,text="Customer Name",fg="white",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=0,padx=5,pady=20)
        cname_txt=Entry(f1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl=Label(f1,text="Phone No.",fg="white",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=2,padx=5,pady=20)
        cphone_txt=Entry(f1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(f1,text="Customer Name",fg="white",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=4,padx=5,pady=20)
        c_bill_txt=Entry(f1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(f1,text="search",width=10,bd=7,font="arial 12 bold ").grid(row=0,column=6,pady=10,padx=10)


        f2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetic",fg="gold",bg=bg_color,font=("times new roman",16,"bold"))
        f2.place(x=5,y=180,width=315,height=380)

        bath_lbl=Label(f2,text="Bath soap",fg="green",font=("times new roman",15,"bold")).grid(row=0,column=0)
        bath_lbl=Entry(f2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid()


        f3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",fg="gold",bg=bg_color,font=("times new roman",16,"bold"))
        f3.place(x=330,y=180,width=315,height=380)


        
        f4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",fg="gold",bg=bg_color,font=("times new roman",16,"bold"))
        f4.place(x=650,y=180,width=315,height=380)


        
        f5=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill",fg="gold",bg="white",font=("times new roman",16,"bold"))
        f5.place(x=950,y=180,width=400,height=380)


        
        f6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill",fg="gold",bg=bg_color,font=("times new roman",16,"bold"))
        f6.place(x=0,y=560,width=6000,height=150)
root=Tk()
obj=Bill_App(root)
root.mainloop()