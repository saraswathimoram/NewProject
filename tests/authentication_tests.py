#!/usr/bin/env python
"""Unit tests for the project1.authentcation module."""


from unittest import TestCase
from mock import patch
import project1.authentication as app
import builtins



class Testcalc(TestCase):

    def setUp(self):
       self.x = 10
       self.y = 5
    
    def test_add(self):
        self.assertEqual(app.add(self.x, self.y), 15)
        self.assertEqual(app.add(2,3), 5)
        
    def test_sub(self):
        self.assertEqual(app.subtract(self.x, self.y), 5)
        self.assertEqual(app.subtract(2,3), -1)
        
    

if __name__ == '__main__':
    unittest.main()
