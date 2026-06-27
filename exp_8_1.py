#1. Create a simple Tkinter window with a title and fixed size. 
from tkinter import *

root=Tk()
root.title("Simple Tkinter Window")
root.geometry("400x300")
root.resizable(False,False)

root.mainloop()