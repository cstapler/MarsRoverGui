#!/usr/bin/python

from Tkiner import *
import Tkinter
import tkMessageBox
import serial

top = Tkinter.Tk()

def moveBot():
    tkMessageBox.showinfo("Hello Python", "This is where the serial communication stuff will go")
    
B = Tkinter.Button(top, text ="Move Robot Forward", command = moveBot)
B.pack()
top.mainloop()
