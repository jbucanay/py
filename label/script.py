from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root)
img = PhotoImage(file="widget.pgm")
small = img.subsample(2, 2)  # low number equals bigger image
label.config(image=small)
label.config(text="Hi There")
label.config(font=('lato', 25, 'bold'))
label.config(compound=RIGHT)
label.pack()
root.mainloop()
