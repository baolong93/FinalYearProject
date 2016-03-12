import os
import time

os.chdir("/home/pi/wiringPi/433Utils/RPi_utils")
emitDeviceCode = "1"; #needed to identify where the signal is comming from
for i in range(1, 5):
	currentTime = int(time.time() * 1000000) #get rid of floating point
	currentTimeTrimed = str(currentTime)[-9:]
	os.system("sudo ./codesend " + emitDeviceCode + currentTimeTrimed) #send signal contain the time 
	time.sleep(1) #wait for 2 second before sending another signal