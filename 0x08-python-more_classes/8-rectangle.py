#!/usr/bin/python3

""" class rectangle """

class Rectangle:
    """ makes the rectangle object """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initialises rectangle obj """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ gets height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns area """
        return self.height * self.width

    def perimeter(self):
        """ returns perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return(self.width * 2) + (self.height * 2)

    def bigger_or_equal(rect_1, rect_2):
        """ returns bigger area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """ modifies str object """
        if not self.perimeter:
            return ""
        return('\n'.join("{}".format(self.print_symbol) * self.width
                         for i in range(self.height)))

    def __repr__(self):
        """ modifies repr object """
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """ modifies del object """
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))

