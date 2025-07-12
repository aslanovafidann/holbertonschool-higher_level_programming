#!/usr/bin/python3
"""
Takes GitHub username and personal access token,
uses Basic Auth to get user info and prints id.
Prints None if authentication fails.
"""

import sys
import requests


def main():
    username = sys.argv[1]
    token = sys.argv[2]
    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print(None)


if __name__ == "__main__":
    main()
