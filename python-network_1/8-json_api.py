#!/usr/bin/python3
"""
Takes a letter as argument (default empty),
POSTs to /search_user with q=letter,
prints [<id>] <name> if JSON valid and not empty,
prints 'No result' if JSON empty,
prints 'Not a valid JSON' if JSON invalid.
"""

import sys
import requests


def main():
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    try:
        response = requests.post(url, data={"q": q})
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(response_json.get("id"), response_json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
