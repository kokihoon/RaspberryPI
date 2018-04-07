import RPi.GPIO as GPIO 
import time 
import urllib.parse 
import urllib.request
import requests
import json
#test_url =  'http://117.16.94.160:8000'
test_url = 'http://192.168.0.113:3000/test'
time_count=0
min = 10000
max = 0
GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 7

def rc_time(pin_to_circuit, time_count):
	count = 0
	GPIO.setup(pin_to_circuit, GPIO.OUT)
	GPIO.output(pin_to_circuit, GPIO.LOW)

	time.sleep(0.5)

	GPIO.setup(pin_to_circuit, GPIO.IN)

	while(GPIO.input(pin_to_circuit) == GPIO.LOW):

		count += 1
	time_count +=1
	print(count,' ', time_count)
	return count, time_count

try:
	while True:

		num, time_count = rc_time(pin_to_circuit, time_count)

		if (num > max):
			max = num

		if (num < min):
			min = num

		if(time_count==110):
			json2 = {'max': int(max), 'min': int(min), 'GPS':{'lat':10.000, 'lng':20.0000000}}
			max = 0
			min = 10000
			r = requests.post(test_url, json = json2)
			time_count=0

except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()

