#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []

# Add command line arguments to the data list
data.extend(argv[1:])

# Save the updated data list to the file
save_to_json_file(data, "add_item.json")
