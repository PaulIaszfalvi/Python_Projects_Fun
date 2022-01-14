# import tkinter as tk

# class App:
#     def __init__(self):
#         root=tk.Tk()
#         root.title("Rock Paper Scissors")
#         root.geometry("420x200")
    
#         self.button =  tk.Button(root,text="Rock",command=self.Rock).grid(row=0,column=1,padx=10)
#         tk.Button(root,text="Paper",command=self.Paper).grid(row=0,column=2)
#         tk.Button(root,text="Scissors",command=self.Scissors).grid(row=0,column=3,padx=10)
#         root.mainloop()

#     def Rock(self):
#         text="Paper!"
#         self.text.delete(0,END) #delete everything from the Text
#         self.text.insert(0,text) #put the text in

#     def Paper(self):
#         text="Scissors!"
#         self.text.delete(0,END) #delete everything from the Text
#         self.text.insert(0,text) #put the text in

#     def Scissors(self):
#         text="Rock!"
#         self.text.delete(0,END) #delete everything from the Text
#         self.text.insert(0,text) #put the text in

# if __name__=='__main__':
#     App()
from tkinter import *

def funct(numimg):
    label.config(image=label.images[numimg])

root= Tk()
row_no = -1
buttons = []
num_of_cols = 3
root.resizable(0, 0)
numfiles = 3

for x in range(0, numfiles):
    if(x % num_of_cols == 0):
        row_no+=1

    buttons.append(Button(root, text = "Button "+str(x), bg = '#4098D3', width = 30,height = 13, command = lambda n=x: funct(n)))
    buttons[x].grid(row = row_no, column = x % num_of_cols)

label = Label(root)
label.grid(row = row_no+1, column = 0, columnspan = num_of_cols)

label.images=[]

for x in range(0, numfiles):
    label.images.append(PhotoImage(file="/home/paul/Programming/Python/MyMiniProjects/Mid/MemoryGame/image"+str(x)+".jpg"))

root.mainloop()