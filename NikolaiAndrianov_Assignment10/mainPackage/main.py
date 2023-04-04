#Name: Nikolai Andrianov - Nathan Lowe, Hugo Bourinbayar, Payton Cook, Jimmy Zimmer
#email: lowenc@mail.uc.edu, bourinhh@mail.uc.edu, cookpk@mail.uc.edu, zimmejc@mail.uc.edu
#Assignment Title: Assignment 10
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Utilizes a public API to extract data from a JSON 
#Citations: 
#Anything else that's relevant:

# main.py

import requests
import json
from iterateOverADictionaryPackage.iterateOverADictionary import *

# Make a request to a web server and store the results in response
response = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=acad,grsm&api_key=pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3')
json_string = response.content                          #
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
    
#print(parsed_json)
#print(parsed_json['data'][0]['description'])
#print(parsed_json['data'][0]['directionsInfo'])
    
total = int(parsed_json['total'])        # The number of parks that were returned
# I Just want the descriptions of the alerts
for park in parsed_json['data']:
    print (park['description'])


#Invoke my function in the other module, pass it parsed_json
#print(iterate_dictionary(parsed_json))