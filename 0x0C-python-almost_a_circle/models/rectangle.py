#!/usr/bin/python3
"""
Module with class Rectangle, inheriting from class Base
"""

from models.base import Base

class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init function """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get y """
        return self.__y
    
    @y.setter
    def y(self, value):
        """ set y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """ returns area of rectangle object """
        return self.width * self.height

    def display(self):
        """ displays a rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str special method """
        strrectangle = "[Rectangle] "
        strid = "({}) ".format(self.id)
        strxy = "{}/{} - ".format(self.x, self.y)
        strwh = "{}/{}".format(self.width, self.height)

        return strrectangle + strid + strxy + strwh

    def display(self):
        """ prints rectangle in hash form """
        print('\n' * self.y, end="")
        print(''.join(' ' * self.x + '#' * self.width + '\n'
                      for times in range(self.height)), end="")

    def update(self, *args, **kwargs):
        """ update method """
        if args != None and len(args) != 0:
            atr_l = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, atr_l[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returns a dictionary """
        list_a = ['id', 'width', 'height', 'x', 'y']
        dict_r = {}

        for key in list_a:
            dict_r[key] = getattr(self, key)

        return dict_r
