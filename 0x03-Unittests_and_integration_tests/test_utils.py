#!/usr/bin/env python3

import unittest
from typing import Callable, Dict, Mapping, Sequence
from unittest.mock import Mock, patch

from parameterized import parameterized
from utils import access_nested_map, get_json

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


class TestGetJson(unittest.TestCase):
    """
    Tests get_json function
    is of type unittest.TestCase
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: Dict[str, bool], mockGetFunc: Callable):
        """
        test if get_json method works correctly assuming request.get
        works as expected
        """
        test_json_mock = Mock()
        test_json_mock.json.return_value = test_payload
        mockGetFunc.return_value = test_json_mock
        main_val = get_json(test_url)
        mockGetFunc.assert_called_with(test_url)
        self.assertEqual(main_val, test_payload)
