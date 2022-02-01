"""
Purpose:
    We can assign a patient already in program to any phase of program using this Script

Usage:
  change_phase.py [<patientId>] [<programName>]

Options:
  <patientId>                 : (string) ID of the patient
  <programName>                    : name of the program

Example:
  python change_phase.py 14450e16-3d7d-4d2c-b993-384f2f2279e7 prog-sample
"""

import requests
from docopt import docopt
import json
from dotenv import get_key
from config import Config as c

token = get_key('../.env', 'WELKIN_API_TOKEN')
headers = {"Authorization": "Bearer {}".format(token)}


def change_phase(patientId, programName):
    data = json.load(open('change_phase.json'))
    url = f'https://api.{c.ENV}.welkincloud.io/{c.tenantName}/{c.instanceName}' \
          f'/patients/{patientId}/programs/{programName}/phases'

    print(url)
    r = requests.patch(url, headers=headers, json=data)
    if r.ok:
        print('Patient Assigned to Phase successfully.....')
        print('response', r.json())
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    args = docopt(__doc__)
    patientId = args.get('<patientId>')
    programName = args.get('<programName>')
    change_phase(patientId, programName)
