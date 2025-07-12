#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib and displays
the response body type, content (bytes), and decoded utf-8 content.
Adds header 'cfclearance': 'true' to bypass firewall.
"""

import urllib.request

def main():
    url = "https://intranet.hbtn.io/status"
    headers = {
        "cfclearance": "true"
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

if __name__ == "__main__":
    main()
