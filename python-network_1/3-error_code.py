#!/usr/bin/python3
"""
Takes URL as argument, sends request, prints body decoded utf-8.
If HTTP error occurs, prints "Error code: " and status code.
"""

import sys
import urllib.request
import urllib.error


def main():
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
