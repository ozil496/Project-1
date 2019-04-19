import urllib.request
import json
import sys
import os
import time
import datetime
from darksky import forecast
from datetime import date, timedelta

if not os.path.exists ("json_files"):
	os.mkdir("json_files")
	
api_key = sys.argv[1]

CLEMSON = 34.683107, -82.837638

for i in range(10):
	response = urllib.request.urlopen('https://api.darksky.net/forecast/' + api_key + '/34.683107,-82.837638')
	json_response = json.load(response)
	
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	
	f = open("json_files/darksky" + current_time_stamp + ".json","w")
	f.write(json.dumps(json_response, indent=4))
	f.close()
	print(current_time_stamp)
	time.sleep(20)
