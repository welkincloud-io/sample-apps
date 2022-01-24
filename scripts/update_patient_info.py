"""
Purpose:
    Use this script to update patient information.
    Note: Using the Patch request, you should specify only those fields that you want to update.
    All fields missing in the request will retain their previous values.
Usage:
    update_patient_info.py [<patientId>]

Options:
  <patientId>                 : (string) ID of the patient

Example:
  python update_patient_info.py 14450e16-3d7d-4d2c-b993-384f2f2279e7
"""

import requests
import json
from dotenv import get_key
from docopt import docopt
from config import Config as c

token = get_key('../.env', 'WELKIN_API_TOKEN')
headers = {"Authorization": "Bearer {}".format(token)}


def update_patient_info(patientId):
    data = json.load(open('update_patient_info.json'))
    url = f'https://api.{c.ENV}.welkincloud.io/{c.tenantName}/{c.instanceName}/patients/{patientId}'
    print(url)

    r = requests.post(url, headers=headers, json=data)

    if r.ok:
        print("Updated Patient info  Successfully")
        print('response', r.json())
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    args = docopt(__doc__)
    patientId = args.get('<patientId>')
    update_patient_info(patientId)
