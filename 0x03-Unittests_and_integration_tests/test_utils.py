#!/usr/bin/env python3
"""Test Utility"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A test class for a function that
    access a nester map"""

    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test case for a function that accesses nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)