#!/usr/bin/python3
"""Displays GitHub user ID"""

import sys
import requests

response = requests.get(
    "https://api.github.com/user",
    auth=(sys.argv[1], sys.argv[2])
)

data = response.json()
print(data.get("id"))
