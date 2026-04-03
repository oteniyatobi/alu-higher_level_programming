#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Test that Square is an instance of Rectangle and Base."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_id_auto(self):
        """Test auto id assignment."""
        s1 = Square(5)
        s2 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_id_provided(self):
        """Test provided id."""
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.id, 12)

    def test_size_getter(self):
        """Test size getter returns width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_x_default(self):
        """Test x defaults to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)

    def test_y_default(self):
        """Test y defaults to 0."""
        s = Square(5)
        self.assertEqual(s.y, 0)

    def test_size_not_int(self):
        """Test TypeError when size is not an integer."""
        with self.assertRaises(TypeError) as ctx:
            Square("5")
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_size_zero(self):
        """Test ValueError when size is 0."""
        with self.assertRaises(ValueError) as ctx:
            Square(0)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_size_negative(self):
        """Test ValueError when size is negative."""
        with self.assertRaises(ValueError) as ctx:
            Square(-1)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_x_not_int(self):
        """Test TypeError when x is not an integer."""
        with self.assertRaises(TypeError) as ctx:
            Square(5, "x")
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_y_not_int(self):
        """Test TypeError when y is not an integer."""
        with self.assertRaises(TypeError) as ctx:
            Square(5, 0, "y")
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_x_negative(self):
        """Test ValueError when x is negative."""
        with self.assertRaises(ValueError) as ctx:
            Square(5, -1)
        self.assertEqual(str(ctx.exception), "x must be >= 0")

    def test_y_negative(self):
        """Test ValueError when y is negative."""
        with self.assertRaises(ValueError) as ctx:
            Square(5, 0, -1)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_area(self):
        """Test area method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_area_after_resize(self):
        """Test area after size change."""
        s = Square(5)
        s.size = 3
        self.assertEqual(s.area(), 9)

    def test_display(self):
        """Test display method."""
        s = Square(2)
        expected = "##\n##\n"
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected)

    def test_display_with_offset(self):
        """Test display with x/y offset."""
        s = Square(2, 2, 1)
        expected = "\n  ##\n  ##\n"
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected)

    def test_str(self):
        """Test __str__ method."""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_str_default(self):
        """Test __str__ with default values."""
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_update_args_id(self):
        """Test update with id arg."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_args_all(self):
        """Test update with all positional args."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update with keyword args."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(s.x, 12)

    def test_update_kwargs_multiple(self):
        """Test update with multiple keyword args."""
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

    def test_update_kwargs_id(self):
        """Test update with id in kwargs."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.y, 1)

    def test_update_args_over_kwargs(self):
        """Test that args take precedence over kwargs."""
        s = Square(5)
        s.update(10, 2, size=99)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d['id'], 1)
        self.assertEqual(d['size'], 10)
        self.assertEqual(d['x'], 2)
        self.assertEqual(d['y'], 1)
        self.assertEqual(type(d), dict)

    def test_to_dictionary_keys(self):
        """Test to_dictionary has correct keys."""
        s = Square(1)
        d = s.to_dictionary()
        self.assertIn('id', d)
        self.assertIn('size', d)
        self.assertIn('x', d)
        self.assertIn('y', d)
        self.assertNotIn('width', d)
        self.assertNotIn('height', d)

    def test_size_float(self):
        """Test TypeError when size is a float."""
        with self.assertRaises(TypeError):
            Square(1.5)

    def test_size_none(self):
        """Test TypeError when size is None."""
        with self.assertRaises(TypeError):
            Square(None)


if __name__ == '__main__':
    unittest.main()
