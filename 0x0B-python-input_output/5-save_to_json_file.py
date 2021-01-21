#!/usr/bin/python3
"""[Module define the save_to_json_file function]
"""
import json


def save_to_json_file(my_obj, filename):
    """[Function writes an Object to a text file, using a JSON representation]

    Args:
        my_obj (Obj): [Python object]
        filename (File): [Text file]

    Returns:
        [Json]: [Json representation of my_obj]
    """
    with open(filename, 'w', encoding="utf-8") as my_file:
        return json.dump(my_obj, my_file)
