import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x300")

def on_click():
    messagebox.showinfo("tk", "welcome to Aurora College!")

b1 = tk.Button(root, text="Click Me", command=on_click)
b1.pack()

root.mainloop()