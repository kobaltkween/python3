import unittest
from ccnSafety import ccnReplace

text = ("Have you ever noticed, in television and movies, "
        "that phone numbers and credit cards are obviously "
        "fake numbers like 555-123-4567 or 5555-5555-5555-5555?"
        " It is because a number that appears to be real, such "
        "as 1234-5678-1234-5678, triggers the attention of "
        "privacy and security experts.")

class TestRegex(unittest.TestCase):
    
    def testReplace(self):
        "Make sure that the function does replace credit card numbers of the right form."
        self.assertTrue("CCN REMOVED FOR YOUR SAFETY" in ccnReplace(text))
        self.assertFalse("1234-5678-1234-5678" in ccnReplace(text))
        self.assertFalse("5555-5555-5555-5555" in ccnReplace(text))
        
    def testSkip(self):
        "Make sure the function doesn't replace other numbers, like phone numbers."
        self.assertTrue("555-123-4567" in ccnReplace(text))


if __name__ == "__main__":
    unittest.main()