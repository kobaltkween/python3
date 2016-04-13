import unittest

from citySearch import citySearch

p1 = """While I was at the store I tried to call 555-123-4567 on my mobile
but accidentally called 555-754-4321.  The person on the line redirected me to 
999-999-9999 which I don't think is a real number. Neither is 000-000-0000 or 555-555-0000.
Well, I will try (555) 123-4567 again now."""

p2 = "I lieve in Washington, DC 20002.  Where do you live?"
p3 = "I live in Falls Church, VA 20188.  And you?"

class TestRegex(unittest.TestCase):
    
    def testCitySearch(self):
        self.assertEqual("Washington, DC 20002", citySearch(p2))
        self.assertEqual("Falls Church, VA 20188", citySearch(p3))
    
    def testCitySearchFailure(self):
        self.assertIsNone(citySearch(p1))
    
if __name__ == "__main__":
    unittest.main()