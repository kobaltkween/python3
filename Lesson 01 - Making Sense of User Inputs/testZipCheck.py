'''
Created on Jan 3, 2016

@author: mboyd

Test the zipErrors() function from teh ZipCheck module
'''
import unittest
from zipCheck  import zipErrors


class Test(unittest.TestCase):


    def testZipErrors(self):
        "Tests ensuring errors in data case validation failures."
        self.assertIsNotNone(zipErrors("1234"), "Accepting length 4")
        self.assertIsNotNone(zipErrors("12345-678"), "Accepting length 9")
        self.assertIsNotNone(zipErrors("1234e"), "Accepting alphabetic 5")
        self.assertIsNotNone(zipErrors("12345-678Y"), "Accepting alphabetic 5+4")
        self.assertIsNotNone(zipErrors("12345/6789"), "Accepting non-hyphen")
    
    def testZipSuccesses(self):
        "Test ensuring that valid data passes."
        self.assertIsNone(zipErrors("12345"), "Not accepting 5 digit zips")
        self.assertIsNone(zipErrors("12345-6789"), "Not accepting 9 digit zips")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testZipErrors']
    unittest.main()