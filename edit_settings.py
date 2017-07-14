import sendpydata as send


while True:
    print('###################')
    ask = input("Would you like to edit the settings? Y/N \n")
    if ask in ['yes','y','Y','YES']:
        quatty = input("How many meals per day? \n")
        size = input("How large would you like the meals? \n")
        mintime = input("how long after a meal should the device be locked? \n")
        send.sendinfo(quatty, size, mintime)






