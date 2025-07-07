#!/usr/bin/python3
"""Script that adds all arguments to a list and saves them in a JSON file."""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Mövcud fayldan oxu, əgər varsa
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Yeni arqumentləri əlavə et (argv[0] skript adıdır)
items.extend(sys.argv[1:])

# Yadda saxla
save_to_json_file(items, filename)
