#Name: Nikolai Andrianov - Nathan Lowe, Hugo Bourinbayar, Payton Cook, Jimmy Zimmer
#email: lowenc@mail.uc.edu, bourinhh@mail.uc.edu, cookpk@mail.uc.edu, zimmejc@mail.uc.edu
#Assignment Title: Assignment 10
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Utilizes a public API to extract data from a JSON. This one is the Current weather of Cincinnati.
#Citations: https://www.weatherapi.com/docs/
#Anything else that's relevant:

# main.py

import requests
import json
from iterateOverADictionaryPackage.iterateOverADictionary import *

# Make a request to a web server and store the results in response
response = requests.get('http://api.weatherapi.com/v1/current.json?key=76cb4cf35a8a41f8b3912556230404&q=Cincinnati&aqi=no')
json_string = response.content                          #
    
parsed_json = json.loads(json_string) # Now we have a python dictionary

#Breaks the JSON into usable parts for printing text
name = (parsed_json['location']['name'])
region = (parsed_json['location']['region'])
localTime = (parsed_json['location']['localtime'])
temp = (parsed_json['current']['temp_f'])
condition = (parsed_json['current']['condition']['text'])
feelsLikeTemp = (parsed_json['current']['feelslike_f'])
windSpeed = (parsed_json['current']['wind_mph'])
windDirection = (parsed_json['current']['wind_dir'])

#Prints the useful information pulled from the API in a readable format
print(f'The weather for {name}, {region}. The Current time is {localTime[10:16]}') 
print(f'The temperture outside is {temp}°F and it feels like {feelsLikeTemp}°F')
print(f'The current condition is: {condition}')
print(f'The current wind speed is: {windSpeed} MPH {windDirection}')
