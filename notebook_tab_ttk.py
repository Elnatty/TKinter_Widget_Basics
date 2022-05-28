from tkinter import *
from tkinter import ttk
# to use the ttk >> from tkinter import ttk.

root = Tk()
root.geometry('800x400')

# create notebook 1st.
notebook = ttk.Notebook(root)
notebook.pack(pady=20)

# create a frame
nath = ttk.Frame(notebook)
hann = ttk.Frame(notebook)
# very necessary.
nath.pack(fill='both', expand=1)
hann.pack(fill='both', expand=1)

# Add frames to notebook
notebook.add(nath, text='Nathan')
notebook.add(hann, text='Hannah')


# Entry box for nath
nath_entry = ttk.Entry(nath, font=("Helvetica", 24))
nath_entry.pack(pady=10)

# Convert Button
convert_button = ttk.Button(nath, text='Convert to Hexadecimal')
convert_button.pack()

root.mainloop()