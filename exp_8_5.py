#5. Design a login and signup authentication system.
from tkinter import *
import sqlite3

root=Tk()
root.title("Login & Signup System")
root.geometry("350x300")
root.resizable(False,False)

conn=sqlite3.connect("users.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)")
conn.commit()

def signup():
    username=user_entry.get()
    password=pass_entry.get()
    
    if username!="" and password!="":
        cur.execute("SELECT * FROM users WHERE username=?",(username,))
        if cur.fetchone():
            status.config(text="User already exists")
        else:
            cur.execute("INSERT INTO users VALUES(?,?)",(username,password))
            conn.commit()
            status.config(text="Signup Successful")
            clear()
    else:
        status.config(text="Fill all fields")

def login():
    username=user_entry.get()
    password=pass_entry.get()
    
    cur.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    if cur.fetchone():
        status.config(text="Login Successful")
    else:
        status.config(text="Invalid Credentials")

def clear():
    user_entry.delete(0,END)
    pass_entry.delete(0,END)

Label(root,text="Authentication System",font=("Arial",14)).pack(pady=10)

Label(root,text="Username").pack()
user_entry=Entry(root,width=25)
user_entry.pack()

Label(root,text="Password").pack()
pass_entry=Entry(root,width=25,show="*")
pass_entry.pack()

Button(root,text="Signup",width=12,command=signup).pack(pady=5)
Button(root,text="Login",width=12,command=login).pack(pady=5)

status=Label(root,text="")
status.pack(pady=10)

root.mainloop()

conn.close()