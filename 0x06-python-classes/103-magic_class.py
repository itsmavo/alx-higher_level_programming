#!/usr/bin/python3
import math

"""magic class definition"""
class MagicClass:
     """magicclass that makes same bytecode as in the task"""
     
    def __init__(self, radius=0):
        """Initialize class"""
        self._MagicClass__radius = 0
        if (type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius

    def area(self):
             """area function calculates some weird stuff"""
        return self._MagicClass_radius ** 2 * math.pi

    def circumference(self):
            """also this func calculate some weird stuff"""
        return self._MagicClass_radius * 2 * math.pi

if __name__ == "__main__":
    import dis
    dis.dis(MagicClass)
        
