#!/usr/bin/python3
"""[Module define a function is_kind_of_class]
"""


def is_kind_of_class(obj, a_class):
    """[Function check if obj is an instance of a_class]

    Args:
        obj (int): [Object to compare with a_class]
        a_class (not defined): [Class to compare with obj]

    Returns:
        [bool]: [Pending]
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
