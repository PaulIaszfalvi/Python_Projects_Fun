import tkinter as tk
import fileWriter

master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)
tk.Label(master, text="E-mail").grid(row=2)
tk.Label(master, text="Age").grid(row=3)
tk.Label(master, text="Gender").grid(row=4)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

myList = [e1, e2, e3, e4, e5]

def callback():
    myList = [e1.get(), e2.get(), e3.get(), e4.get(), e5.get()]    
    fileWriter.writeFile(' '.join(myList))

tk.Button(master, text="Quit", command=master.destroy).grid(column=1, row=9)
tk.Button(master, text="Submit", command=callback).grid(column=0, row=9)

master.mainloop()