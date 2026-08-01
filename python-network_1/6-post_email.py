#!/usr/bin/python3
"""POST email using requests"""

import sys
import requests

response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
print(response.text)
