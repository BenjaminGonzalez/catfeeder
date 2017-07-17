import sendpydata as send
import getpyrequest as getdata
import datetime
import re



while True:
    print("#################################################")
    print("#         Welcome to the catfeeder app          #")
    print("#################################################\n")

    ask = input("Would you like to edit the settings? Y/N \n")
    if ask in ['yes','y','Y','YES']:
        quatty = input("How many meals per day? \n")
        size = input("How large would you like the meals? \n")
        mintime = input("how long after a meal should the device be locked? \n")
        send.sendinfo(quatty, size, mintime)
    elif ask in ["no", "NO", "N", "n"]:
        askagain = input("Would you like to see how much the cat has eaten today? Y/N \n")
        if askagain in ['yes','y','Y','YES']:
            data = getdata.store()
            for line in data:
                date = line[2]
                date = re.compile('(.*?)T', re.DOTALL | re.IGNORECASE).findall(date)

                date = [x.split('-') for x in date]
                date = [[int(x) for x in line] for line in date]
            i = datetime.datetime.now()
            amount = date.count([i.year, i.month, i.day])
            amountyesturday = amount + date.count([i.year, i.month, i.day - 1])
            print("The cat has eaten ", amount, "meals today and ", amountyesturday - amount, "meals yesterday\n")
    input("Press enter key to restart.\n")
    print("#################################################")
    print("#                   RESTARTING                  #")
    print("#################################################\n")







