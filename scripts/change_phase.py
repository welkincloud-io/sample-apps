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

from __future__ import absolute_import
import requests
from docopt import docopt
import json
from dotenv import get_key
from config import Config

token = get_key('../.env','WELKIN_API_TOKEN')
headers = { "Authorization": "Bearer {}".format(token)}


def change_phase(patientId, programName):
    data = json.load(open('change_phase.json'))
    print('data', data)
    url = 'https://api.%s.welkincloud.io/%s/%s/patients/%s/programs/%s/phases' \
        %(Config.ENV, Config.tenantName, Config.instanceName, patientId, programName)
    print('URL', url)
    r = requests.patch(url, headers=headers, json=data)
    if r.ok:
        print('Patient Assigned to "%s" Phase successfully.....' %data['phaseName'])
        print('response', r)
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    args = docopt(__doc__)
    patientId  = args.get('<patientId>')
    programName = args.get('<programName>')
    change_phase(patientId, programName)
