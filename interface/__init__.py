from functools import partial
from tkinter import *

def initializeFrame(parent):
    frame = Frame(parent, borderwidth = 1, relief = "raised")
    frame.place(x = 5, y = 5, width = 315, height = 390)

    return frame

def deleteFrameAndGo(frame, destiny):
    frame.destroy()
    destiny()

def configureCommands(frame, elements, destinations):
    position = 0
    for element in elements:
        element["command"] = partial(deleteFrameAndGo, frame, destinations[position])
        position += 1

def drawMenu(frame, title, elements, back_button = False):
    line = 4
    w_label = 38

    spacing_1 = Label(frame, width = w_label, height = 1)
    spacing_2 = Label(frame, width = w_label, height = 2)

    spacing_1.grid(row = 1, column = 1, columnspan = 3)
    title.grid(row = 2, column = 1, columnspan = 3)
    spacing_2.grid(row = 3, column = 1, columnspan = 3)
    
    
    for element in elements:
        spacing_on_top_of_the_button = Label(frame, width = w_label, height = 1)
        spacing_on_top_of_the_button.grid(row = line, column = 1, columnspan = 3)
        
        line += 1 
        
        element["width"] = 10
        element["height"] = 2
        element.grid(row = line, column = 2)
        
        line += 1 
    
    if back_button:
        spacing_3 = Label(frame, width = w_label, height = 2)
        spacing_3.grid(row = line, column = 1, columnspan = 3)
        back_button["width"] = 8
        back_button.grid(row = line+1, column = 2)

def drawForm(frame, title, elements, texts, confirm_button, back_button):
    line = 4
    w_label = 38
    position = 0

    spacing_1 = Label(frame, width = w_label, height = 1)
    spacing_2 = Label(frame, width = w_label, height = 1)

    spacing_1.grid(row = 1, column = 1, columnspan = 3)
    title.grid(row = 2, column = 1, columnspan = 3)
    spacing_2.grid(row = 3, column = 1, columnspan = 3)
    
    for element in elements:
        spacing_on_top_of_the_button = Label(frame, width = w_label, height = 1)
        spacing_on_top_of_the_button.grid(row = line, column = 1, columnspan = 3)
        
        line += 1 
        
        label_info = Label(frame, text = texts[position])
        label_info.grid(row = line, column = 1, sticky = E)

        
        element.grid(row = line, column = 2, sticky = W)
        
        line += 1
        position += 1

    spacing_3 = Label(frame, width = w_label, height = 3)
    spacing_3.grid(row = line, column = 1, columnspan = 3)

    back_button["width"] = 7
    back_button.grid(row = line+1, column = 1, sticky = E)

    confirm_button.grid(row = line+1, column = 2, columnspan = 2)

def drawListMembers(frame, title):
    pass