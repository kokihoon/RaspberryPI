from pynmea import nmea
#import matplotlib.pyplot as plt
import serial, time, sys, threading, datetime, shutil
ser = 0
lat = 0
long = 0
pos_x = 0
pos_y = 0
alt = 0
i = 0 #x units for altitude measurment

def altitude():
	global alt, i
	
	#we want to create temporary file to parse, so that we don't mess with the nmea.txt file
	#f1 = open('test.txt', 'w') #creates and opens a writable txt file
	#f1.truncate() #erase contents of file
	#shutil.copyfile('test.txt', 'temp.txt') #copy nmea.txt to temp.txt
	#f1.close() #close writable file
	
	f1 = open('temp.txt', 'r') #open and read only
	#print(f1)
	try: #best to use try/finally so that the file opens and closes correctly
		#print("qwe")
             #   print(f2)
		for line in f1: #read each line in temp.txt
                       # print(line[4])
			if(line[4] == 'G'): # fifth character in $GPGGA
				if(len(line) > 50): # when there is a lock, the sentence gets filled with data
					#print line
					gpgga = nmea.GPGGA()
					gpgga.parse(line)
					alt = gpgga.antenna_altitude
					i +=1 #increment the counter
				
#					plt.scatter(x=[i], y=[float(alt)], s = 1, c='r') #plot each point
	finally:
            print("error")
            f1.close()
	i=0
	
altitude()
	#axis is autoscaled
#	plt.ylabel('meters')
#	plt.xlabel('counts')
#	plt.title('ALTITUDE')
#	plt.show()