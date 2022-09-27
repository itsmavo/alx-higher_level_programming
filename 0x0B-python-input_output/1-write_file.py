#!/usr/bin/python3
""" file-writing function """
def write_file(filename="", text=""):
    """ writes string to utf8 file """
    with open(filename, mode='w', encoding='utf-8') as rd:
        return rd.write(text)
