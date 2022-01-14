import random
import time
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import glob
import os, os.path

# Fetch images from location and create a list of Image objects, then return.
def getImages():
    imgs = []
    path = "/home/paul/Programming/Python/MyMiniProjects/Mid/MemoryGame/"
    valid_images = [".jpg",".gif",".png",".tga"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(Image.open(os.path.join(path,f)))
    return imgs + imgs

#Set the height and width of the game by number of items. 
width = 6
height = 6
buttons = [[None]*width]*height

# Create frame, set default size of frame and background color.
ws = Tk()
ws.title('PythonGuides')
ws.geometry('1000x1000')
ws.config(bg='#0080FF')

frame = Frame(ws, bg='#0080FF')


# image_list = []
# for filename in glob.glob('/home/paul/Programming/Python/MyMiniProjects/Mid/MemoryGame/'): #assuming gif
#     im=Image.open(filename)
#     image_list.append(im)


count = 35

imgs = getImages()
random.shuffle(imgs)

def buttonClicked(w, h):
    print(buttons[w][h])
   #self.state=DISABLED

# def createButton(w,h,imgs):
#     buttonPairs = []
#     for i in  range(int(w*h/2)):
#         picture = imgs[i]
#         button = Button(frame, image=picture, state=NORMAL, command= lambda: buttonClicked( w, h))
#         button.image = picture
#         buttonPairs.append(button)
#         buttonPairs.append(button)
#     return buttonPairs

# print(createButton(width, height, imgs))

buttonList = []

for w in range(width):
    for h in range(height):
        picture = ImageTk.PhotoImage(imgs.pop(count))
        buttons[w][h] = Button(frame, image=picture, state=NORMAL, command= lambda width_placeholder=w, height_placeholder=h: buttonClicked(width_placeholder, height_placeholder))
        buttons[w][h].image = picture
        buttons[w][h].name = str(w + h)
        #buttons[w][h].grid(row=w, column=h, ipadx=random.randint(0,40), ipady=random.randint(0,40), padx=random.randint(0,5), pady=random.randint(0,5))
        buttons[w][h].grid(row=w, column=h, padx=5, pady=5)

        #Button(frame, image=picture).grid(row=w, column=h, ipadx=random.randint(0,40), ipady=random.randint(0,40), padx=random.randint(0,5), pady=random.randint(0,5))
        count -= 1
        buttonList.append(buttons[w][h])
      
for x in buttonList:
    #x.grid()
    pass

# Button(frame, text="7").grid(row=0, column=0, sticky='ew')
# Button(frame, text="8").grid(row=0, column=1)
# Button(frame, text="9").grid(row=0, column=2)

# Button(frame, text="4 ").grid(row=1, column=0)
# Button(frame, text="5").grid(row=1, column=1, ipadx=10, ipady=10, padx=10, pady=10)
# Button(frame, text="6").grid(row=1, column=2)

# Button(frame, text="7 ").grid(row=2, column=0)
# Button(frame, text="8").grid(row=2, column=1)
# Button(frame, text="9").grid(row=2, column=2)

frame.pack(expand=True) 

ws.mainloop()

# root = Tk()
# root.title('Matchmaker')
# root.resizable(width=False, height=False)

# # my_w = tk.Tk()
# # my_w.geometry("200x200")  # Size of the window 
# # my_w.title("www.plus2net.com")  # Adding a title
# # my_w.mainloop()


# # width = 5
# # height = 5

# # root.grid(width, height, "Hey")

# class App(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
#         self.canvas.pack(side="top", fill="both", expand="true")
#         self.rows = 100
#         self.columns = 100
#         self.cellwidth = 25
#         self.cellheight = 25

#         self.rect = {}
#         self.oval = {}
#         for column in range(20):
#             for row in range(20):
#                 x1 = column*self.cellwidth
#                 y1 = row * self.cellheight
#                 x2 = x1 + self.cellwidth
#                 y2 = y1 + self.cellheight
#                 self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="blue", tags="rect")
#                 self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="blue", tags="oval")

#         self.redraw(1000)

#     def redraw(self, delay):
#         self.canvas.itemconfig("rect", fill="blue")
#         self.canvas.itemconfig("oval", fill="blue")
#         for i in range(10):
#             row = random.randint(0,19)
#             col = random.randint(0,19)
#             item_id = self.oval[row,col]
#             self.canvas.itemconfig(item_id, fill="green")
#         self.after(delay, lambda: self.redraw(delay))

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

