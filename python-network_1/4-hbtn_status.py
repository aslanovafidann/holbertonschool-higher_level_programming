#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests.
Prints the response body type and content as string.
"""

import requests


def main():
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()

