#!/usr/bin/python3
"""[Module define write_file function]
"""


def write_file(filename="", text=""):
    """[Function writes a string to a text file]

    Args:
        filename (text): [Name of the file]. Defaults to "".
        text (str): [Text to write in the file]. Defaults to "".

    Returns:
        [int]: [Numbers of characters writed in the file]
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
