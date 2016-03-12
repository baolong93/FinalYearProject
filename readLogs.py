import os
import time
# top = Tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()
from graphics import *
from Tkinter import *

# Getting the distant from the transmitter and emitter base on the time the signal takes to reach the dest.
def getDistance (sendTime, receiveTime) :
	sendingTime = (int(receiveTime) - int(sendTime)) #nanosecond
	speedOfLight = 300000000; #m/s 299792458
	distance = sendingTime * speedOfLight / 100000000;
	return distance

# Working out which emitter sending the signal.
def identifyEmitterAndDistance (signalMessage, receiveTime):
	emitterCode = signalMessage[0]
	sendTime = signalMessage[1:]
	distance = getDistance(sendTime, receiveTime)
	return (emitterCode, distance)

# Create circle using provided centre point coordinate and diameter.
def drawCircleWithCentrePoint (x, y, r, canvas, outlineColor, tags):
	return canvas.create_oval(x - r, y - r, x + r, y + r, outline = outlineColor, tags = tags)

# Write Log file 
def writeLogFile (url, fileName):
	os.system("cd " + url)# url = "/Users/baolongngo/Documents/UoP/FinalYear/Project"
	f = open(fileName,"w")# filename = "logs.txt"
	currentTime = int(time.time() * 1000000000)#nano second
	f.write(str(currentTime) + " " + str(currentTime + 6)) 

# Read Log file
def readLogFile(url, fileName, canvas):
	os.system("cd " + url)# url = "/Users/baolongngo/Documents/UoP/FinalYear/Project"
	f = open(fileName,"r")# filename = "logs.txt"
	readf = f.readlines()
	for line in readf:
		distance = 0
		times = line.split()
		emitterCodeNdistance = identifyEmitterAndDistance(times[0], times[1])
		print emitterCodeNdistance[1]
		if emitterCodeNdistance[0] == "1":
			canvas.delete(canvas.find_withtag("one")[0])
			drawCircleWithCentrePoint(400, 200, emitterCodeNdistance[1], canvas, "red", "one")
		elif emitterCodeNdistance[0] == "2":
			canvas.delete(canvas.find_withtag("two")[0])
			drawCircleWithCentrePoint(200, 400, emitterCodeNdistance[1], canvas, "green", "two")
		else:
			canvas.delete(canvas.find_withtag("three")[0])
			drawCircleWithCentrePoint(200, 200, emitterCodeNdistance[1], canvas, "blue", "three")
	#close file
	if f.closed == "False":
	    f.close()

#main
def main():
	master = Tk()
	w = Canvas(master, width=600, height=600)
	w.pack()

	w.create_rectangle(200, 200, 400, 400, outline="black")
	emitter1 = drawCircleWithCentrePoint(400, 200, 170, w, "red", "one")
	emitter2 = drawCircleWithCentrePoint(200, 400, 132, w, "green", "two")
	emitter3 = drawCircleWithCentrePoint(200, 200, 150, w, "blue", "three")

	readLogFile("/Users/baolongngo/Documents/UoP/FinalYear/Project", "logs.txt", w)


	mainloop()

main()


