#!/usr/bin/python3
"""
[Module define a function that concatenate "My name is"
with 2 strings passed as arguments: first_name and last_name]
"""


def say_my_name(first_name, last_name=""):
        """[Function concatenate: "My name is" with first and
                second arguments passed to the function]

        Args:
            first_name (str): [First string passed to the function]
            last_name (str): [Second string passed]. Defaults to "".

        Raises:
            TypeError: [If first_name is not a string]
            TypeError: [If last_name is not a string]
        """

        if type(first_name) is not str:
                raise TypeError("first_name must be a string")
        elif type(last_name) is not str:
                raise TypeError("last_name must be a string")
        print("My name is {} {}".format(first_name, last_name))
