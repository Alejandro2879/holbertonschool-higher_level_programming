#!/usr/bin/python3
"""[Module define the Base class]
"""
import json


class Base():
        """[Base class compute an object from or to JSON]

        Returns:
            [Json]: [Json object]
        """

    __nb_objects = 0

    def __init__(self, id=None):
        """[Define __init__ method]
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[Method returns the JSON string representation of list_dictionaries]
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """[Method writes the JSON string representation of list_objs to a file]
        """
        new_str = []
        file_n = '{}.json'.format(cls.__name__)
        with open(file_n, 'w', encoding="utf-8") as file:
            if list_objs is not None:
                for obj in list_objs:
                    new_str.append(cls.to_dictionary(obj))
                new_str = Base.to_json_string(new_str)
                file.write(str(new_str))
            else:
                file.write(str(new_str))

    @staticmethod
    def from_json_string(json_string):
        """[Returns the list of the JSON string representation json_string]
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """[Returns an instance with all attributes already set:]
        """
        if cls.__name__ == 'Rectangle':
            temp = cls(1, 1)
        elif cls.__name__ == 'Square':
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """[Returns the list of the JSON string representation json_string]
        """
        new_l = []
        try:
            file_n = '{}.json'.format(cls.__name__)
            with open(file_n) as op_file:
                for obj in cls.from_json_string(op_file.read()):
                    new_l.append(cls.create(**obj))
                return new_l
        except Exception:
            return new_l
