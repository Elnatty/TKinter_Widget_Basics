from tkinter import *
from PIL import ImageTk, Image


# Placement of widgets
# Using padx or pady in (.pack or .grid) moves the widget to your desired location on the screen.
# Using padx or pady in (the main widget) increases the size of the particular widget.
# Using ipadx or ipady in (.pack or .grid) increases the size of the particular widget.
# Note.. you cant use ipadx or ipady in (the main widget).

root = Tk()
root.title('Image Test')
root.geometry('300x400')
root.iconbitmap('icon_png/computer.ico')


frame_1 = LabelFrame(root, text='Frame 1', bg='red', padx=25, pady=25)
frame_1.pack(pady=90)

b1 = Button(frame_1, text='Button', bg='white', bd=5)
b1.pack(ipady=30)



root.mainloop()