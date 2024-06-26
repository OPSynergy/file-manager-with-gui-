import tkinter as tk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import os

root = tk.Tk()
root.title("File Management System By OP")
root.geometry("800x510+0+0")

lbltitle = tk.Label(root, bd=20, relief="ridge", text="FILE MANAGEMENT SYSTEM", fg="cyan", bg="black", font=("Times new roman", 30, 'bold'))
lbltitle.pack(side="top", fill="x")

bf = tk.Frame(root, bd=20, relief="ridge", bg="light blue")
bf.place(x=0, y=80, width=800, height=500)

button_width = 20
button_height = 1
button_padx = 2
button_pady = 10

create_btn = tk.Button(bf, text="Create File", bg="black", fg="cyan", font=('Helvetica', 14, "bold"), width=button_width, height=button_height, padx=button_padx, pady=6, command=lambda: create_f())
create_btn.grid(row=0, column=0, pady=button_pady, sticky='ew')

view_btn = tk.Button(bf, text="View All Files", bg="black", fg="cyan", font=('Helvetica', 14, "bold"), width=button_width, height=button_height, padx=button_padx, pady=6, command=lambda: view_af())
view_btn.grid(row=1, column=0, pady=button_pady, sticky='ew')

delete_btn = tk.Button(bf, text="Delete File", bg="black", fg="cyan", font=('Helvetica', 14, "bold"), width=button_width, height=button_height, padx=button_padx, pady=6, command=lambda: delete_f())
delete_btn.grid(row=2, column=0, pady=button_pady, sticky='ew')

read_btn = tk.Button(bf, text="Read File", bg="black", fg="cyan", font=('Helvetica', 14, "bold"), width=button_width, height=button_height, padx=button_padx, pady=6, command=lambda: read_f())
read_btn.grid(row=3, column=0, pady=button_pady, sticky='ew')

edit_btn = tk.Button(bf, text="Edit File", bg="black", fg="cyan", font=('Helvetica', 14, "bold"), width=button_width, height=button_height, padx=button_padx, pady=6, command=lambda: edit_f())
edit_btn.grid(row=4, column=0, pady=button_pady, sticky='ew')

exit_btn = tk.Button(bf, text="Exit System", bg="black", fg="cyan", font=('Helvetica', 14, "bold"), width=button_width, height=button_height, padx=button_padx, pady=6, command=lambda: exit_app())
exit_btn.grid(row=5, column=0, pady=button_pady, sticky='ew')

bf.grid_columnconfigure(0, weight=1)

def create_f():
    try:
        fn = sd.askstring("Create File", "Enter the File Name : ")
        if fn:
            with open(fn, "x") as f:
                mb.showinfo("Success", "File Created Successfully!")
        else:
            mb.showerror("Error", "File name cannot be empty.")
    except Exception as e:
        mb.showerror("Error occurred", str(e))

def view_af():
    try:
        af = os.listdir()
        if not af:
            mb.showinfo("No Files", "No files found!")
        else:
            mb.showinfo("All Files", "\n".join(af))
    except Exception as e:
        mb.showerror("Error occurred", str(e))

def delete_f():
    try:
        fn = sd.askstring("Delete File", "Enter the File Name to delete : ")
        if fn:
            os.remove(fn)
            mb.showinfo("Success", "File Deleted Successfully!")
        else:
            mb.showerror("Error", "File name cannot be empty.")
    except Exception as e:
        mb.showerror("Error occurred", str(e))

def read_f():
    try:
        fn = sd.askstring("Read File", "Enter the File Name : ")
        if fn:
            with open(fn, "r") as f:
                data = f.read()
                if data:
                    mb.showinfo("Data", data)
                else:
                    mb.showinfo("Data", "No Content to Show!")
        else:
            mb.showerror("Error", "File name cannot be empty.")
    except Exception as e:
        mb.showerror("Error occurred", str(e))

def edit_f():
    try:
        fn = sd.askstring("Edit File", "Enter the File Name : ")
        if fn:
            add = sd.askstring("Edit File", "Enter the contents to add : ")
            if add is not None:
                with open(fn, "a") as f:
                    f.write(add)
                    mb.showinfo("Success", "File Edited Successfully!")
            else:
                mb.showerror("Error", "No content provided.")
        else:
            mb.showerror("Error", "File name cannot be empty.")
    except Exception as e:
        mb.showerror("Error occurred", str(e))

def exit_app():
    root.quit()

root.mainloop()