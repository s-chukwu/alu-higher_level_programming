#!/usr/bin/python3
"""Module that defines a Square class with comparison capabilities."""


class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int or float): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int or float): The new size of the square.
        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if areas are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if areas are not equal."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if self area is less than other area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if self area is less than or equal to other area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if self area is greater than other area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if self area is greater than or equal to other area."""
        return self.area() >= other.area()
