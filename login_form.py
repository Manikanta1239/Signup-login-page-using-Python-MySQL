from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import os
from signup_form import SignUp
import credentials as cr

class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("Python Registration login")
        # Set the window size
        # Here 0,0 represents the starting point of the window 
        self.window.geometry("1350x700+0+0")
        self.window.config(bg = "white")

        #============================================================================
        #==============================DESIGN PART===================================
        #============================================================================

        self.frame1 = Frame(self.window, bg="lightblue")
        self.frame1.place(x=0, y=0, width=450, relheight = 1)

        label1 = Label(self.frame1, text= "LOGIN TO COURSE", font=("times new roman",25, "bold"), bg="white", fg="blue").place(x=50,y=300)
        label3 = Label(self.frame1, text= "It's all about your skill's", font=("times new roman", 15, "bold"), bg="white", fg="brown4").place(x=100,y=360)

        #=============Entry Field & Buttons============

        self.frame2 = Frame(self.window, bg = "gray95")
        self.frame2.place(x=450,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140,y=150,width=500,height=450)

        self.email_label = Label(self.frame3,text="Email Address", font=("helvetica",20,"bold"),bg="white", fg="gray").place(x=50,y=40)
        self.email_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.email_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3,text="Password", font=("helvetica",20,"bold"),bg="white", fg="gray").place(x=50,y=120)
        self.password_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="white",fg="gray",show="*")
        self.password_entry.place(x=50, y=160, width=300)

        #================Buttons===================
        self.login_button = Button(self.frame3,text="Log In",command=self.login_func,font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=50,y=200,width=300)

        self.forgotten_pass = Button(self.frame3,text="Forgotten password?",command=self.forgot_func,font=("times new roman",10, "bold"),bd=0,cursor="hand2",bg="white",fg="blue").place(x=125,y=260,width=150)

        self.create_button = Button(self.frame3,text="Create New Account",command=self.redirect_window,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=80,y=320,width=250)


    def login_func(self):
        if self.email_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)
        else:
            try:
                connection=pymysql.connect(host="localhost", user="root", password="root", database="student_database")
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and password=%s",(self.email_entry.get(),self.password_entry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!","Invalid USERNAME & PASSWORD",parent=self.window)
                else:
                    messagebox.showinfo("Success","Welcome to PYTHON WORLD'S family",parent=self.window)
                    # Clear all the entries
                    self.reset_fields()
                    
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def forgot_func(self):
        if self.email_entry.get()=="":
            messagebox.showerror("Error!", "Please enter your Email Id",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host="localhost",  user="root",  password="root",  database="student_database")
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s", self.email_entry.get())
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "Email Id doesn't exists")
                else:
                    connection.close()
                    
                    #=========================SECOND WINDOW===============================
                    #------------Toplevel:create a window top of another window-----------
                    #------------focus_force:Helps to to focus on the current window------
                    #-----Grab:Helps to grab the current window until user ungrab it------

                    self.root=Toplevel()
                    self.root.title("Forget Password?")
                    self.root.geometry("400x440")
                    self.root.config(bg="white")
                    self.root.focus_force()
                    self.root.grab_set()

                    title3 = Label(self.root,text="Change your password",font=("times new roman",15,"bold"),bg="white").grid(row=0,column=3)

                    phone =  Label(self.root, text="Phone Number", font=("times new roman",10,"bold"),bg="white").grid(row=1,column=2)
                    self.phone_txt = Entry(self.root,font=("arial"),bg="lightgray")
                    self.phone_txt.grid(row=1,column=3)

                    title7 = Label(self.root, text="New Password", font=("times new roman", 10, "bold"), bg="white").grid(row=2,column=2)
                    self.new_pass = Entry(self.root,font=("arial"))
                    self.new_pass.grid(row=2,column=3)

                    self.create_button = Button(self.root,text="Submit",command=self.change_pass,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").grid(row=3,column=3)
                    #=========================================================================

            except Exception as e:
                messagebox.showerror("Error", f"{e}")
                
      
    def change_pass(self):
        if self.email_entry.get() == "" or self.phone_txt.get()=="" == "Select" or self.new_pass.get() == "":
            messagebox.showerror("Error!", "Please fill the all entry field correctly")
        else:
            try:
                connection = pymysql.connect(host="localhost",  user="root",  password="root",  database="student_database")
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and phone_no=%s",(self.email_entry.get(),self.phone_txt.get()))
                row=cur.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "Please fill the all entry field correctly")
                else:
                    try:
                        cur.execute("update student_register set password=%s where email=%s", (self.new_pass.get(),self.email_entry.get()))
                        connection.commit()

                        messagebox.showinfo("Successful", "Password has changed successfully")
                        connection.close()
                        self.reset_fields()
                        self.root.destroy()

                    except Exception as er:
                        messagebox.showerror("Error!", f"{er}")
                        
            except Exception as er:
                        messagebox.showerror("Error!", f"{er}")
            

    def redirect_window(self):
        self.window.destroy()
        # Importing the signup window.
        # The page must be in the same directory
        root = Tk()
        obj = SignUp(root)
        root.mainloop()

    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)
# The main function
if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()
