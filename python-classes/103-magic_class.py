#!/usr/bin/python3
"""Module that defines a MagicClass."""
import math


class MagicClass:
    """Class that stores a radius and calculates area and circumference."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (int or float): The radius of the magic circle.
        Raises:
            TypeError: If radius is not a number.
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Return the area of the circle."""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self._MagicClass__radius
