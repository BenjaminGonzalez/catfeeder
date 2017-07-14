import getfoodsettings as getsettings
import getpyrequest as getdata
import test_body as cateaten
import time
import datetime
import re

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

continue_reading = True


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal, frame):
        global continue_reading
        print
        "Ctrl+C captured, ending read."
        continue_reading = False
        GPIO.cleanup()


# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()





while True:
    sensor_data = int(input("type float to force input: #hint below 20 is an empty bowl\n"))
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    if status == MIFAREReader.MI_OK:
        i = datetime.datetime.now()
        data = getdata.store()
        settings = getsettings.store()
        #print (data)
        settings = [[float(i) for i in line[3:6]] for line in settings]

        for line in data:
            date = line[2]
            date = re.compile('(.*?)T', re.DOTALL | re.IGNORECASE).findall(date)

            date = [x.split('-') for x in date]
            date = [[int(x) for x in line] for line in date]

        amount = date.count([i.year, i.month, i.day])
        amountyesturday = amount + date.count([i.year, i.month, i.day-1])
        if amount < settings[-1][0] or amountyesturday < settings[-1][0]*2:
            print("the cat was starving and was given some food <3")
            cateaten.sendinfo(1)
            print('the catfeeder has given the cat ', settings[-1][1], 'g of food')
            print('the catfeeder will now sleep for ', settings[-1][0], ' seconds')
            time.sleep(settings[-1][2])
        else:
            print('the cat has already eaten its fill today')


        print(settings[-1])






