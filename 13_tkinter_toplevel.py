from tkinter import *

# create a function for 2nd TopLevel, window which is not associated with any parent window
def open_toplevel2():
    # create a widget
    top2 = Toplevel()
    top2.title('Toplevel2')
    top2.geometry('200x200')
    # create a label
    label = Label(top2, text='This is Toplevel2 Window')
    label.pack()
    # create exit button
    button = Button(top2, text='Exit', command=top2.destroy)
    button.pack()
    # create a button back to root window
    button3 = Button(top2, text='back to root window', command=root)
    button3.pack()

# define a function for 1st TopLevel which is associated with root window, ie (moving to toplevel1 from root)
def open_toplevel1():
    # create a widget
    top1 = Toplevel()
    top1.title('Toplevel2')
    top1.geometry('200x200')
    # create a label
    label = Label(top1, text='This is Toplevel1 WIndow')
    label.pack()
    # exit button
    button = Button(top1, text='Exit', command=top1.destroy)
    button.pack()
    # create a button to TopLevel2
    button2 = Button(top1, text='open toplevel2', command=open_toplevel2)
    button2.pack()

def root():
    root = Tk()
    root.title('Main Page')
    root.geometry('200x300')

    l1 = Label(root, text='This is Root Page')
    l1.pack()

    b = Button(root, text='open toplevel1', command=open_toplevel1)
    b.pack()
    b.place(x=50,y=60)

    root.mainloop()

root()