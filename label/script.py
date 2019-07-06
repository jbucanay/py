from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root)
img = PhotoImage(file="widget.pgm")

label.config(image=img,)
label.config(text="Hi There")
label.config(font=('lato', 25, 'bold'))
label.config(compound='center')
label.pack()
root.mainloop()
