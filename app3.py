import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

l1 = tk.Label(root, text="Username")
l1.pack(side="left")

e1 = tk.Entry(root)
e1.pack(side="right")

l2 = tk.Label(root, text="Password")
l2.pack(side="left")

e2 = tk.Entry(root)
e2.pack(side="right")

root.mainloop()