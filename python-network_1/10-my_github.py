#!/usr/bin/python3
"""Script that displays your GitHub id using Basic Authentication."""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        print(r.json().get("id"))
    except ValueError:
        print("None")
