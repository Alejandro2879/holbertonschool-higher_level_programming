#!/usr/bin/python3
"""[Module define the read_file function]
"""


def read_file(filename=""):
    """[Function print text file]

    Args:
        filename (str): [Name of the file to print]. Defaults to "".
    """
    with open('my_file_0.txt', 'r', encoding="utf-8") as my_file:
        print(my_file.read(), end="")
