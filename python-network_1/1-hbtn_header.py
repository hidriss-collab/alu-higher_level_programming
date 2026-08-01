#!/usr/bin/python3
"""Displays the X-Request-Id header"""

import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get("X-Request-Id"))
