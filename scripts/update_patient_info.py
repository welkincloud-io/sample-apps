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
import os
import json
from docopt import docopt
from config import Config

token = os.environ['WELKIN_API_TOKEN']
headers = {"Authorization": "Bearer {}".format(token)}


def update_patient_info(patientId):
    data = json.load(open('update_patient_info.json'))
    url = 'https://api.%s.welkincloud.io/%s/%s/patients/%s'\
        % (Config.ENV, Config.tenantName, Config.instanceName, patientId)

    r = requests.post(url, headers=headers, json=data)

    if r.ok:
        print("Updated Patient info  Successfully")
        print('response', r)
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    args = docopt(__doc__)
    patientId = args.get('<patientId>')
    update_patient_info(patientId)
