#!/usr/bin/python3

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def mix(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def empty(self):
        self.assertIsNone(max_integer([]))
    
    def one_elm(self):
        self.asserEqual(max_integer([1]), 1)

if __name__ == "__main__":
    unittest.main()

