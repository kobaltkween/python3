'''
Created on Jan 3, 2016

@author: mboyd
'''
import unittest
from adder import adder


class Test(unittest.TestCase):


    def testAdderErrors(self):
        self.assertRaises(TypeError, adder, 1, "5")
        self.assertRaises(TypeError, adder, 1, [5])
        self.assertRaises(TypeError, adder, 1, (5, 0))
        self.assertRaises(TypeError, adder, 1, 5.5)
    
    def testAdderSuccess(self):
        self.assertEqual(adder(1, 5), 6, "Two positive integers should add.")
        self.assertEqual(adder(1, 0), 1, "Positive integer and zero should add.")
        self.assertEqual(adder(1, -5), -4,"A positive and a negative integer should add." )
        self.assertEqual(adder(-1, -5), -6, "Two negative integers should add.")
        self.assertEqual(adder(-1, 0), -1, "A negative integer and zero should add.")
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAdder']
    unittest.main()