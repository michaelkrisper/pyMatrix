#! /usr/bin/env python3
# coding=utf-8
"""
Test for Matrix Class
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__date__ = "2014-11-14"

import unittest

import matrix


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.m0 = matrix.Matrix.zeroes(4, 4)
        self.m1 = matrix.Matrix.ones(4, 4)

    def test_mul(self):
        self.assertEqual(self.m0 * self.m1, self.m0)

    def test_add(self):
        self.assertEqual(self.m0 + self.m1, self.m1)

    def test_sub(self):
        self.assertEqual(self.m1 - self.m1, self.m0)

    def test_str(self):
        self.assertEqual(str(self.m1), "1\t1\t1\t1\n1\t1\t1\t1\n1\t1\t1\t1\n1\t1\t1\t1")


if __name__ == '__main__':
    unittest.main()
