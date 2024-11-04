#!/usr/bin/env python3
"""Test Utility"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map
from typing import (Mapping, Sequence, Any)


class TestAccessNestedMap(unittest.TestCase):
    """A test class for a function that
    access a nester map"""

    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
        ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected: Any
            ):
        """Test case for a function that accesses nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
        ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence):
        """Test that an exception is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Class for unit testing the function utils.get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Mock test for the function"""
        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Class for unit testing the function utils.memoize"""

    def test_memoize(self):
        """Mock test for the function"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            mock_method.return_value = 42
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            mock_method.assert_called_once()
            self.assertEqual(result1, mock_method.return_value)
            self.assertEqual(result2, mock_method.return_value)


if __name__ == "__main__":
    unittest.main()
