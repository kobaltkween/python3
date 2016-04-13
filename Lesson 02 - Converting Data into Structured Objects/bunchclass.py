"""
Simple bunch class with a pretty printing method that protects its API.
"""
import unittest

class Bunch(object):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                raise AttributeError("API conflict: {0} is part of the {1} API".format(key, self.__class__.__name___))
            else:
                setattr(self, key, value)
        
    def pretty(self):
        text = ""
        for key, value in self.__dict__.items():
            text += "{0}: {1}\n".format(key, value)
        return text
        
class TestBunch(unittest.TestCase):
    def testAttributes(self):
        b = Bunch(name = "Python 3", language = "Python 3.0.1")
        self.assertEqual("Python 3", b.name)
        self.assertEqual("Python 3.0.1", b.language)
    
    def testPretty(self):
        self.assertRaises(AttributeError, Bunch, name = "Audrey", job = "Software Developer", pretty = True)
        b = Bunch(name = "Audrey", profession = "Software Developer")
        p = b.pretty()
        self.assertTrue("Audrey" in p)
        self.assertFalse("pretty: True" in p)
        
if __name__ == "__main__":
    unittest.main()