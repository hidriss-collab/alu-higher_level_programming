#!/usr/bin/python3
"""Displays X-Request-Id using requests"""

import sys
import requests

response = requests.get(sys.argv[1])
print(response.headers.get("X-Request-Id"))
