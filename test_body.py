import random
import time
import config

timestamp = int(time.time())

devicetype = '", "messages":[{"devicetype":"' +['flow', 'port'][random.randint(0, 1)]
timestamp = ', "timestamp":' + str(timestamp)
longitude = '", "longitude":' +str(random.uniform(-180, 180))
latitude = ', "latitude":'+str(random.uniform(-90, 90))
temp = ', "temp":'+str(random.uniform(-20, 60))
turb = ', "turb":'+str(random.uniform(0, 10))
ph = ', "ph":'+str(random.uniform(1, 7))
conduct =', "conduct":'+str(random.uniform(0, 1))

body = '{"mode":"async", "messageType":"' + str(
    config.message_type_id_From_device) + devicetype + longitude + latitude + temp + turb + ph + conduct + timestamp + '}]}'

print (body)

body='{"mode":"async", "messageType":"' + str(config.message_type_id_From_device) + '", "messages":[{"sensor":"slider_device", "value":"' + str(5) + '", "timestamp":' + str(timestamp) + '}]}'

