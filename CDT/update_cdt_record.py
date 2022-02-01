"""
Purpose:
    Use this script to update cdt record by using id

Usage:
  update_cdt_record.py [<patientId>] [<cdtName>] [<cdtRecordId>]

Options:
  <patientId>                 : (string) ID of the patient
  <cdtName>                    : name of the cdt
  <cdtRecordId>                : cdt record id
Example:
  python update_cdt_record.py 14450e16-3d7d-4d2c-b993-384f2f2279e7 cdt-vitals fe60ebdb-f7cc-4d44-910c-6f3114befacf

"""
import os
import sys
import requests
from docopt import docopt
import json
from dotenv import get_key

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config as C

token = get_key('../.env', 'WELKIN_API_TOKEN')
headers = { "Authorization": "Bearer {}".format(token)}


def update_cdt_record(patientId, cdtName, cdtRecordId):
    data = json.load(open('CDT/update_cdt_record.json'))
    print('data', data)
    url =  f"https://api.{C.ENV}.welkincloud.io/{C.tenantName}/{C.instanceName}" \
           f"/patients/{patientId}/cdts/{cdtName}/{cdtRecordId}"
    print('URL',url)
    r = requests.patch(url, headers=headers, json=data)
    if r.ok:
        print("Updated  CDT record Successfully")
        print(r)
    else:
        print(r.status_code, r.text)


if __name__ == '__main__':
    args = docopt(__doc__)
    patientId = args.get('<patientId>')
    cdtName = args.get('<cdtName>')
    cdtRecordId = args.get('<cdtRecordId>')
    update_cdt_record(patientId, cdtName, cdtRecordId)
