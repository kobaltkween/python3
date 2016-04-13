import unittest
from sentenceSplit import sentenceSplit

text = "Hello! My name is Steve. What is yours? I hope you enjoyed this class!"

class TestRegex(unittest.TestCase):
    
    def testSplitSentence(self):
        numbers = sentenceSplit(text)
        self.assertEqual(len(numbers), 4)
        
if __name__ == "__main__":
    unittest.main()