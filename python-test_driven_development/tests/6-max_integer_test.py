#!/usr/bin/python3

import unittest

max_integer = __import__("6-max_integer").max_integer

class TestMaxinteger(unittest.TestCase):
    def positive(self):
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)

    def negative(self):
        self.assertEqual(max_integer([-1, -3, -5, -7]), -1)

    def mix(self):
        self.assertEqual(max_integer([-1, 5, 3, -7]), 5)

    def one_elm(self):
        self.assertEqual(max_integer([5]), 5)
    
    def empty(self):
        self.asserEqual(max_integer([]))

if __name__ == '__main__':
    unittest.main()
