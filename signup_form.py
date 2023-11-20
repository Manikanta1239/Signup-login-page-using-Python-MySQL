from tkinter import *
from datetime import date
from time import strftime
from tkinter import ttk, messagebox
import pymysql, os
import credentials as cr

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")

        self.window.geometry("1350x700+0+0")
        self.window.config(bg = "lightblue")

        frame = Frame(self.window, bg="white")
        frame.grid(padx=350,pady=100)

        def Date():
             string = date.today()
             lbl1.config(text=string)
        lbl1 = Label(frame,font='calibri 15 bold',fg='black',width=15,height=2)
        lbl1.grid(row=0,column=2)
        Date()
        
        title1 = Label(frame, text="Registration Form", font=("Georgia",25,"bold"),bg="white").grid(row=0,column=3)

        def time():
             string = strftime('%I:%M:%S %p')
             lbl.config(text=string)
             lbl.after(1000, time)
        Time=StringVar()
        lbl = Label(frame,font='calibri 15 bold',fg='black',width=15,height=2)
        lbl.grid(row=0,column=5)
        time()
    
        name = Label(frame, text="Name", font=("helvetica",15,"bold"),bg="white").grid(row=1,column=2)
        self.name_txt = Entry(frame,font=("arial"),bg="lightgray")
        self.name_txt.grid(row=1,column=3)

        dob = Label(frame, text="Date of Birth", font=("helvetica",15,"bold"),bg="white").grid(row=2,column=2)
        self.dob_txt = Entry(frame,font=("arial"),bg="lightgray")
        self.dob_txt.grid(row=2,column=3)

        gender = Label(frame, text="Gender", font=("helvetica",15,"bold"),bg="white").grid(row=3,column=2)
        self.gender = ttk.Combobox(frame,font=("helvetica",13),state='readonly',justify=CENTER)
        self.gender['values'] = ("Select","MALE","FEMALE")
        self.gender.grid(row=3,column=3)
        self.gender.current(0)

        email = Label(frame, text="Email", font=("helvetica",15,"bold"),bg="white").grid(row=4,column=2)
        self.email_txt = Entry(frame,font=("arial"),bg="lightgray")
        self.email_txt.grid(row=4,column=3)

        phone =  Label(frame, text="Phone Number", font=("helvetica",15,"bold"),bg="white").grid(row=5,column=2)
        self.phone_txt = Entry(frame,font=("arial"),bg="lightgray")
        self.phone_txt.grid(row=5,column=3)

        password =  Label(frame, text="password", font=("helvetica",15,"bold"),bg="white").grid(row=6,column=2)
        self.password_txt = Entry(frame,show="*",font=("arial"),bg="lightgray")
        self.password_txt.grid(row=6,column=3)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).grid(row=7,column=3)
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="black",fg="red").grid(row=8,column=3)

    def signup_func(self):
        if self.name_txt.get()=="" or self.dob_txt.get()=="" or self.gender.get()=="" or self.email_txt.get()=="" or self.phone_txt.get()=="" or  self.password_txt.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            try:
                connection = pymysql.connect(host="localhost", user="root", password="root", database="student_database")
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s",self.email_txt.get())
                row=cur.fetchone()

                # Check if th entered email id is already exists or not.
                if row!=None:
                    messagebox.showerror("Error!","The email id is already exists, please try again with another email id",parent=self.window)
                else:
                    cur.execute("insert into student_register (name,dob,gender,email,phone_no,password) values(%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.name_txt.get(),
                                        self.dob_txt.get(),
                                        self.gender.get(),
                                        self.email_txt.get(),
                                        self.phone_txt.get(),
                                        self.password_txt.get()
                                    )
                                )
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    self.reset_fields()
            except Exception as es:
                messagebox.showerror("Error!",f"Error due to {es}",parent=self.window)

    def reset_fields(self):
        self.name_txt.delete(0, END)
        self.dob_txt.delete(0, END)
        self.gender.current(0)
        self.email_txt.delete(0, END)
        self.phone_txt.delete(0, END)
        self.password_txt.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()
