import getfoodsettings as getsettings
import getpyrequest as getdata
import test_body as cateaten
import time
import datetime
import re


while True:
    sensor_data = int(input("type float to force input: #hint below 20 is an empty bowl\n"))
    if sensor_data < 20:
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






