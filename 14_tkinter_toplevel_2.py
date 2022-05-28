from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('New Window')
root.configure(bd=6)
root.iconbitmap('icon_png/computer.ico')

img_open = Image.open('../icon_png/a2.png').resize((300, 500))
imgg = ImageTk.PhotoImage(img_open)

def open():
    global img
    top = Toplevel()
    Label(top, text=f'You are in 2nd Window').pack()
    img_open = Image.open('../icon_png/a1.png').resize((300, 500))
    img = ImageTk.PhotoImage(img_open)
    Label(top, image=img).pack()

    MODES = [('a', 'a'), ('Forward', 'Forward'), ('Quit Window', 'Quit Window')]
    r = StringVar()
    r.set('a')
    for text, mode in MODES:
        Radiobutton(top, text=text, variable=r, value=mode, command=lambda: r.get()).pack()

    # def cli(value):
    #     lab = Label(top, text=value)
    #     lab.pack()
    Button(top, text='Quit', command=top.destroy).pack()



b1 = Button(root, text='Next Window', image=imgg, width=300, command=open)
b1.pack()


root.mainloop()