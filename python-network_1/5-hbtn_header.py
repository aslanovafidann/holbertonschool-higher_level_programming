#!/usr/bin/python3
"""
Takes URL as argument, sends request using requests,
prints X-Request-Id header value.
"""

import sys
import requests


def main():
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()

