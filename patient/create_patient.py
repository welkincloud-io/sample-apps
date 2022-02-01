"""
Purpose:
  Creating a new Patient. Before running this script
  edit create_patient.json file add patient information in  json file.
Usage:
  create_patient.py

Example:
  python create_patient.py
"""

import os
import sys
import requests
import json
from dotenv import get_key

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config as c

token = get_key('../.env', 'WELKIN_API_TOKEN')
headers = {"Authorization": "Bearer {}".format(token)}


def create_patient(json_data):
    url = f"https://api.{c.ENV}.welkincloud.io/{c.tenantName}/{c.instanceName}/patients"
    print(url)
    r = requests.post(url, headers=headers, json=json_data)

    if r.ok:
        print("Patient Created Successfully")
        print(r)
        print(r.json())
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    data = json.load(open('patient/create_patient.json'))
    create_patient(data)
