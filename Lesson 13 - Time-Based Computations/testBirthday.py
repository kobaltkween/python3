from datetime import datetime
import unittest

from birthday import *

class TestBirthday(unittest.TestCase):
    
    def testBirthdayCounter(self):
        # will fail on October 31
        self.assertTrue(birthdayCounter("10-31-1948") > 0)
        # will fail on February 1
        self.assertTrue(birthdayCounter("02-01-1999") > 0)
        
    def testStringToDate(self):
        self.assertRaises(InvalidDateFormat, stringToDate, "10-32-1948")
        # create a new datetime object from scratch
        datetimeObj = datetime(2012, 10, 31)
        self.assertEqual(datetimeObj, stringToDate("10-31-2012"))
        
if __name__ == "__main__":
    unittest.main()