"""
testExtend.py: verify that Ford successfully extends
                the Car.__init__() method
"""

import unittest
from extend import Car, Ford, Toyota

class TestCars(unittest.TestCase):
    
    def testToyota(self):
        car1 = Car("red", 2000)
        car2 = Toyota("red", 2000, "Corolla")
        self.assertEqual(car1.color, car2.color)
        self.assertEqual(car1.cc, car2.cc)
        self.assertEqual(car2.model, "Corolla")
        
    def testFord(self):
        car1 = Car("red", 2000)
        car2 = Ford("red", 2000, "Taurus")
        self.assertEqual(car1.color, car2.color)
        self.assertEqual(car1.cc, car2.cc)
        self.assertEqual(car2.model, "Taurus")
        
if __name__ == "__main__":
    unittest.main()