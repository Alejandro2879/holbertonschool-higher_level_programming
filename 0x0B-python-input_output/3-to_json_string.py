#!/usr/bin/python3
"""[Module define to_json_string function]
"""
import json


def to_json_string(my_obj):
    """[Fuction returns the JSON representation of an object]

    Args:
        my_obj (obj): [object]

    Returns:
        [json]: [Json representation of obj]
    """
    return json.dumps(my_obj)
