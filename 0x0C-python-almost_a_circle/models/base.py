#!/usr/bin/python3
""" class base """
import json
import os.path

class Base:
    """ Inside class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json string """
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves to file """
        try:
            jsf = cls.to_json_string([x.to_dictionary() for x in list_objs])
        except:
            jsf = '[]'
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as wr:
            wr.write(jsf)

    @staticmethod
    def from_json_string(json_string):
        """ returns list of jsons """
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance of all attributes already set """
        if cls.__name__ == 'Square':
            newcreate = cls(1)
        if cls.__name__ == 'Rectangle':
            newcreate = cls(1, 1)
        if newcreate:
            newcreate.update(**dictionary)
            return newcreate

    @classmethod
    def load_from_file(cls):
        if not os.path.isfile(cls.__name__ + '.json'):
            return []
        else:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as wr:
                list_dict = cls.from_json_string(wr.read())
            return [cls.create(**dic) for dic in list_dict]


    @classmethod
    def save_to_file_csv(cls, list_objs):
        import csv
        try:
            csv_f = [i.to_dictionary() for i in list_objs]
        except:
            csv_f = '[]'
        kys = csv_f[0].keys()
        with open(cls.__name__ + '.csv', 'w') as wr:
            writer = csv.DictWriter(wr, kys)
            writer.writeheader()
            writer.writerows(csv_f)

    @classmethod
    def load_from_file_csv(cls):
        import csv
        if not os.path.isfile(cls.__name__ + '.csv'):
            return []
        else:
            with open(cls.__name__ + '.csv', 'r') as rd:
                reader = csv.DictReader(rd)
                csv_f = [row for row in reader]
                for row in csv_f:
                    for key, val in row.items():
                        try:
                            row[key] = int(val)
                        except:
                            pass
        return[cls.create(**dic) for dic in csv_f]
