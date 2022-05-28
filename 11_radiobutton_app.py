from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap('icon_png/computer.ico')
root.title('Frame')
root.geometry('300x200')

frame = LabelFrame(root, text='Radio Button', padx=10, pady=20)
frame.pack(padx=15, pady=10)

# this fumction takes an arg ie, value, which is necessary to define and get the clicked value of a particular radio button.
def click(value):
    # make l1 a global variable in order for the function to see it.
    global l1
    # to replace the default value with whatever is clicked or (you can use the .grid_forget or .pack_forget also.)
    l1.forget()
    l1 = Label(root, padx=90, bg='red', fg='white', text=value)
    l1.pack(ipadx=45, pady=20)

# Note.. when you use a list you use a for loop to iterate through your radio option, then you have to set a default value or option
# ie, example >> pizza.set('') this selects a default value since you are iterating through a list.
# but when you dont use a list you dont have to set a default value, though you can but its by choice.

# variable here is either StingVar() or IntVar()
# value here means the value of the button clicked, could be integer or string.

MODES = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion')
]
pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:
    # we use lambda when we have a function that takes on an argument. ie click(value) where value is pizza.get()
    Radiobutton(root, text=text, variable=pizza, value=mode, command=lambda: click(pizza.get())).pack(anchor=W)

# r = IntVar()
# radio = Radiobutton(frame, text='Boy', variable=r, value=1, command=lambda: click(r.get()))
# radio2 = Radiobutton(frame, text='Girl', variable=r, value=2, command=lambda: click(r.get()))
# radio3 = Radiobutton(frame, text='Man', variable=r, value=3, command=lambda: click(r.get()))
l1 = Label(root, padx=78, bg='red', fg='white', text=pizza.get())
l1.pack(ipadx=45, pady=20)
# radio.pack()
# radio2.pack()
# radio3.pack()



root.mainloop()