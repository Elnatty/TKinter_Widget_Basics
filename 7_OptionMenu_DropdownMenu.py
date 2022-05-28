from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('200x200')

# the 'variable' can be named to anything, its just used to denote that the dropdown options are strings.
# if options are integer we use IntVar instead of StringVar.
# other options for it are DoubleVar() >> holds float value eg: 0.0.
# then the BooleanVar() >> holds a boolean, returns 0 for False and 1 for True.

# wrapper function that executes the variable.get() value when button is clicked
def action(val):
    global lab
    lab.pack_forget()
    lab = Label(root, text=val)
    lab.pack()

# we can outline the options in a list.
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
variable = StringVar()
variable.set(days_of_the_week[0])
# use a * at the back of the list variable to make it appear as a dropdown.
option_menu = OptionMenu(root, variable, *days_of_the_week, )
option_menu.pack()

b1 = Button(root, text='Select', command=lambda: action(variable.get()))
b1.pack(pady=15)

lab = Label(root)
lab.pack()
root.mainloop()