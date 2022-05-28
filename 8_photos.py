from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap('icon_for_tkinter/computer.ico')
# open('icon_for_tkinter/computer.ico')

img = Image.open('icon_for_tkinter/n2.png').resize((400, 500))
img_tk = ImageTk.PhotoImage(img)
Button(root, image=img_tk).pack()


root.mainloop()