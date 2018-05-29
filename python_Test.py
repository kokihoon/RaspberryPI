import time
from time import strftime
from pynmea import nmea


def dms_to_dec(value, dir):
    mPos = value.find(".")
    print(mPos)
    degree = float(value[:mPos])
    print(degree)
    minute = float(value[mPos:])

    converted_degree = float(degree) + float(minute) / float(60)

    if dir == "W":
        converted_degree = -converted_degree
    elif dir == "S":
        converted_degree = -converted_degree

    return "%.9f" % float(round(converted_degree, 8))


def convert(inputName, outputName):
    data = open(inputName, "r")
    file = open(outputName, "w")

    file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n <gpx version=\"1.0\">\n")
    file.write("<tk>\n<trkseg>\n")

    while(True):
        data.seek(data.tell())
        time.sleep(1)
        for line in data:
            if line[4] == 'G':
                gpgga = nmea.GPGGA()
                gpgga.parse(line)
                lats = gpgga.latitude
                longs = gpgga.longitude
                print(lats, longs)


convert('/home/pi/test3.txt', 'nmea.gpx')
print("Done!")

