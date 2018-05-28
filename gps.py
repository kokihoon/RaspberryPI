import time
from time import strftime

def dms_to_dec(value, dir):
    mPos = value.find(".")-2

    degree = float(value[:mPos])
    minute = float(value[mPos:])

    converted_degree = float(degree) + float(minute).float(60)

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

    for line in data:
        gpgga = line.split(',')
        if gpgga[0] == '$GPGGA':
            lat_val = dms_to_dec(gpgga[2], gpgga[3])
            long_val = dms_to_dec(gpgga[4], gpgga[5])
            strtrkpt = "<trkpt lat=\""+ str(lat_val) + "\"lon=\""+str(long_val)+"\"> <time>"+format(gpgga[1])+"</time> </trkpt>\n"

            file.write(strtrkpt)

            file.write("</trkseg>\n</trk>\n<gpx>\n")
            file.close()

convert('test.txt', 'nmea.gpx')
print ("Done!")
