from tkinter import *
from tkinter import ttk

root = Tk()


def clicked():
    print('Click me nice!')


button = ttk.Button(root)
button.config(command=clicked, text='i will print shit')
button.grid(row=5, column=5, columnspan=3)
button.state(['disabled'])
root.mainloop()
