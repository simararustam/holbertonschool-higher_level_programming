#!/usr/bin/python3

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    #Positive
    def positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    #Negative
    def negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    #mix element
    def mix(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
    
    #empty
    def empty(self):
        self.assertIsNone(max_integer([]))
    
    #only one elment
    def one_elm(self):
        self.asserEqual(max_integer([1]), 1)

if __name__ == "__main__":
    unittest.main()
