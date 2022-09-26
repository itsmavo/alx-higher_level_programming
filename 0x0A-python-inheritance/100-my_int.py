#!/usr/bin/python3
""" MyInt class """

class MyInt(int):
    """ instance of MyInt """

    def __init__(self, value):
        """ inits class """
        self.value = value

    def __eq__(self, b):
        """ rev equals to not equals """
        return self.value != b
    def __ne__(self, b):
        """ rev not equals to equals """
        return self.value == b
