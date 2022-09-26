#!/usr/bin/python3
""" basegeometry class """
class BaseGeometry:
    def area(self):
        """ raises exception """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ validates value for int and position """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

""" class Rectangle """
class Rectangle(BaseGeometry):
    """ creates rectangle class """
    def __init__(self, width, height):
        """ inits rectangle """
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height
