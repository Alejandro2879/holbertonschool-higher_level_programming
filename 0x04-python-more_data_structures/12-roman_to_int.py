#!/usr/bin/python3
def roman_to_int(roman_string):
        result = 0
        i = 0

        if type(roman_string) != str:
                return (0)
        if roman_string is None:
                return (0)

        while (i < len(roman_string)):
                s1 = value(roman_string[i])
                if (i + 1 < len(roman_string)):
                        s2 = value(roman_string[i + 1])
                        if (s1 >= s2):
                                result = result + s1
                                i = i + 1
                        else:
                                result = result + s2 - s1
                                i = i + 2
                else:
                        result = result + s1
                        i = i + 1
        return result


def value(num):
        if (num == 'I'):
                return (1)
        if (num == 'V'):
                return (5)
        if (num == 'X'):
                return (10)
        if (num == 'L'):
                return (50)
        if (num == 'C'):
                return (100)
        if (num == 'D'):
                return (500)
        if (num == 'M'):
                return (1000)
        return (-1)
