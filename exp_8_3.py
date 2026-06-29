'''3. Design a GUI for student registration for a course and store these details in a database. 
Use Tkinter for UI, SQLite/MySQL for database storage. '''
from tkinter import *
import sqlite3

root=Tk()
root.title("Student Registration")
root.geometry("400x400")
root.resizable(False,False)

conn=sqlite3.connect("students.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students(name TEXT,course TEXT,email TEXT,phone TEXT)")
conn.commit()

def submit():
    name=name_entry.get()
    course=course_entry.get()
    email=email_entry.get()
    phone=phone_entry.get()
    
    if name!="" and course!="":
        cur.execute("INSERT INTO students VALUES(?,?,?,?)",(name,course,email,phone))
        conn.commit()
        clear()
        status_label.config(text="Data Saved Successfully")
    else:
        status_label.config(text="Name & Course Required")

def clear():
    name_entry.delete(0,END)
    course_entry.delete(0,END)
    email_entry.delete(0,END)
    phone_entry.delete(0,END)

Label(root,text="Student Registration Form",font=("Arial",14)).pack(pady=10)

Label(root,text="Name").pack()
name_entry=Entry(root,width=30)
name_entry.pack()

Label(root,text="Course").pack()
course_entry=Entry(root,width=30)
course_entry.pack()

Label(root,text="Email").pack()
email_entry=Entry(root,width=30)
email_entry.pack()

Label(root,text="Phone").pack()
phone_entry=Entry(root,width=30)
phone_entry.pack()

Button(root,text="Submit",command=submit,width=15).pack(pady=10)
Button(root,text="Clear",command=clear,width=15).pack()

status_label=Label(root,text="")
status_label.pack(pady=10)

root.mainloop()

conn.close()