"""
Purpose:
    This script is used for creating encounter for patient. Edit create_encounter_for_patient.json
    before running this script.

Usage:
  create_encounter_for_patient.py [<patientId>]

Options:
  <patientId>            : (string) ID of the patient

Example:
  python3 create_encounter_for_patient.py 14450e16-3d7d-4d2c-b993-384f2f2279e7
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





def create_encounter_for_patient(patientId):
    data = json.load(open('create_encounter_for_patient.json'))
    url = f'https://api.{c.ENV}.welkincloud.io/{c.tenantName}/{c.instanceName}' \
          f'/patients/{patientId}/encounters'
    print(url)
    r = requests.post(url, headers=headers, json=data)

    if r.ok:
        print("Created encounter for patient Successfully .....")
        print('response', r.json())
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    args = docopt(__doc__)
    patientId = args.get('<patientId>')
    create_encounter_for_patient(patientId)





