#!/usr/bin/python3
"""
Takes URL as argument, sends request using urllib, 
prints the X-Request-Id header value.
"""

import sys
import urllib.request


def main():
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
