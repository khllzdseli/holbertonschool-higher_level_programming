#!/usr/bin/python3
"""Module that defines a Square class with an area method."""


class Square:
    """Defines a square with a validated private size and area computation."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
