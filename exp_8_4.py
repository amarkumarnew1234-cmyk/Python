'''4. Create a GUI based task manager where users can add, edit and remove tasks. Use Tkinter 
(buttons, listbox), SQLite/MySQL (task storage).'''
from tkinter import *
import sqlite3

root=Tk()
root.title("Task Manager")
root.geometry("400x400")
root.resizable(False,False)

conn=sqlite3.connect("tasks.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,task TEXT)")
conn.commit()

def load_tasks():
    listbox.delete(0,END)
    cur.execute("SELECT * FROM tasks")
    rows=cur.fetchall()
    for row in rows:
        listbox.insert(END,row[1])

def add_task():
    task=entry.get()
    if task!="":
        cur.execute("INSERT INTO tasks(task) VALUES(?)",(task,))
        conn.commit()
        entry.delete(0,END)
        load_tasks()

def delete_task():
    try:
        selected=listbox.curselection()[0]
        task=listbox.get(selected)
        cur.execute("DELETE FROM tasks WHERE task=?",(task,))
        conn.commit()
        load_tasks()
    except:
        pass

def edit_task():
    try:
        selected=listbox.curselection()[0]
        old_task=listbox.get(selected)
        new_task=entry.get()
        if new_task!="":
            cur.execute("UPDATE tasks SET task=? WHERE task=?",(new_task,old_task))
            conn.commit()
            entry.delete(0,END)
            load_tasks()
    except:
        pass

Label(root,text="Task Manager",font=("Arial",14)).pack(pady=10)

entry=Entry(root,width=30)
entry.pack(pady=5)

Button(root,text="Add Task",width=15,command=add_task).pack(pady=5)
Button(root,text="Edit Task",width=15,command=edit_task).pack(pady=5)
Button(root,text="Delete Task",width=15,command=delete_task).pack(pady=5)

listbox=Listbox(root,width=40,height=10)
listbox.pack(pady=10)

load_tasks()

root.mainloop()

conn.close()