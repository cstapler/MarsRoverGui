# Tkinter based GUI for use with Cerebot II using ATmega128
from Tkinter import *
import Tkinter as tk
import tkMessageBox
import serial
import io

top = tk.Tk() # Creates the interface

seeEndB = True
#Turn off or on the see END button
def seeEndToggle():
    global seeEndB
    if seeEndB is True:
        seeEndB = False
    else:
        seeEndB = True

# Sends 1 to Move Bot forward
def moveBot():
    print "1 Should be written to bot"
    ser.write("1" + "\r")
#Sends 2 to Scan with the bot
def scanWithBot():
    print "2 written to bot"
    ser.write("2" + "\r")
#Sends 3 and Rotates the bot a specified amount(from Drop Down List)
def rotateBot():
    angle = var1.get()
    print "3 and " + angle + " written to bot"
    ser.write("3 " + angle + "\r")
#Sends 4 to Move the bot backwards
def moveBack():
    print "4 written to bot"
    ser.write("4" + "\r")
#Sends 5 to Play a song
def playSong():
    print "5 written to bot"
    ser.write("5" + "\r")
#Turns on Autonomous Mode
def autonomousMode():
    print "6 written to bot"
    ser.write("6" + "\r")
#Button Linked to Moving Bot Forward
B1 = tk.Button(top, text = "Move Robot Forward", command = moveBot)
B1.grid(row = 0, column = 0)
#Button linked to Scanning with Bot
B2 = tk.Button(top, text = "Scan with Robot", command = scanWithBot)
B2.grid(row = 1, column = 0)
#Label for angle used in rotate function
angleL = tk.Label(top, text="Enter Angle")
angleL.grid(row = 1, column = 1)
#Entry field for angle used rotate Function
angleE = tk.Entry(top,bd = 5)
angleE.grid(row = 3, column = 1)
#Button linked to rotating bot a certain amount specified in angle Entry
B3 = tk.Button(top, text = "Rotate Robot", command = rotateBot)
B3.grid(row = 0, column = 1)
#Button linked to moving bot backwards
B4 = tk.Button(top, text = "Move Backwards", command = moveBack)
B4.grid(row = 2, column = 0)
#Button linked to playing song
B5 = tk.Button(top, text = "Play Song", command = playSong)
B5.grid(row = 3, column = 0)

#Dropdown for selecting the angle to bot will rotate
var1 = tk.StringVar()
drop = tk.OptionMenu(top, var1,'-90','-60','-45','-30','30','45','60','90','180')
drop.grid(row = 2, column = 1)

#Creates button to toggle the See End Feature
seeEndButton = tk.Button(top, text = "Toggle See End", command = seeEndToggle)
seeEndButton.grid(row = 11, column = 0)

#Creates Frame used for text
textFrame = tk.Frame()
#Creates the textbox for text
textBox = tk.Text(textFrame, width=50)
textBox.pack(side=LEFT, fill=Y)
#Creates the scroll bar for the text since their is alot of text that gets added
scrollText = tk.Scrollbar(textFrame)
scrollText.pack(side=RIGHT, fill=Y)
#Attaches the TextBox and ScrollBar to each other
scrollText.config(command=textBox.yview)
textBox.config(yscrollcommand=scrollText.set)
#Places the TextFrame in the Main Frame
textFrame.grid(row = 12, column = 0)

## First Called from before mainloop and subsequently after every 200 miliseconds
## This updates the textbox with text read from serial COM port
def task_ReadFromSerial():
    global seeEndB
    readData = None
    if ser.inWaiting() != 0:
        readData = ser.readline()
        readData = readData[1:]
        textBox.insert(END,readData)
        if seeEndB == True:
            textBox.see(END)

    top.after(50, task_ReadFromSerial) #rescheduled even for 200 miliseconds

ser = serial.Serial() #Serial instance
ser.baudrate = 57600 #Specifies baudrate
ser.stopbits = 2 #Specifies number of stopbits(Has associated constants)
ser.timeout = 1 #Specifies timeout in number of seconds(for read)
ser.port = '/dev/rfcomm0' #Specifies which port to connect (On Windows 'COM#' format should work)

ser.open() #opens port communication
print ser.is_open # True if working correctly


top.after(50, task_ReadFromSerial)
top.mainloop()

ser.close() #closes port
print ser.is_open # False if not working correctly
