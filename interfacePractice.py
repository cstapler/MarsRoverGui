#GUI for use with Cerebot II using ATmega128


from Tkinter import *
import Tkinter
import tkMessageBox
import serial
import io

top = Tkinter.Tk()
#ser = serial.Serial() #Serial instance
#ser.baudrate = 57600 #Specifies baudrate
#ser.stopbits = STOPBITS_TWO #Specifies number of stopbits(Has associated constants)
#ser.timeout = 20 #Specifies timeout in number of seconds(for read)
#ser.port = 'COM8' #Specifies which port to connect (On Windows 'COM#' format should work)

#ser.open() #opens port communication
#ser.is_open

def moveBot():
    #ser.write("1")
    tkMessageBox.showinfo("Dream Machine", "Move")
    
def scanWithBot():
    #ser.write("2")
    tkMessageBox. showinfo("Dream Machine","Scan")
    
def rotateBot(angle):
    #ser.write("3 %d" % (angle))
    tkMessageBox.showinfo("Dream Machine", "Rotate")
    
#Button Linked to Moving Bot Forward
B1 = Tkinter.Button(top, text = "Move Robot Forward", command = moveBot)
B1.grid(row = 0, column = 0)
#Button linked to Scanning with Bot
B2 = Tkinter.Button(top, text = "Scan with Robot", command = scanWithBot)
B2.grid(row = 3, column = 0)
#Label for angle used in rotate function                   
angleL = Label(top, text="Enter Angle")
angleL.grid(row = 6, column = 0)
#Entry field for angle used rotate Function 
angleE = Entry(top,bd = 5)
angleE.grid(row = 6, column = 1)
#Button linked to rotating bot a certain amount specified in angle Entry
B3 = Tkinter.Button(top, text = "Rotate Robot", command = rotateBot(angleE.get()))
B3.grid(row = 9, column = 0)



top.mainloop()

ser.close() #closes port
ser.is_open
