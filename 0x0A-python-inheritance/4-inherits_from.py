#!/usr/bin/python3
"""[Module define a function inherits_from]
"""


def inherits_from(obj, a_class):
    """[Function check if obj is an instance of a_class]

    Args:
        obj (int): [Object to compare with a_class]
        a_class (not defined): [Class to compare with obj]

    Returns:
        [bool]: [Pending]
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
