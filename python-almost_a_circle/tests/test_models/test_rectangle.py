#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Test that Rectangle is an instance of Base."""
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)

    def test_id_auto(self):
        """Test auto id assignment."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_id_provided(self):
        """Test provided id."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width_getter(self):
        """Test width getter."""
        r = Rectangle(5, 3)
        self.assertEqual(r.width, 5)

    def test_height_getter(self):
        """Test height getter."""
        r = Rectangle(5, 3)
        self.assertEqual(r.height, 3)

    def test_x_getter(self):
        """Test x getter."""
        r = Rectangle(5, 3, 2)
        self.assertEqual(r.x, 2)

    def test_y_getter(self):
        """Test y getter."""
        r = Rectangle(5, 3, 2, 4)
        self.assertEqual(r.y, 4)

    def test_x_default(self):
        """Test x defaults to 0."""
        r = Rectangle(5, 3)
        self.assertEqual(r.x, 0)

    def test_y_default(self):
        """Test y defaults to 0."""
        r = Rectangle(5, 3)
        self.assertEqual(r.y, 0)

    def test_width_setter(self):
        """Test width setter."""
        r = Rectangle(5, 3)
        r.width = 10
        self.assertEqual(r.width, 10)

    def test_height_setter(self):
        """Test height setter."""
        r = Rectangle(5, 3)
        r.height = 10
        self.assertEqual(r.height, 10)

    def test_x_setter(self):
        """Test x setter."""
        r = Rectangle(5, 3)
        r.x = 4
        self.assertEqual(r.x, 4)

    def test_y_setter(self):
        """Test y setter."""
        r = Rectangle(5, 3)
        r.y = 4
        self.assertEqual(r.y, 4)

    def test_width_not_int(self):
        """Test TypeError when width is not an integer."""
        with self.assertRaises(TypeError) as ctx:
            Rectangle("10", 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_height_not_int(self):
        """Test TypeError when height is not an integer."""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, "2")
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_x_not_int(self):
        """Test TypeError when x is not an integer."""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, 2, {})
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_y_not_int(self):
        """Test TypeError when y is not an integer."""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, 2, 3, "y")
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_width_zero(self):
        """Test ValueError when width is 0."""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(0, 2)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_width_negative(self):
        """Test ValueError when width is negative."""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(-10, 2)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_height_zero(self):
        """Test ValueError when height is 0."""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(10, 0)
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_height_negative(self):
        """Test ValueError when height is negative."""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(10, -2)
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_x_negative(self):
        """Test ValueError when x is negative."""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(10, 2, -1)
        self.assertEqual(str(ctx.exception), "x must be >= 0")

    def test_y_negative(self):
        """Test ValueError when y is negative."""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_width_float(self):
        """Test TypeError when width is a float."""
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_width_none(self):
        """Test TypeError when width is None."""
        with self.assertRaises(TypeError):
            Rectangle(None, 2)

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        """Test area with large values."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_display_no_offset(self):
        """Test display without x/y offset."""
        r = Rectangle(4, 2)
        expected = "####\n####\n"
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected)

    def test_display_with_offset(self):
        """Test display with x/y offset."""
        r = Rectangle(2, 2, 1, 1)
        expected = "\n ##\n ##\n"
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected)

    def test_str(self):
        """Test __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default(self):
        """Test __str__ with default x/y."""
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """Test update with positional args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_args_partial(self):
        """Test update with partial positional args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)

    def test_update_kwargs(self):
        """Test update with keyword args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_kwargs_multiple(self):
        """Test update with multiple keyword args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)

    def test_update_args_over_kwargs(self):
        """Test that args take precedence over kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, height=5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(d['id'], 1)
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 2)
        self.assertEqual(d['x'], 1)
        self.assertEqual(d['y'], 9)
        self.assertEqual(type(d), dict)

    def test_to_dictionary_keys(self):
        """Test to_dictionary has correct keys."""
        r = Rectangle(1, 1)
        d = r.to_dictionary()
        self.assertIn('id', d)
        self.assertIn('width', d)
        self.assertIn('height', d)
        self.assertIn('x', d)
        self.assertIn('y', d)


if __name__ == '__main__':
    unittest.main()
