#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Test that id auto-increments when not provided."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_provided(self):
        """Test that provided id is assigned correctly."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_provided_then_auto(self):
        """Test mix of provided and auto ids."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_id_zero(self):
        """Test that id=0 is assigned."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """Test that negative id is assigned."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_string(self):
        """Test that string id is assigned."""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a list of dicts."""
        d = [{"id": 1, "width": 10}]
        result = Base.to_json_string(d)
        self.assertEqual(type(result), str)
        self.assertEqual(json.loads(result), d)

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_list(self):
        """Test from_json_string with valid JSON string."""
        s = '[{"id": 1, "width": 10}]'
        result = Base.from_json_string(s)
        self.assertEqual(result, [{"id": 1, "width": 10}])
        self.assertEqual(type(result), list)

    def test_save_to_file_rectangle(self):
        """Test save_to_file with Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 2)
        os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        """Test save_to_file with empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        os.remove("Rectangle.json")

    def test_create_rectangle(self):
        """Test create for Rectangle."""
        r = Rectangle.create(**{'id': 1, 'width': 3, 'height': 5, 'x': 1})
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)

    def test_create_square(self):
        """Test create for Square."""
        s = Square.create(**{'id': 1, 'size': 5, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file does not exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_rectangle(self):
        """Test load_from_file with Rectangle."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].width, 10)
        os.remove("Rectangle.json")

    def test_load_from_file_square(self):
        """Test load_from_file with Square."""
        s1 = Square(5, 0, 0, 1)
        Square.save_to_file([s1])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].size, 5)
        os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
