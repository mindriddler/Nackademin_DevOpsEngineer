from tkinter import Tk
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root)


ttk.Style().configure('.', font=('Helvetica', 40))
ttk.Style().configure('TButton', font=('Helvetica', 20))
frm.pack()

ttk.Label(frm, text="Hello World!").pack()
ttk.Button(frm, text="Quit", command=root.destroy).pack()

root.mainloop()