#!/usr/bin/python3
"""[Module define the load_from_json_file function]
"""
import json


def load_from_json_file(filename):
    """[Function create an object from a json file]

    Args:
        filename (file): [Json file]

    Returns:
        [Obj]: [Python representation of the json file]
    """
    with open(filename, 'r', encoding="utf-8") as json_file:
        return json.load(json_file)
