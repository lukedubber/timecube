import serial
import io
import datetime
import time
import os.path
import sys


fileName = 'timeTracker2.csv'


file = open(fileName, 'a')
ser = serial.Serial('COM3')  # open serial port
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

# Function definition is here
def printProject(str=''):
    "This prints a passed string into this function"
    str = str.rstrip('\n').rstrip('\r')
    return projects(str)

def projects(x):
    return {
        'd5544c3a': 'PAUSE',
        '4173d284': 'CFAC',
        'ed101a2e': 'KACA(RAS)',
        '6e402419': 'SS',
        'b5d54e3a': 'ADMIN',
        'd533fc2d': 'RA',
        '8f9c490' : "LMJ",
        '784079'  : "DERM"

    }[x]


print ser.name         # check which port was really used

ser.flushInput()
ser.flushOutput()

try: 
    while True:
        i = datetime.datetime.now()
        data_raw = ser.readline()
        file.write(printProject(data_raw) + "," + unicode(i.year) +  "/" + unicode(i.month) + "/" + unicode(i.day) + "," + unicode(time.strftime("%H:%M:%S"))+"\n")
        file.flush()
        print printProject(data_raw) + "    " + unicode(datetime.datetime.now())
except KeyboardInterrupt:
    pass

ser.close()