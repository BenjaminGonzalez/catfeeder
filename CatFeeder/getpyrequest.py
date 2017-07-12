import urllib3
import config
import certifi
import re

def store():

	http = urllib3.PoolManager(
		cert_reqs='CERT_REQUIRED',  # Force certificate check.
		ca_certs=certifi.where(),  # Path to the Certifi bundle.
	)

	url = 'https://iotmms' + config.hcp_account_id + config.hcp_landscape_host + '/com.sap.iotservices.mms/v1/api/http/data/' + str(
		config.device_id)  # 'https://iotmms_on_your_trial_system.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/1'

	headers = urllib3.util.make_headers()

	# use with authentication
	# please insert correct OAuth token
	headers['Authorization'] = 'Basic STM0MjUwNTpUaGVvYmVhcmZhdDI='

	r = http.urlopen('GET',
					 'https://iotmmsi342505trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/app.svc/NEO_AUDWFPK2YVE1TF8J4HHQQQYVJ.T_IOT_DE2D4CAFE79B98BCAD7A',
					 headers=headers)

	print(r.status)
	# print(r.data)


	page = r.data.decode("utf-8")

	out = re.compile('<m:properties>(.*?)</m:properties>', re.DOTALL | re.IGNORECASE).findall(page)

	final_array = []
	for i in out:
		inside = re.compile('>(.*?)<', re.DOTALL | re.IGNORECASE).findall(i)
		final_array += [list(filter(None, inside))]

	#for i in final_array:
		#print(i)
	return final_array




