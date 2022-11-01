#!/usr/bin/python3
import unittest
import os.path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
""" tests Base """

class TestBase(unittest.TestCase):

    def test_id(self):
        """ tests id """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(10)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 10)
        self.assertEqual(b5.id, 4)

    def test_dictionary(self):
        """ tests the dictionary """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertDictEqual(dictionary,
                             {'x': 2, 'width': 10,
                              'id': 1, 'height': 7, 'y': 8})
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(json_dict, json_dict)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_saveFile(self):
        """ tests the savefile"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Square(4)
        Rectangle.save_to_file([r1])
        Square.save_to_file([r2])
        with open("Rectangle.json", 'r') as rd:
            self.assertTrue(len(rd.read()) > 1)
        with open("Square.json", 'r') as rd:
            self.assertTrue(len(rd.read()) > 1)

        Rectangle.save_to_file(None)
        Square.save_to_file(None)
        with open("Rectangle.json", 'r') as rd:
            self.assertTrue(rd.read() == "[]")
        with open("Square.json", 'r') as rd:
            self.assertTrue(rd.read() == "[]")


    def test_fromJson(self):
        """ tests the from json """
        r_input = [{'id': 89, 'width': 10, 'height': 4}]
        s_input = [{'id': 89, 'size': 4}]
        json_list_input = Rectangle.to_json_string(r_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_output) is list)
        list_output = Rectangle.from_json_string([])
        self.assertTrue(list_output == [])
        list_output = Rectangle.from_json_string(None)
        self.assertTrue(list_output == [])

        json_list_input = Square.to_json_string(s_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertTrue(type(list_output) is list)
        list_output = Square.from_json_string([])
        self.assertTrue(list_output == [])
        list_output = Square.from_json_string(None)
        self.assertTrue(list_output == [])

    def test_load(self):
        """ tests load """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rec_inp = [r1, r2]
        Rectangle.save_to_file(list_rec_inp)
        list_rec_out = Rectangle.load_from_file()
        for i in list_rec_out:
            self.assertTrue(type(i) is Rectangle)

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_sq_inp = [s1, s2]
        Square.save_to_file(list_sq_inp)
        list_sq_out = Square.load_from_file()
        for i in list_sq_out:
            self.assertTrue(type(i) is Square)


    if __name__ == '__main__':
        unittest.main()
