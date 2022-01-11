"""
Purpose:
    We can create new cdt record using this Script

Usage:
  create_cdt.py [<patientId>] [<cdtName>]

Options:
  <patientId>                 : (string) ID of the patient
  <cdtName>                    : name of the cdt

Example:
  python create_cdt.py 14450e16-3d7d-4d2c-b993-384f2f2279e7 cdt-vitals

"""
from __future__ import absolute_import

import requests
from docopt import docopt
import json

from dotenv import get_key
from config import Config

token = get_key('../.env','WELKIN_API_TOKEN')
headers = { "Authorization": "Bearer {}".format(token)}

data = json.load(open('create_cdt.json'))

def create_cdt(patientId, cdtName):
    data = json.load(open('create_cdt.json'))
    print('data',data)
    url = 'https://api.%s.welkincloud.io/%s/%s/patients/%s/cdts/%s' \
        %(Config.ENV, Config.tenantName, Config.instanceName, patientId, cdtName)
    print('URL', url)
    r = requests.post(url, headers=headers, json=data)
    if r.ok:
        print("Created CDT record Successfully")
        print('response', r)
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    args = docopt(__doc__)
    patient_id = args.get('<patientId>')
    cdtName = args.get('<cdtName>')
    create_cdt(patient_id, cdtName)
