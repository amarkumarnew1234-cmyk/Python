#2. Design a GUI based basic calculator for performing basic arithmetic operations. 
from tkinter import *

root=Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.resizable(False,False)

def click(val):
    e=entry.get()
    entry.delete(0,END)
    entry.insert(0,e+str(val))

def clear():
    entry.delete(0,END)

def equal():
    try:
        result=eval(entry.get())
        entry.delete(0,END)
        entry.insert(0,result)
    except:
        entry.delete(0,END)
        entry.insert(0,"Error")

entry=Entry(root,font=("Arial",18),bd=5,relief=RIDGE,justify="right")
entry.pack(fill=BOTH,ipady=10,padx=10,pady=10)

frame=Frame(root)
frame.pack()

buttons=[
['7','8','9','/'],
['4','5','6','*'],
['1','2','3','-'],
['0','C','=','+']
]

for r in range(4):
    for c in range(4):
        b=buttons[r][c]
        if b=="C":
            btn=Button(frame,text=b,width=5,height=2,font=("Arial",14),command=clear)
        elif b=="=":
            btn=Button(frame,text=b,width=5,height=2,font=("Arial",14),command=equal)
        else:
            btn=Button(frame,text=b,width=5,height=2,font=("Arial",14),command=lambda x=b:click(x))
        btn.grid(row=r,column=c,padx=5,pady=5)

root.mainloop()