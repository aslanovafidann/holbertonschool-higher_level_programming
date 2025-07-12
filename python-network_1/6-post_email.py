#!/usr/bin/python3
"""
Takes URL and email as arguments, sends POST request with email parameter.
Prints response body.
"""

import sys
import requests


def main():
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={"email": email})
    print(response.text)


if __name__ == "__main__":
    main()
