#!/usr/bin/python3
"""Search API"""

import sys
import requests

letter = "" if len(sys.argv) == 1 else sys.argv[1]

response = requests.post(
    "http://0.0.0.0:5000/search_user",
    data={"q": letter}
)

try:
    data = response.json()
    if data:
        print("[{}] {}".format(data.get("id"), data.get("name")))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
