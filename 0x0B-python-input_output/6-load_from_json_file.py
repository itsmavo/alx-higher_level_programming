#!/usr/bin/python3
import json
""" loads an object from json file """

def load_from_json_file(filename):
    """ load it """
    with open(filename, mode='r', encoding='utf-8') as rd:
        return(json.load(rd))
