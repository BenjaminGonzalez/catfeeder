import urllib3
import time

try:
    import config
except ImportError:
    print("Please copy template-config.py to config.py and configure appropriately !");
    exit();

debug_communication = 0

def send_to_hcp(http, url, headers,dev,long,lat,tem,tur,ph,con):
    timestamp = int(time.time())
    devicetype = '", "messages":[{"devicetype":"' + dev#input("What is your device Type: \n ")
    timestamp = ', "timestamp":' + str(timestamp)
    longitude = '", "longitude":' + long#input("What is your Longitude: \n")
    latitude = ', "latitude":' + lat #input("What is your Latitude: \n")
    temp = ', "temp":' + tem#input("What is your measured temperature \n")
    turb = ', "turb":' + tur# input("What is your measured turbitity: \n")
    ph = ', "ph":' + ph#input("What is your ph: \n ")
    conduct = ', "conduct":' + con# input("What is your conductivity: \n")
    body = '{"mode":"async", "messageType":"' + str(
        config.message_type_id_From_device) + devicetype + longitude + latitude + temp + turb + ph + conduct + timestamp + '}]}'
    #print('msg ID, ', config.message_type_id_From_device)
    print(body)
    r = http.urlopen('POST', url, body=body, headers=headers)
    #print('POST', url, body, headers)
    if (debug_communication == 1):
        print("send_to_hcp():" + str(r.status))
    print(r.data)

def sendinfo(dev,long,lat,tem,tur,ph,con):
    try:
        urllib3.disable_warnings()
    except:
        print(
            "urllib3.disable_warnings() failed - get a recent enough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.")

    # use with or without proxy
    if (config.proxy_url == ''):
        http = urllib3.PoolManager()
    else:
        http = urllib3.proxy_from_url(config.proxy_url)

    url = 'https://iotmms' + config.hcp_account_id + config.hcp_landscape_host + '/com.sap.iotservices.mms/v1/api/http/data/' + str(
        config.device_id)
    # print("Host   " + config.hcp_account_id + config.hcp_landscape_host)

    headers = urllib3.util.make_headers(user_agent=None)

    # use with authentication
    headers['Authorization'] = 'Bearer ' + config.oauth_credentials_for_device
    headers['Content-Type'] = 'application/json;charset=utf-8'

    send_to_hcp(http, url, headers,str(dev), str(long), str(lat), str(tem), str(tur), str(ph), str(con))


#sendinfo("port", 1.22334343, 43.2343, 23.44, 9.33, 1.5, 0.95)