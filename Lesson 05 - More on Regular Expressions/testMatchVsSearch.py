import unittest
from matchVsSearch import checkNumber

p1 = """While I was at the store in Washington, DC 20001 I tried to call 555-123-4567 on my mobile
but accidentally called 555-754-4321.  The person on the line redirected me to 
999-999-9999 which I don't think is a real number. Neither is 000-000-0000 or 555-555-0000.
Well, I will try (555) 123-4567 again now."""

p1a = """While I was at the store in Washington, DC 20001 I tried to call (555) 123-4567 on my mobile
but accidentally called (555)-754-4321.  The person on the line redirected me to 
(999)-999-9999 which I don't think is a real number. Neither is (000)-000-0000 or (555) 555-0000.
Well, I will try (555) 123-4567 again now."""

p2 = "555-555-5555"
p2a = "(555)-555-5555"

p3 = "What is the author's phone number?"

class TestRegex(unittest.TestCase):
    
    def testMatch(self):
        self.assertEqual("555-555-5555", checkNumber(p2))
        self.assertEqual("(555)-555-5555", checkNumber(p2a))
        
    def testSearch(self):
        self.assertEqual(305, checkNumber(p1))
        self.assertEqual(315, checkNumber(p1a))
    
    def testNone(self):
        result = checkNumber(p3)
        self.assertIsNone(result)
        
if __name__ == "__main__":
    unittest.main()