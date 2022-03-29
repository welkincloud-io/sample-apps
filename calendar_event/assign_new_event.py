"""
Purpose:
    This script is for assigning new event to existing encounter for patient. Edit assign_new_event.json
    before running this script.

Usage:
  assign_new_event.py [<patientId>] [<encounterId>]

Options:
  <patientId>            : (string) ID of the patient
  <encounterId>          : encounter Id

Example:
  python3 assign_new_event.py 14450e16-3d7d-4d2c-b993-384f2f2279e7 030d1599-d6cd-4448-a140-c22b1cd39372
"""

import os
import sys
import json
import requests
from docopt import docopt
from dotenv import get_key

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config as c

token = get_key('../.env', 'WELKIN_API_TOKEN')
headers = {"Authorization": "Bearer {}".format(token)}


def assign_new_event(patientId, encounterId):
    data = json.load(open('assign_new_event.json'))
    url = f'https://api.{c.ENV}.welkincloud.io/{c.tenantName}/{c.instanceName}' \
          f'/patients/{patientId}/encounters/{encounterId}'
    print(url)
    r = requests.post(url, headers=headers, json=data)

    if r.ok:
        print("Assigned new event to encounter Successfully .....")
        print('response', r.json())
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    args = docopt(__doc__)
    patientId = args.get('<patientId>')
    encounterId = args.get('<encounterId>')
    assign_new_event(patientId, encounterId)





