#!/usr/bin/python3
""" square class """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ inherits from rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ inits """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ gets size """
        return self.width

    @size.setter
    def size(self, value):
        """ sets size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        if args != None and len(args) != 0:
            atr_l = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if atr_l[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height',args[i])
                else:
                    setattr(self, atr_l[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)


    def to_dictionary(self):
        """ Returns a dictionary """
        list_a = ['id', 'size', 'x', 'y']
        dict_r = {}

        for key in list_a:
            if key == 'size':
                dict_r[key] = getattr(self, 'width')
            else:
                dict_r[key] = getattr(self, key)

        return dict_r
