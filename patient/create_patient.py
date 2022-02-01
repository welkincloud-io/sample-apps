"""
Purpose:
  Creating a new Patient

Usage:
  create_patient.py

Example:
  python change_phase.py 14450e16-3d7d-4d2c-b993-384f2f2279e7 prog-sample
"""

import requests
import json
from dotenv import get_key
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
    data = json.load(open('create_patient.json'))
    create_patient(data)
