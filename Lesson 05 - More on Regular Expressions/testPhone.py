import unittest
from phone import getPhone, text

class TestRegex(unittest.TestCase):
    
    def testPhone(self):
        numbers = getPhone(text)
        self.assertEqual(len(numbers), 5)
    
if __name__ == "__main__":
    unittest.main()