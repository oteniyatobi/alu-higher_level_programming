#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size (width and height) of the square.
            x (int): The x position offset.
            y (int): The y position offset.
            id (int): The id to assign.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size (width and height) of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update square attributes using positional or keyword args.

        Args:
            *args: id, size, x, y in order.
            **kwargs: Key/value pairs of attributes to update.
        """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i, val in enumerate(args):
                if i < len(attrs):
                    if attrs[i] == 'id':
                        self.id = val
                    else:
                        setattr(self, attrs[i], val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Return dictionary representation of the square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
