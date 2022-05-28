from tkinter import messagebox
from tkinter import *

def click():
    messagebox.showinfo(title='INFO', message='Click me')
def lab():
    Label(window, text='Oya lets go..', font=('monospace', 10)).pack()

window = Tk()
window.geometry('200x200')

button = Button(window, text='ENTER', command=lambda: click())
button.pack()



window.mainloop()