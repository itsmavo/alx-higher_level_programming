#!/usr/bin/python3

""" creates class Square """
class Square:
    """ Square class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if(type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of a Square """
        return(self.__size**2)

    def __lt__(self, other):
        """ Check if less than other square """
        return self.area() < other.area()
    
    def __eq__(self, other):
        """ Check if equal to another square """
        return self.area() == other.area()
    
    def __le__(self, other):
        """ Check if less than or equal to other square """
        return self.area() <= other.area()
    
    def __gt__(self, other):
        """ Check if greater than another square """
        return self.area() > other.area()
    
    def __ge__ (self, other):
        """ Check if greater than or equal to another square"""
        return self.area() >= other.area()
    
    def __ne__(self, other):
        """ Check if not equal to another square """
        return self.area() != other.area()
