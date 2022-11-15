'''
**************************************************************************************************
Name: Jon Buck, Alyssa Hughes
email: buckjn@mail.uc.edu, hugheah@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can call an API and submit a data request in Eclipse
Citations: 
    
Anything else that's relevant: Not at this time
**************************************************************************************************
'''

import json
import requests

#call API to get data
response = requests.get('https://api.usa.gov/crime/fbi/sapi/api/summarized/state/oh/property-crime/2007/2007?api_key=AuPyoB7VYfkvdFkPpV3rCkT75bBDZuWkHMF80K6C')

#parse data into a python dictionary
json_string = response.content
parsed_json = json.loads(json_string)

#print the data from the newly created dictionary
for test in parsed_json['results']:
    print(test)

#check that the request was successful, if not return the status code
if response.status_code == 200:
    print("Query executed successfully.")
else:
    print(response.status_code)      #status code is to check that the request went through, 200 is a successful request
    