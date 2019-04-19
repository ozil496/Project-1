import json
import pandas as pd
import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")
j = 1
i = 1
df = pd.DataFrame()

for one_file_name in glob.glob("json_files/*.json"):
	f = open(one_file_name, "r", encoding="utf-8")
	json_data = json.load(f)
	
	
	df = df.append({
		'precip':json_data['currently']['precipProbability'],
		'temp':json_data['currently']['temperature'],
		'summary':json_data['currently']['summary'],
		'time':json_data['currently']['time'],
		'cloud cover':json_data['currently']['cloudCover'],
		'humidity':json_data['currently']['humidity'],
		'Feels Like Temp':json_data['currently']['apparentTemperature'],
		'wind speed':json_data['currently']['windSpeed'],
		'wind gust':json_data['currently']['windGust'],
		'nearest storm distance':json_data['currently']['nearestStormDistance']
		
		}, ignore_index=True)
		
print(df)
df.to_csv("parsed_files/darksky_dataset.csv")
