"""
Inheritance test program
"""

import unittest
from inhairitance import Child

class TestHair(unittest.TestCase):
    
    def testHair(self):
        child = Child()
        hair =  child.hair()
        self.assertNotEqual(hair, "red")
        self.assertNotEqual(hair, "brown")
        self.assertNotEqual(hair, "grey")
        self.assertEqual(hair, "bald")
        
if __name__ == "__main__":
    unittest.main()