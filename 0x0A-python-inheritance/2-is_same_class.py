#!/usr/bin/python3
"""[Module define the funtion is_same_class()]
"""


def is_same_class(obj, a_class):
    """[Function check if the object is exactly an instance of the specified class]

    Args:
        obj (int): [Object to check]
        a_class (not defined): [Class to compare with obj]

    Returns:
        [bool]: [True is obj is an instance of a_class, False if not]
    """
    if type(obj) is a_class:
        return True
    else:
        return False
