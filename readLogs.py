import os
import time
# top = Tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()
from graphics import *
from Tkinter import *
import math

url = "/Users/baolongngo/Documents/UoP/FinalYear/Project"
logsFile = "logs.txt"
point1 = [400, 200]
point2 = [200, 400]
point3 = [200, 200]

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
def writeLogFile (url, fileName, distance1, distance2, distance3):
	os.system("cd " + url)# url = "/Users/baolongngo/Documents/UoP/FinalYear/Project"
	f = open(fileName,"r+")# filename = "logs.txt"
	currentTime = int(time.time() * 1000000000)#nano second
	f.seek(0)
	f.write("1" + str(currentTime)[-9:] + " " + str(currentTime + int(distance1/3))[-9:] + "\n") 
	f.write("2" + str(currentTime)[-9:] + " " + str(currentTime + int(distance2/3))[-9:] + "\n") 
	f.write("3" + str(currentTime)[-9:] + " " + str(currentTime + int(distance3/3))[-9:] + "\n") 
	f.truncate()
	f.close()

# Read Log file
def readLogFile(url, fileName, canvas):
	os.system("cd " + url)# url = "/Users/baolongngo/Documents/UoP/FinalYear/Project"
	f = open(fileName,"r")# filename = "logs.txt"
	readf = f.readlines()
	for line in readf:
		if len(line) > 1: 
			distance = 0
			times = line.split()
			emitterCodeNdistance = identifyEmitterAndDistance(times[0], times[1])
			print emitterCodeNdistance[1]
			if emitterCodeNdistance[0] == "1":
				canvas.delete(canvas.find_withtag("one")[0])
				drawCircleWithCentrePoint(point1[0], point1[1], emitterCodeNdistance[1], canvas, "red", "one")
			elif emitterCodeNdistance[0] == "2":
				canvas.delete(canvas.find_withtag("two")[0])
				drawCircleWithCentrePoint(point2[0], point2[1], emitterCodeNdistance[1], canvas, "green", "two")
			else:
				canvas.delete(canvas.find_withtag("three")[0])
				drawCircleWithCentrePoint(point3[0], point3[1], emitterCodeNdistance[1], canvas, "blue", "three")
	#close file
	if f.closed == "False":
	    f.close()
	canvas.after(1000, readLogFile, url, logsFile, canvas)

def distanceBetweenPoints(x1, y1, x2, y2):
	distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	return int(distance)

def callback(event):
    print "clicked at", event.x, event.y
    print "distance to point Point1", distanceBetweenPoints(point1[0], point1[1], event.x, event.y)
    print "distance to point Point2", distanceBetweenPoints(point2[0], point2[1], event.x, event.y)
    print "distance to point Point3", distanceBetweenPoints(point3[0], point3[1], event.x, event.y)
    distance1 = distanceBetweenPoints(point1[0], point1[1], event.x, event.y)
    distance2 = distanceBetweenPoints(point2[0], point2[1], event.x, event.y)
    distance3 = distanceBetweenPoints(point3[0], point3[1], event.x, event.y)
    writeLogFile(url, logsFile, distance1, distance2, distance3)

#main
def main():
	master = Tk()
	w = Canvas(master, width=600, height=600)

	w.bind("<Button-1>", callback)
	w.pack()

	w.create_rectangle(200, 200, 400, 400, outline="black")
	emitter1 = drawCircleWithCentrePoint(400, 200, 170, w, "red", "one")
	emitter2 = drawCircleWithCentrePoint(200, 400, 132, w, "green", "two")
	emitter3 = drawCircleWithCentrePoint(200, 200, 150, w, "blue", "three")

	w.after(1000, readLogFile, url, logsFile, w)#calling the method every second. 
	mainloop()

main()


