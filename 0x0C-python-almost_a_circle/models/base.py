#!/usr/bin/python3
"""Deifne: Base Class"""

import json
import csv
import turtle


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
        json_list = []
        if list_objs is not None:
            for i in list_objs:
                json_list.append(i.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

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
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_list = cls.from_json_string(file.read())
                obj_list = []
                for i in json_list:
                    obj_list.append(cls.create(**i))
                return obj_list
        except:
            return []

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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list of Rectangles)
            list_squares (list of squares)
        Returns:
            None
        """
        for i in list_rectangles:
            t = turtle.Turtle()
            t.speed(0.7)
            t.penup()
            t.setpos(i.x, i.y)
            t.pendown()
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
        for i in list_squares:
            t = turtle.Turtle()
            t.speed(0.7)
            t.penup()
            t.setpos(i.x, i.y)
            t.pendown()
            t.begin_fill()
            for _ in range(4):
                t.forward(i.size)
                t.left(90)
