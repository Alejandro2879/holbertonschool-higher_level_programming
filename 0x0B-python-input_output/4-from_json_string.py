#!/usr/bin/python3
"""[Module defines the from_json_string function]
"""
import json


def from_json_string(my_str):
    """[Function returns an Python object represented by a JSON ]

    Args:
        my_str (obj): [Object]

    Returns:
        [Obj]: [Python object]
    """
    return json.loads(my_str)
