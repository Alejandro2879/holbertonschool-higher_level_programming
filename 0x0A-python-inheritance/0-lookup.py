#!/usr/bin/python3
"""[Module define a lookup function that return all attributes of obj.]
"""


def lookup(obj):
    """[Function return all available attributes and methods of the superclass]

    Args:
        obj ([class]): [Parent class]
    """
    return(list(obj.__dict__))
