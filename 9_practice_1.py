import random
import sqlite3
from tkinter import *


root = Tk()
root.configure(bg='skyblue')

def acct_generator():
    digit = random.sample(range(10), 9)
    d_list = [str(x) for x in digit]
    a = '2' + ''.join(d_list)
    global acct
    acct = int(a)
    return acct
acct_generator()
global acct

# create sqlite table
conn = sqlite3.connect('bank.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS bankinfo (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, passw TEXT UNIQUE, acctnumber INTEGER)')
conn.commit()
conn.close()

# insert into sqlite table
def add_account(name, passw, acctnumber=acct):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO bankinfo VALUES (NULL, ?, ?, ?)', (name, passw, acctnumber))
    except sqlite3.IntegrityError:
        print('Info already exists...')
    conn.commit()
    conn.close()
# add_account('Nathan', 'natty')

def view_db():
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    add = cur.execute('SELECT * FROM bankinfo')
    global info
    info = add.fetchall()
    conn.close()
    return info
print(view_db())

# button executes the wrapper function when clicked.
def display_info():
    listb_on_frame_root.delete(0, END)
    for data in view_db():
        # print(data)
        listb_on_frame_root.insert(END, data)

# tkinter menu......................................................................................
root.title('DKing')
root.iconbitmap('computer.ico')

# frame that houses everything.
frame_root = LabelFrame(root, bg='skyblue', bd=0)
frame_root.pack()

b1_on_frame_root = Button(frame_root, text='Click Me', bg='blue', command=display_info)
b1_on_frame_root.pack(pady=10)

listb_on_frame_root = Listbox(frame_root, bg='skyblue', width=25, bd=0)
listb_on_frame_root.pack()


root.mainloop()