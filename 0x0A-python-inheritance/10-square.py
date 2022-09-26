#!/usr/bin/python3
""" basegeometry class """

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ creates square """
    def __init__(self, size):
        """ inits rectangle """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
