#!/usr/bin/python3
"""Deifne: Base Class"""

import json

class Base:
    """Representation of Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
    
 
    @staticmethod
    def save_to_file(cls, list_objs):
        """"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        else:
            for i, obj in enumerate(list_objs):
                list_objs[i] = cls.to_dictionary(obj) 
        
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                l = cls.from_json_string(f.read())
            for i in l:
                l[i] = cls.create(**l[i])
        except:
            pass
        return l
