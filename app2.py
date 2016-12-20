    #!/usr/bin/env python
# Module     : SysTrayIcon.py
# Synopsis   : Windows System tray icon.
# Programmer : Simon Brunning - simon@brunningonline.net
# Date       : 11 April 2005
# Notes      : Based on (i.e. ripped off from) Mark Hammond's
#              win32gui_taskbar.py and win32gui_menu.py demos from PyWin32
'''TODO

For now, the demo at the bottom shows how to use it...'''
         
from threading import Thread
from time import sleep

monitor = True

def threaded_function(arg):
    for i in range(arg):
        print "running"
        sleep(1)

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


def eventTimeCubeListen():
    import serial
    import io
    import datetime
    import time
    global monitor
    file = open('timeTracker.csv', 'a')
    ser = serial.Serial('COM3')  # open serial port
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

    #print ser.name         # check which port was really used
    print "Monitor of "+ser.name+" Started"

    ser.flushInput()
    ser.flushOutput()

    try: 
        while True:
            print monitor
            if monitor:
                i = datetime.datetime.now()
                data_raw = ser.readline()
                file.write(printProject(data_raw) + "," + unicode(i.year) +  "/" + unicode(i.month) + "/" + unicode(i.day) + "," + unicode(time.strftime("%H:%M:%S"))+"\n")
                file.flush()
                print printProject(data_raw) + "    " + unicode(datetime.datetime.now())
    except KeyboardInterrupt:
        pass

    print "Monitor of "+ser.name+" Stopped"
    ser.close()


if __name__ == '__main__':
    import itertools, glob
    import SysTrayIcon


    icons = itertools.cycle(glob.glob('*.ico'))
    hover_text = "SysTrayIcon.py Demo"
    def hello(sysTrayIcon): print "Hello World."
    def simon(sysTrayIcon): print "Hello Simon."
    def switch_icon(sysTrayIcon):
        sysTrayIcon.icon = icons.next()
        sysTrayIcon.refresh_icon()
    def monitorSwitch(sysTrayIcon):
        global monitor
        print monitor
        monitor = not monitor
        print monitor
        #if monitor:
            #thread.start()
        
        
    menu_options = (('Monitor', None, monitorSwitch),
                    ('Switch Icon', None, switch_icon),
                    ('A sub-menu', icons.next(), (('Say Hello to Simon', icons.next(), simon),
                                                  ('Switch Icon', icons.next(), switch_icon),
                                                 ))
                   )
    def bye(sysTrayIcon): 
        monitor = False
        print 'Bye, then.'

    
    thread = Thread(target=eventTimeCubeListen)
    thread.daemon = True 
    thread.start()
    #thread.join()

    SysTrayIcon.SysTrayIcon(icons.next(), hover_text, menu_options, on_quit=bye, default_menu_index=1)
