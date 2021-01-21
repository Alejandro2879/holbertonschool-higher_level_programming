#!/usr/bin/python3
"""[Module define the append_write function]
"""


def append_write(filename="", text=""):
    """[Function append text to a file]

    Args:
        filename (file): [Name of the file]. Defaults to "".
        text (str): [Text to write in the file]. Defaults to "".

    Returns:
        [int]: [Number of characters copied]
    """
    with open(filename, 'a', encoding="utf-8") as my_file:
        return my_file.write(text)
