#!/usr/bin/python3
"""Module that defines a Square class with size and position."""


class Square:
    """Defines a square with size, position, and print functionality."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: The current position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position with validation.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using # with position offsets applied."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):  # vertical offset
            print("")

        for _ in range(self.__size):          # each row
            print(" " * self.__position[0] + "#" * self.__size)
