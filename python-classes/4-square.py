#!/usr/bin/python3
"""Module that defines a Square class with property getter and setter."""


class Square:
    """Defines a square with a controlled size attribute via properties."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size  # uses the setter — validation happens here!

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size * self.__size
