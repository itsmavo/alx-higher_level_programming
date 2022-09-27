#!/usr/bin/python3
""" turns string to object """
import json

def from_json_string(my_str):
    """ returns new obj """
    return json.loads(my_str)
