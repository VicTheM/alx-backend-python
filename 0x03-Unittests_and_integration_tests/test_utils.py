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
