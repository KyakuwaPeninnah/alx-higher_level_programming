#!/usr/bin/python3
"""Module base.
Defines a Base class for other classes."""


class Base:
    """Class with:
    Private class attribute: __nb_object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a Base instance."""

        if not isinstance(id, int) and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
