from tkinter import messagebox
from tkinter import *

window = Tk()
window.geometry('80x80')

# playing around messagebox args, and their responses
def click():
    response = messagebox.askquestion(title='INFO', message='Click me')
    if response == 'yes':
        # setting l1 as global variable so that the click() function can see it.
        global l1
        # to prevent duplicate entries
        l1.pack_forget()
        l1 = Label(window, text='You selected 1')
        l1.pack()
    else:
        l1.pack_forget()
        l1 = Label(window, text='You selected 2')
        l1.pack()
    # to disable button after a particular criteria is met.
    #button.configure(state=DISABLED)

button = Button(window, text='ENTER', command=lambda: click())
button.pack()
l1 = Label(window)
l1.pack()


window.mainloop()