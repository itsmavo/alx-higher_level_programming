#!/usr/bin/python3
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO
""" tests square """

class TestSquare(unittest.TestCase):

    def test_docstrings(self):
        """ tests docstrings """
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Square.__doc__) > 0)
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)
        for func in dir(Square):
            self.assertTrue(len(func.__doc__) > 0)

    def test_ids(self):
        """ test ids """
        Base._Base__nb_objects = 0
        s1 = Square(10)
        s2 = Square(2)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 12)
        s3.id = "b"
        self.assertEqual(s3.id, "b")

    def test_attr_errors(self):
        """ test errors """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError, msg="size must be an integer"):
            s1 = Square("2")
        with self.assertRaises(ValueError, msg="size must be > 0"):
            s1 = Square(-2)
        with self.assertRaises(TypeError, msg="size must be an integer"):
            s1 = Square({1: 2})
        with self.assertRaises(ValueError, msg="size must be > 0"):
            s2 = Square(10)
            s2.size = -10
        with self.assertRaises(TypeError, msg="x must be an integer"):
            s3 = Square(10, 2)
            s3.x = {}
        with self.assertRaises(ValueError, msg="y must be > 0"):
            s4 = Square(10, 2, -1)

    def test_areas(self):
        """ test areas """
        Base._Base__nb_objects = 0
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

        s1 = Square(2)
        self.assertEqual(s1.area(), 4)

        s1 = Square(8, 0, 0, 12)
        self.assertEqual(s1.area(), 64)

    def test_display(self):
        """ test display """
        Base._Base__nb_objects = 0
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        s1 = Square(2)
        s1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "##\n##\n")
        sys.stdout = mystdout = StringIO()
        s1 = Square(2, 2, 2)
        s1.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n")
        sys.stdout = old_stdout

    def test_str(self):
        """ tests strings """
        Base._Base__nb_objects = 0
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Rectangle] (12) 2/1 - 4/4")
        s2 = Square(5, 1)
        self.assertEqual(s2.__str__(), "[Rectangle] (1) 1/0 - 5/5")
        s1 = Square(1)
        self.assertEqual(s1.__str__(), "[Rectangle] (2) 0/0 - 1/1")

    def test_update(self):
        """ tests update """
        Base._Base__nb_objects = 0
        s1 = Square(10, 10, 10, 10)
        s1_dict = s1.to_dictionary()
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        s1.update(89, 2)
        self.assertEqual(s1.__str__(), "[Rectangle] (89) 10/10 - 2/2")
        s1.update(89, 2, 3)
        self.assertEqual(s1.__str__(), "[Rectangle] (89) 3/10 - 2/2")
        s1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(s1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        with self.assertRaises(ValueError, msg="x must be >=0"):
            s1.update(y=1, width=2, x=-3, id=89)
        s2 = Square(2, 2)
        s2.update(**s1_dict)
        self.assertEqual(s2.__str__(), "[Rectangle] (10) 10/10 - 10/10")

    def test_dictionary(self):
        """ test dictionary """
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1, 9)
        s1_dict = s1.to_dictionary()
        self.assertDictEqual(s1_dict, {
            'x': 2, 'y': 1, 'size': 10, 'id': 9})
        s1 = Square(1)
        s1_dict = s1.to_dictionary()
        self.assertDictEqual(s1_dict, {
            'x': 0, 'y': 0, 'size': 1, 'id': 1})

    def test_SquareCreate(self):
        """ tests create """
        Base._Base__nb_objects = 0
        s1 = Square(10)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

if __name__ == '__main__':
    unittest.main()
        
