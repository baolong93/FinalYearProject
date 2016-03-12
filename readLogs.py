import os
import Tkinter
# top = Tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()
from graphics import *
from Tkinter import *

# Getting the distant from the transmitter and emitter base on the time the signal takes to reach the dest.
def getDistance (sendTime, receiveTime) :
	sendingTime = (int(receiveTime) - int(sendTime)) #nanosecond
	speedOfLight = 299792458; #m/s
	distance = sendingTime * speedOfLight / 1000000000;
	return distance

# Working out which emitter sending the signal.
def identifyEmitterAndDistance (signalMessage, receiveTime):
	emitterCode = signalMessage[0]
	sendTime = signalMessage[1:]
	distance = getDistance(sendTime, receiveTime)
	return (emitterCode, distance)

# Create circle using provided centre point coordinate and diameter.
def drawCircleWithCentrePoint (x, y, r, canvas, outlineColor):
	return canvas.create_oval(x - r, y - r, x + r, y + r, outline = outlineColor)

master = Tk()

w = Canvas(master, width=200, height=200)
w.pack()

# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

# w.create_rectangle(50, 25, 150, 75, fill="blue")
# w.create_oval(10, 50, 50, 80, outline="green")
# drawCircleWithCentrePoint(0, 0, 50, w)
drawCircleWithCentrePoint(200, 0, 150, w, "red")
drawCircleWithCentrePoint(0, 200, 132, w, "green")
drawCircleWithCentrePoint(0, 0, 150, w, "blue")

mainloop()

# os.system("cd /Users/baolongngo/Documents/UoP/FinalYear/Project")
# f = open("logs.txt","r")
# readf = f.readlines()
# for line in readf:
# 	distance = 0
# 	times = line.split()
# 	emitterCodeNdistance = identifyEmitterAndDistance(times[0], times[1])
# 	print emitterCodeNdistance[0]
# 	print emitterCodeNdistance[1]
# #close file
# if f.closed == "False":
#     f.close()

