from tkinter import Tk, Frame, Label, Button

root = Tk()
frm = Frame(root)
frm.pack()
Label(frm, text="Hello World!", font=('Helvetica', 40)).pack()
Button(frm, text="Quit", command=root.destroy).pack()
root.mainloop()