#!/usr/bin/python3
""" appends to a file or creates it """

def append_write(filename="", text=""):
    """ appends or creates """
    with open(filename, mode="a+", encoding='utf-8') as ap:
        return(ap.write(text))
