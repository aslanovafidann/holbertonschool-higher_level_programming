#!/usr/bin/python3
"""
Takes URL and email as arguments, sends POST request with email parameter.
Prints the response body decoded as utf-8.
"""

import sys
import urllib.request
import urllib.parse


def main():
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))


if __name__ == "__main__":
    main()
