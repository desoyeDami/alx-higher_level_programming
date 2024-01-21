#!/usr/bin/python3
"""
Module: 1-square
Defines a class Square with a private instance attribute.
"""


class Square:
    """
    The Square class represents a geometric square.

    Attributes:
        __size (int): Private instance attribute
        representing the size of the square.

    Methods:
        None
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Note:
            The size attribute is private
            and can only be accessed within the class.
        """
        self.__size = size
