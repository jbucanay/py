from tkinter import *
from tkinter import ttk

root = Tk()
# prog = ttk.Progressbar(root, orient=HORIZONTAL)
# prog.config(mode='determinate', maximum=100.0, value=0.0)
# for x in range(0, 1000):
#     y = x - .000000000000001
#     prog.config(value=y)
# prog.pack()
# root.mainloop()
val = 5.5
prog = ttk.Progressbar(root, orient=HORIZONTAL)
prog.config(mode='determinate', maximum=100.0, variable=val)
scale = ttk.Scale(root, orient=HORIZONTAL, length=200,
                  variable=val, from_=0.0, to=100.0)
prog.pack()
scale.pack()
root.mainloop()
