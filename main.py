from tkinter import *

window = Tk() # instantiated an instance of a window
window.geometry("500x500")
window.title("Python Project GUI Program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)

window.config(background='grey')

window.mainloop() # place window on computer screen , listen for events