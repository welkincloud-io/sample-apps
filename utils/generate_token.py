"""
Usage:
Note: please edit config.py file in order to generate token

generate_token.py
generated token will generate and store token in token.json.
"""

from __future__ import absolute_import
import requests

from dotenv import set_key
from config import ENV, tenantName, apiClientName, SECRET


def generate_token():
    params = {'secret': SECRET}
    r = requests.post('https://api.%s.welkincloud.io/%s/admin/api_clients/%s' % (ENV, tenantName, apiClientName),
                      json=params)
    token = r.json().get("token")
    return token


if __name__ == '__main__':
    token = generate_token()
    print(token)
    # Store token
    set_key('../.env', 'WELKIN_API_TOKEN', token)
