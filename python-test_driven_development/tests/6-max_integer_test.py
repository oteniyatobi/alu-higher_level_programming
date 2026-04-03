#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_regular_list(self):
        """Test with a normal list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_start(self):
        """Test when the max is at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test when the max is in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a single-element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_negative_positive(self):
        """Test with both negative and positive numbers."""
        self.assertEqual(max_integer([-5, 0, 5, 3]), 5)

    def test_duplicate_values(self):
        """Test with duplicate values including the max."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_all_same(self):
        """Test with all identical values."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_two_elements(self):
        """Test with exactly two elements."""
        self.assertEqual(max_integer([1, 100]), 100)

    def test_no_argument(self):
        """Test calling with no argument returns None."""
        self.assertIsNone(max_integer())

    def test_floats(self):
        """Test with float values."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_max_at_end(self):
        """Test when the max is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 4, 100]), 100)


if __name__ == '__main__':
    unittest.main()
