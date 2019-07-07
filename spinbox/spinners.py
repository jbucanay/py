from tkinter import *
from tkinter import ttk

root = Tk()
# vals = range(0, 11)
# month = StringVar()
# combo = ttk.Combobox(root, textvariable=month)
# combo.pack()
# y = []
# for x in vals:
#     y.append(x)
# combo.config(values=y)
# combo.get()
# print(combo)
# root.mainloop()
year = StringVar()
Spinbox(root, from_=1990, to=2019, textvariable=year).pack()
root.mainloop()
