#!/usr/bin/python3
"""Deifne: Base Class"""

import json
import csv


class Base:
    """Representation of Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization a Base

        Args:
            id (int): base id

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries ( list of dicts): list of dict respersantaion

        Returns:
            (str): Json represantation
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string ( list of dicts): list of dict respersantaion

        Returns:
            (list): Json represantation
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list)

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        else:
            for i, obj in enumerate(list_objs):
                list_objs[i] = cls.to_dictionary(obj)

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:

        Args:
            None
        Returns:
            (list): of instances
        """
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                l = cls.from_json_string(f.read())
            for i, e in enumerate(l):
                l[i] = cls.create(**l[i])
        except:
            pass
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of Rectangles/Squares in csv

        Args:
            list
        Returns:
            (list) of Rectangles/Squares in csv
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for r in list_objs:
                    csv_writer.writerow([r.id, r.width, r.height,
                                         r.x, r.y])
            elif cls.__name__ is "Square":
                for s in list_objs:
                    csv_writer.writerow([s.id, s.size, s.x, s.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv
        Args:
            None
        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        obj_list = []
        try:
            with open(filename, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        obj = cls.create(**{"id": int(args[0]),
                                            "width": int(args[1]),
                                            "height": int(args[2]),
                                            "x": int(args[3]),
                                            "y": int(args[4])})
                    elif cls.__name__ is "Square":
                        obj = cls.create(**{"id": int(args[0]),
                                            "size": int(args[1]),
                                            "x": int(args[2]),
                                            "y": int(args[3])})

                    obj_list.append(obj)
        except Exception:
            return obj_list
        return obj_list
