import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os, os.path
from sqlalchemy import null

#resize images and button
imgButtonWidth = 100
imgButtonHeight = 100
imgButtonSize = (imgButtonWidth,imgButtonHeight)
#Set the height and width of the game by number of items. 
width = 6
height = 6
buttonList = []
#Will be a 2d array of [button, id]
answersList = []
clickedCount = 0
imgs = []
hiddenImg = null

#Helper function to configure background in Tkinter
def fromRGB(rgb): 
    return "#%02x%02x%02x" % rgb   

# Create frame, set default size of frame and background color.
root = Tk()
root.title('Memory Game')
root.geometry(str(imgButtonWidth * (width+1)) + "x" + str(imgButtonHeight * (height+1)))
root.config(bg=fromRGB((100,100,100)))

frame = Frame(root, bg='darkblue')
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

#Shuffle images for the game
imgs = getImages()
random.shuffle(imgs)

#Simple image to cover the tiles
hiddenImg = ImageTk.PhotoImage(Image.new('RGB', (imgButtonWidth, imgButtonHeight), (50,50,105)))

#Disable buttons after a match
def disable():
    global clickedCount, answersList

    clickedCount = 0
    for a in answersList:
        a[0].config(state=DISABLED, bg="green")    

    answersList = []

#Hide buttons again
def hide():
    global clickedCount, answersList  
              
    for answers in answersList:               
        answers[0].config(image=hiddenImg, state=NORMAL, bg="white")#, bg="white")    
 
def show():
    global answersList

    for answer in answersList:
        answer[0].config(image=answer[2], state=DISABLED) 
        #Update the button before being hidden again
        root.update()                
       
def wrong():
    for a in answersList:
        a[0]["bg"] = "red"
    
def buttonClicked(picture, id, button):
    global clickedCount, answersList, lastbutton
    
    answersList.append([button, id, picture])    
    #if button.image is hiddenImg:# and clickedCount < 2:       
    show() 

    if len(answersList) == 2:               
        #Check id but make sure it's not the same button pressed twice
        if answersList[0][1] is answersList[1][1]:#and answersList[0][0] is not answersList[1][0]:
            disable()
        else:           
            wrong()             
            button.after(600, hide())             
            answersList = []  

#Create the actual buttons with their respective image 
for h in range(height):    #print(buttons[w][::],"\n")    
    newList = []
    for w in range(width):        
        tempImage = imgs.pop()
        picture = ImageTk.PhotoImage(tempImage[0])        
        id = tempImage[1]        
        button = Button(frame, image=hiddenImg, state=NORMAL, height=imgButtonHeight, width=imgButtonWidth) 
        #Need to split this up because of how python handles closures
        button.config(command = lambda pic_temp=picture, id_temp=id, button_temp = button: buttonClicked(pic_temp, id_temp, button_temp))         
        button.grid(row=h, column=w, padx=1, pady=1)           
        newList.append(button)
    buttonList.append(newList)

frame.pack(expand=True) 

root.mainloop()
