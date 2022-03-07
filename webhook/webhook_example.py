"""
webhook using a simple python example.

Usage:
Change  webhook_url to your pipedream URL.
data variable contains sample data, you can change it if required.
response will be either string or json. if data is string response.json() method
will give parsing error.
"""

import requests
import json

# Use Pipedream  URL here
webhook_url = 'https://eoh1qxhm4wnl0zn.m.pipedream.net'

# Request body data
data = {"patient_id": "098212a0-4476-4573-8c25-31c936c65013",
        "firstName": "Jonh",
        "lastName": "Smith",
        "primaryLanguage": "ENGLISH"
        }

response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type':'application/json'})

# Response data
print(response.text)
