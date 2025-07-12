#!/usr/bin/python3
"""
Takes URL as argument, sends request, prints body.
If status code >= 400, prints "Error code: <status_code>".
"""

import sys
import requests


def main():
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()
