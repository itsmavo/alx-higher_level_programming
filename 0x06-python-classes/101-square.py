#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if(type(value) is not tuple or len(value) is not 2
           or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        if(type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return(self.__size**2)

    def my_print(self):
        if(self.position[1]):
            print('' * self.position[1])
        for x in range(self.size):
            if(self.position[0]):
                print(" " * self.position[0], end='')
            print("#" * self.size, end='')
            print()

    def __str__(self):
        if(self.size == 0):
            return ''
        newline = '\n' * self.position[1]
        space = ' ' * self.position[0]
        hashes = "#" * self.size
        return newline + '\n'.join(space + hashes for i in range(self.size))
    
