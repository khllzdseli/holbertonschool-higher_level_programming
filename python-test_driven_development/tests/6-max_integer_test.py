#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    # --- Normal cases ---

    def test_max_at_end(self):
        """Max integer is at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Max integer is at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Max integer is in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """List with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_all_same(self):
        """All elements are the same."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    # --- Edge cases ---

    def test_empty_list(self):
        """Empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument defaults to empty list, returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """List with all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """List with both positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 5, -3]), 5)

    def test_zero(self):
        """List containing zero."""
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_large_numbers(self):
        """List with large integers."""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_floats(self):
        """List with float values."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_float(self):
        """List with mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.9, 2]), 2.9)

    def test_two_elements(self):
        """List with exactly two elements."""
        self.assertEqual(max_integer([3, 7]), 7)

    def test_sorted_ascending(self):
        """Already sorted ascending list."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_sorted_descending(self):
        """Already sorted descending list."""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)


if __name__ == '__main__':
    unittest.main()
