#!/usr/bin/python3
"""Module Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class rectangle inheriting attributes of the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor that initializes Rectangle instances"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
