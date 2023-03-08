'''
We’ll be working with the Open Notify API, which gives access to data about the international space station. It’s a great API for learning because it has a very simple design, and doesn’t require authentication. We’ll teach you how to use an API that requires authentication in a later post.
'''

import requests

#connect to an endpoint which doesnot exist
#response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")

#print(response.status_code)

#The first endpoint we’ll use is http://api.open-notify.org/astros.json, which returns data about astronauts currently in space.
response = requests.get("https://api.open-notify.org/astros.json")
print(response.status_code)

print(response.json())

'''
Response
{'message': 'success', 'people': [{'name': 'Alexey Ovchinin', 'craft': 'ISS'}, {'name': 'Nick Hague', 'craft': 'ISS'}, {'name': 'Christina Koch', 'craft': 'ISS'}, {'name': 'Alexander Skvortsov', 'craft': 'ISS'}, {'name': 'Luca Parmitano', 'craft': 'ISS'}, {'name': 'Andrew Morgan', 'craft': 'ISS'}], 'number': 6}
'''

import json

'''
The json library has two main functions:

json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
json.loads() — Takes a JSON string, and converts (loads) it to a Python object.
'''

def jprint(obj):
	text = json.dumps(obj,sort_keys=True,indent=4)
	print(text)

jprint(response.json())

'''
{
    "message": "success",
    "number": 6,
    "people": [
        {
            "craft": "ISS",
            "name": "Alexey Ovchinin"
        },
        {
            "craft": "ISS",
            "name": "Nick Hague"
        },
        {
            "craft": "ISS",
            "name": "Christina Koch"
        },
        {
            "craft": "ISS",
            "name": "Alexander Skvortsov"
        },
        {
            "craft": "ISS",
            "name": "Luca Parmitano"
        },
        {
            "craft": "ISS",
            "name": "Andrew Morgan"
        }
    ]
}
'''

'''
It’s very common, however, to have an API endpoint that requires us to specify parameters. An example of this the https://api.open-notify.org/iss-pass.json endpoint. This endpoint tells us the next times that the international space station will pass over a given location on the earth.
'''
#New York City
parameters={
		"lat":40.71,
		"lon": -74
		}
#https://api.open-notify.org/iss-pass.json?lat=40.71&lon;=-74

response = requests.get("https://api.open-notify.org/iss-pass.json", params=parameters)
jprint(response.json())

'''
{
    "message": "success",
    "request": {
        "altitude": 100,
        "datetime": 1568062811,
        "latitude": 40.71,
        "longitude": -74.0,
        "passes": 5
    },
    "response": [
        {
            "duration": 395,
            "risetime": 1568082479
        },
        {
            "duration": 640,
            "risetime": 1568088118
        },
        {
            "duration": 614,
            "risetime": 1568093944
        },
        {
            "duration": 555,
            "risetime": 1568099831
        },
        {
            "duration": 595,
            "risetime": 1568105674
        }
    ]
}
'''

'''
Understanding the Pass Times
The JSON response matches what the documentation specified:

A dictionary with three keys
The third key, response, contains a list of pass times
Each pass time is a dictionary with risetime (pass start time) and duration keys.
'''

pass_times = response.json()['response']
jprint(pass_time)

'''
[
    {
        "duration": 395,
        "risetime": 1568082479
    },
    {
        "duration": 640,
        "risetime": 1568088118
    },
    {
        "duration": 614,
        "risetime": 1568093944
    },
    {
        "duration": 555,
        "risetime": 1568099831
    },
    {
        "duration": 595,
        "risetime": 1568105674
    }
]
'''

#Extract rise times in loop

risetime = []

for i in pass_time:
	time = d['risetime']
	risetime.append(time)

print(risetime)

#[1568082479, 1568088118, 1568093944, 1568099831, 1568105674]

'''
These times are difficult to understand – they are in a format known as timestamp or epoch. Essentially the time is measured in the number of seconds since January 1st 1970. We can use the Python datetime.fromtimestamp() method to convert these into easier to understand times:
'''

from datetime import datetime

times = []

for rt in risetime:
	time = datetime.fromtimestamp(rt)
	times.append(time)

print(times)

'''
It looks like the ISS passes over New York City often – the next five times happen within a seven hour period!
2019-09-09 21:27:59
2019-09-09 23:01:58
2019-09-10 00:39:04
2019-09-10 02:17:11
2019-09-10 03:54:34
'''