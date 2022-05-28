from tkinter import *

window = Tk()
window.geometry('50x50')

# spinbox
spin = Spinbox(window, from_=10, to=50, width=5).pack()

# checkbox
# you need variable, onvalue and offvalue.
r = StringVar()
chk = Checkbutton(window, text='lets go...', variable=r)
# since the checkbox is checked by default, we use the .deselect method to uncheck.
chk.deselect()
chk.pack()



window.mainloop()