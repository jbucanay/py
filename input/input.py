from tkinter import *
from tkinter import ttk

root = Tk()
entry = ttk.Entry(root, width=40)
entry.pack()
entry.insert(0, input())
entry.config(show="#*.")
entry.state(['disabled'])
root.mainloop()
