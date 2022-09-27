#!/usr/bin/python3
""" append """

def append_after(filename="", search_string="", new_string=""):
    """ appends after """
    with open(filename, mode='r', encoding='utf-8') as rd:
        lines = rd.readlines()

    with open(filename, mode='w', encoding='utf-8') as wt:
        for line in lines:
            wt.write(line)
            if search_string in line:
                wt.write(new_string)
