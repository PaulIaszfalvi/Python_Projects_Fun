import random
import time
import tkinter as tk
from tkinter import *
from typing_extensions import Self
from PIL import Image, ImageTk
import glob
import os, os.path
import numpy as np


#resize images and button
imgButtonWidth = 100
imgButtonHeight = 100
imgButtonSize = (imgButtonWidth,imgButtonHeight)
#Set the height and width of the game by number of items. 
width = 6
height = 6
#buttons = [[Button]*width]*height
#Total number of items 36 (0-35)
count = width*height-1
buttonList = []
answersList = []
clickedCount = 0

# Fetch images from location and create a list of Image objects, then return.
def getImages():
    imgs = []
    path = "/home/paul/Programming/Python/MyMiniProjects/Mid/MemoryGame/"
    valid_images = [".jpg",".gif",".png",".tga"]
    
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append([Image.open(os.path.join(path,f)).resize(imgButtonSize), f])
    return imgs + imgs

# Create frame, set default size of frame and background color.
ws = Tk()
ws.title('Memory Game')
ws.geometry(str(imgButtonWidth * (width+1)) + "x" + str(imgButtonHeight * (height+1)))
ws.config(bg='darkblue')

frame = Frame(ws, bg='darkblue')

#Shuffle images for the game
imgs = getImages()
random.shuffle(imgs)

#Simple image to cover the tiles
hiddenImg = ImageTk.PhotoImage(Image.new('RGB', (imgButtonWidth, imgButtonHeight), (0,0,105)))

def buttonClicked(picture, id, button):
    global clickedCount, answersList

    if button.image == hiddenImg and clickedCount < 2:  
        button["image"] = picture           
        clickedCount += 1     
        answersList.append([button, id])        
    elif len(answersList) == 2:        
        #Check id but make sure it's not the same button pressed twice
        if answersList[0][1] == answersList[1][1] and answersList[0][0] != answersList[1][0]:
            clickedCount = 0
            for a in answersList:
                a[0]["state"] = "disabled"
            answersList = []
        else:             
            clickedCount = 0                      
            for a in answersList:
                a[0]["image"] = hiddenImg
            answersList = []
   

#Create the actual buttons with their respective image 
for h in range(height):    #print(buttons[w][::],"\n")    
    newList = []
    for w in range(width):        
        tempImage = imgs.pop(count)
        picture = ImageTk.PhotoImage(tempImage[0])
        id = tempImage[1]        
        button = Button(frame, image=hiddenImg,  state=NORMAL, height=imgButtonHeight, width=imgButtonWidth) 
        #Need to split this up because of how python handles closures
        button["command"] = lambda pic_temp=picture, id_temp=id, button_temp = button: buttonClicked(pic_temp, id_temp, button_temp)
        button.image = hiddenImg      
        
        #buttons[w][h].name = str(w + h)
        #buttons[w][h].grid(row=w, column=h, ipadx=random.randint(0,40), ipady=random.randint(0,40), padx=random.randint(0,5), pady=random.randint(0,5))
        button.grid(row=h, column=w, padx=1, pady=1)
        
        #Button(frame, image=picture).grid(row=w, column=h, ipadx=random.randint(0,40), ipady=random.randint(0,40), padx=random.randint(0,5), pady=random.randint(0,5))
        count -= 1
       # buttonList.append(buttons[h][w])
        newList.append(button)
    buttonList.append(newList)

# for y in range(height):
#     for x in range(width):
#         print(ButtonList[y][x])
#     print("")


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


# image_list = []
# for filename in glob.glob('/home/paul/Programming/Python/MyMiniProjects/Mid/MemoryGame/'): #assuming gif
#     im=Image.open(filename)
#     image_list.append(im)