#!/usr/bin/env python3

import unittest
from typing import Mapping, Sequence

from parameterized import parameterized
from utils import access_nested_map

"""
Test utils.py
"""


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests access_nested_map function
    Is of type of unittest.TestCase
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: int) -> None:
        """Tests access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence) -> None:
        """Test access_nested_map function if raises a key error
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(e.exception.args[0], path[-1])
