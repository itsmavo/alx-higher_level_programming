#!/usr/bin/python3
""" loads adds saves json to file """
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    listJson = load_from_json_file("add_item.json")
except:
    listJson = []

for i in sys.argv[1:]:
    listJson.append(i)
save_to_json_file(listJson, "add_item.json")
