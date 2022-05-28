from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('200x100')

l1 = Label(root, text='Select one Option below...')
l1.grid(row=0, column=0, columnspan=2, padx=10)

rad1 = Radiobutton(root, text='Python', value=1)
rad1.grid(row=1, column=0, padx=5)
rad2 = Radiobutton(root, text='Java', value=2)
rad2.grid(row=1, column=1)



root.mainloop()