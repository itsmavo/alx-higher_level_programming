#!/usr/bin/python3
""" reads file """

def read_file(filename=""):
    """ read file """
    with open(filename, mode='r', encoding='utf-8') as rd:
        for line in rd:
            print(line, end="")
