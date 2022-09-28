#!/usr/bin/python3
""" loads an object from json file """
import json

def load_from_json_file(filename):
    """ load it """
    with open(filename, mode='r', encoding='utf-8') as rd:
        return(json.load(rd))
