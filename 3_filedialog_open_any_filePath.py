from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.configure(bd=6)
root.iconbitmap('icon_png/computer.ico')

root.filename = filedialog.askopenfilename(initialdir='icon_png', title='Select File', filetypes=(('png files', '*.png'), ('all files', '*.*')))
lab = Label(root, text=root.filename).pack()
def show():
    global image
    image = ImageTk.PhotoImage(Image.open(root.filename).resize((300,500)))
    Label(image=image).pack()

b1 = Button(root, text='Click Here', command=show).pack()


root.mainloop()