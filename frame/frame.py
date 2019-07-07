from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root)
# flat, solid, raised, groove, ridge, sunken
frame.config(height=500, width=500)
frame.config(relief=RAISED)
ttk.Button(frame, text='click').grid()
frame.config(padding=(30, 30))

frame.pack()

root.mainloop()
