"""
Purpose:
    We use this script to create calendar event.
    Edit create_calendar_event.json file before running this script.

Usage:
  create_calendar_event.py

Example:
  python3 create_calendar_event.py
"""

import os
import sys
import json
import requests
from dotenv import get_key

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config as c

token = get_key('../.env', 'WELKIN_API_TOKEN')
headers = {"Authorization": "Bearer {}".format(token)}


def create_calendar_event():
    data = json.load(open('create_calendar_event.json'))
    url = f'https://api.{c.ENV}.welkincloud.io/{c.tenantName}/{c.instanceName}/calendar/events'
    print(url)
    r = requests.post(url, headers=headers, json=data)

    if r.ok:
        print("Calendar Event Created Successfully .....")
        print('response', r.json())
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    create_calendar_event()
