#!/usr/bin/python3
""" saves object as json string """
import json

def save_to_json_file(my_obj, filename):
    """ json string dump """
    with open(filename, mode='w', encoding='utf-8') as wt:
        wt.write(json.dumps(my_obj))
