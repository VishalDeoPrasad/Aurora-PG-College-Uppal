import tkinter as tk    

root = tk.Tk()
root.geometry("300x300")

l1 = tk.Label(root, text="Username")
l1.grid(row=0, column=0, padx=15, pady=15)

e1 = tk.Entry(root)
e1.grid(row=0, column=1, padx=15, pady=15)

l2 = tk.Label(root, text="Password")
l2.grid(row=1, column=0, padx=15, pady=15)

e1 = tk.Entry(root)
e1.grid(row=1, column=1, padx=15, pady=15)

b1 = tk.Button(root, text="Login")
b1.grid(row=2, column=0, padx=15, pady=15)

root.mainloop()