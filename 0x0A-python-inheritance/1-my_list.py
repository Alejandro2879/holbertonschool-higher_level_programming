#!/usr/bin/python3
"""[Module define MyList function]
"""


class MyList(list):
    """[Function inherite from list to print a sorted list]

    Args:
        list (object): [Built-in object]
    """
    def print_sorted(self):
        print(sorted(self))
