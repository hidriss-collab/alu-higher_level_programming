#!/usr/bin/python3
"""Fetches ALU intranet status using requests"""

import requests

response = requests.get("https://alu-intranet.hbtn.io/status")

print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
