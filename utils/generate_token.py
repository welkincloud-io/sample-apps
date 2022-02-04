"""
Usage:
Note: please edit config.py file in order to generate token

python3 generate_token.py
generated token will be automatically used in header. You need not to copy paste it.
"""
import os
import sys
import requests

from dotenv import set_key

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config as C


def generate_token():
    params = {'secret': C.SECRET}
    r = requests.post(f"https://api.{C.ENV}.welkincloud.io/{C.tenantName}/admin/api_clients/{C.apiClientName}"
                      , json=params)
    token = r.json().get("token")
    return token


if __name__ == '__main__':
    token = generate_token()
    print(token)
    # Store token
    set_key('../.env', 'WELKIN_API_TOKEN', token)
