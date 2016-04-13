"""
Testing Furnishings, its subclasses, and the mapTheself.home function
"""

import unittest
from furnishings import *

class TestFurnish(unittest.TestCase):
    
    def setUp(self):
        """ Create home and fill it with furniture."""
        self.b1 = Bed('Bedroom')
        self.s1 = Sofa("Living Room")
        self.sh1 = Bookshelf('Bedroom')
        self.sh2 = Bookshelf("Living Room")
        self.t1 = Table("Living Room")
        self.t2 = Table('Dining Room')
        self.home = [self.b1, self.s1, self.sh1, self.sh2, self.t1, self.t2]
    
    def testMapTheHome(self):
        """Test the mapTheHome function"""
        m = mapTheHome(self.home)
        self.assertEqual([self.b1, self.sh1], m['Bedroom'])
        self.assertEqual([self.s1, self.sh2, self.t1], m['Living Room'])
        self.assertEqual([self.t2], m['Dining Room'])
        
    def testCounter(self):
        """Test the counter function"""
        count = counter(self.home, printOut = False)
        self.assertEqual(1, count['Bed'])
        self.assertEqual(1, count['Sofa'])
        self.assertEqual(2, count['Bookshelf'])
        self.assertEqual(2, count['Table'])


if __name__ == "__main__":
    unittest.main()