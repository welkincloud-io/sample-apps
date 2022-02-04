"""
Purpose:
    We can assign a patient to  a program using this Script

Usage:
  assign_to_program.py [<patientId>] [<programName>]

Options:
  <patientId>            : (string) ID of the patient
  <programName>          : name of the program

Example:
  python3 assign_to_program.py 14450e16-3d7d-4d2c-b993-384f2f2279e7 prog-sample
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


def assign_to_program(patientId, programName):
    data = json.load(open('patient/assign_to_program.json'))
    url = f'https://api.{c.ENV}.welkincloud.io/{c.tenantName}/{c.instanceName}' \
          f'/patients/{patientId}/programs/{programName}'
    print(url)
    r = requests.patch(url, headers=headers, json=data)

    if r.ok:
        print("Patient Assigned to program Successfully .....")
        print('response', r.json())
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    args = docopt(__doc__)
    patientId = args.get('<patientId>')
    programName = args.get('<programName>')
    assign_to_program(patientId, programName)
