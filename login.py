import tkinter as tk
import tkinter.messagebox
import sqlite3

connection=sqlite3.connect("credentials.db")
cursor=connection.cursor()
#sql_command="""CREATE TABLE cred(
#username VARCHAR(15) PRIMARY KEY,
#email VARCHAR(45),
#password VARCHAR(55))"""
#cursor.execute(sql_command)    

win=tk.Tk()
win.configure(bg='#333333')
win.minsize(455,315)
frame=tk.Frame(bg='#333333', pady=55)

def tab_login():
    def tab_register():
        login_label.destroy()
        us.destroy()
        username.destroy()
        pa.destroy()
        password.destroy()
        login_button.destroy()
        signup_label.destroy()
        tab_register_button.destroy()

        def back_button():
            tab_login()
            register_label.destroy()
            us1.destroy()
            username1.destroy()
            em1.destroy()
            email.destroy()
            n_pa.destroy()
            n_password.destroy()
            c_pa.destroy()
            c_password.destroy()
            register_button.destroy()
            al_login_label.destroy()
            tab_login_button.destroy()

        register_label=tk.Label(frame,text="Create a new account", bg='#333333', fg='#ffffff', font=('Arial',20))
        us1=tk.Label(frame, text="Username", bg='#333333', fg='#ffffff', font=('Arial',15))
        username1=tk.Entry(frame, font=('Arial',15))
        em1=tk.Label(frame, text="Email ID", bg='#333333', fg='#ffffff', font=('Arial',15))
        email=tk.Entry(frame, font=('Arial',15))
        n_pa=tk.Label(frame,text="Password", bg='#333333', fg='#ffffff', font=('Arial',15))
        n_password=tk.Entry(frame, show="*", font=('Arial',15))
        c_pa=tk.Label(frame, text="Confirm Password", bg='#333333', fg='#ffffff', font=('Arial',15))
        c_password=tk.Entry(frame, show="*", font=('Arial',15))
        

        def register():
            username_check=cursor.execute(f"""SELECT username FROM cred WHERE username="{username1.get()}";""")
            email_check=cursor.execute(f"""SELECT email FROM cred WHERE email="{email.get()}";""")
            if username1.get()=="" or email.get()=="" or n_password.get()=="" or c_password.get()=="":
                tkinter.messagebox.showerror("Register", "Entries cannot be blank")
            elif n_password.get() != c_password.get():
                tkinter.messagebox.showerror("Register","Passwords do not match")
            elif username_check.fetchone()!=None:
                tkinter.messagebox.showerror("Register","Username already taken")
            elif email_check.fetchone() != None :
                tkinter.messagebox.showerror("Register","Email already in use")
            else:
                cursor.execute(f"""INSERT INTO cred VALUES ("{username1.get()}", "{email.get()}", "{c_password.get()}");""")
                connection.commit()
                tkinter.messagebox.showinfo("Register", "Successfully registered. Please Login")

        register_button=tk.Button(frame, text="Register", command=register, bg='#999999', font=('Arial',13))
        al_login_label=tk.Label(frame, text="Already a user?", bg='#333333', fg='#ffffff', font=('Arial',13))
        tab_login_button=tk.Button(frame, text="Login", command=back_button, bg='#999999', font=('Arial',13))

        register_label.grid(row=0,column=0,columnspan=2,pady=15)
        us1.grid(row=1, column=0)
        username1.grid(row=1, column=1)
        em1.grid(row=2, column=0)
        email.grid(row=2, column=1)
        n_pa.grid(row=3,column=0)
        n_password.grid(row=3,column=1)
        c_pa.grid(row=4,column=0)
        c_password.grid(row=4, column=1)
        register_button.grid(row=5,column=0, columnspan=2,  pady=15)
        al_login_label.grid(row=6,column=0)
        tab_login_button.grid(row=6, column=1)

        

    login_label=tk.Label(frame, text="Login", bg='#333333', fg='#ffffff', font=('Arial',25))
    us=tk.Label(frame, text="Username:", bg='#333333', fg='#ffffff', font=('Arial',15))
    username=tk.Entry(frame, font=('Arial',15))
    pa=tk.Label(frame, text="Password:", bg='#333333', fg='#ffffff', font=('Arial',15))
    password=tk.Entry(frame, show="*", font=('Arial',15))

    def login():
        login_check_password=cursor.execute(f"""SELECT password FROM cred WHERE username="{username.get()}";""")
        if login_check_password.fetchone()[0] == password.get():
            tkinter.messagebox.showinfo("Login", "Login successful!")
        else: 
            tkinter.messagebox.showerror("Login","Invalid Username or Password")
    login_button=tk.Button(frame, text="Login", command=login, bg='#999999', font=('Arial',13))
    signup_label=tk.Label(frame, text="Not a registered user?", bg='#333333', fg='#ffffff', font=('Arial',13))
    tab_register_button=tk.Button(frame, text="Register Now", command=tab_register, bg='#999999', font=('Arial',13))

    
    login_label.grid(row=0, column=0, columnspan=2,pady=15)
    us.grid(row=1,column=0)
    username.grid(row=1,column=1)
    pa.grid(row=2, column=0)
    password.grid(row=2,column=1)
    login_button.grid(row=3,column=0,columnspan=2, pady=15)
    signup_label.grid(row=4,column=0)
    tab_register_button.grid(row=4,column=1)

tab_login()
frame.pack()
win.mainloop()
connection.close