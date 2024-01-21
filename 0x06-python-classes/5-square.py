#!/usr/bin/python3
""" define a square class"""


class Square:
    """
        Represents a square.

        Attributes:
            __size (int): Private instance attribute
            representing the size of the square.

        Methods:
            __init__(self, size=0): Initializes a
            new instance of the Square class.
                Args:
                    size (int, optional):
                    The size of the square. Defaults to 0.
                Raises:
                    TypeError: If size is not an integer.
                    ValueError: If size is less than 0.
            area(self): Computes and returns the area of the square.

        Properties:
            size(self): Getter method to retrieve the size.
            size(self, value): Setter method to set the size.
                Raises:
                    TypeError: If value is not an integer.
                    ValueError: If value is less than 0.
        """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
                Setter method for the size attribute.

                Args:
                    value (int): The new size value.

                Raises:
                    TypeError: If value is not an integer.
                    ValueError: If value is less than 0.
                """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.
        """
        x = self.__size
        if x == 0:
            print("")
        else:
            for row in range(0, x):
                for col in range(0, x):
                    print("#", end="")
                print()
