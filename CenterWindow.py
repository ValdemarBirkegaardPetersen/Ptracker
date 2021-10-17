import tkinter
from tkinter import *
from tkinter import ttk

#Creating the menubar and the different cascades and commands
def menubar(myWindow):
    menu = Menu(myWindow)
    myWindow.config(menu=menu)

    #Adding a cascade "file" and inserting commands into it.
    file = Menu(menu)
    file.add_command(label="Exit", command=myWindow.quit) #Not working - Does not exit the window when clicked
    menu.add_cascade(label="File", menu=file)

    #Adding a cascade "edit" and inserting commands into it.
    edit = Menu(menu)
    edit.add_command(label="Undo")
    menu.add_cascade(label="Edit", menu=edit)
