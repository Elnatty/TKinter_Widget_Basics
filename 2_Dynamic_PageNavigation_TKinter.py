from tkinter import *
root = Tk()

# navigation functions.
def next():
    print('Page 2')
    frame_window_1.pack_forget()
    frame_window_2.pack()

def back():
    print('Page 1')
    frame_window_2.pack_forget()
    frame_window_1.pack()

# frame_windows.
frame_window_1 = LabelFrame(root, bg='red')
frame_window_2 = LabelFrame(root, bg='blue')
frame_window_1.pack()

# buttons_frame_1
btn_frame_1 = Button(frame_window_1, text='Frame 1')
ent_frame_1 = Entry(frame_window_1, width=30)
btn_frame_1.grid(row=0, column=0)
ent_frame_1.grid(row=0, column=1)

# buttons_frame_2
btn_frame_2 = Button(frame_window_2, text='Frame 2')
ent_frame_2 = Entry(frame_window_2, width=30)
btn_frame_2.grid(row=0, column=0)
ent_frame_2.grid(row=0, column=1)

# nav_buttons
nav_btn_pg1 = Button(frame_window_1, text='Next', command=next)
nav_btn_pg2 = Button(frame_window_2, text='Back', command=back)
nav_btn_pg1.grid(row=1, column=0, columnspan=2)
nav_btn_pg2.grid(row=1, column=0, columnspan=2)


root.mainloop()