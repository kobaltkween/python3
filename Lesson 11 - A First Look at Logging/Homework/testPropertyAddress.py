import unittest
from propertyAddress import *

class TestAddresses(unittest.TestCase):
    
    def setUp(self):
        self.home = Address( name = 'Steve Holden', streetAddress = '1972 Flying Circus', city = "Arlington", state = "VA", zipCode = "12345")
    
    def testName(self):
        self.assertEqual(self.home.name, 'Steve Holden')
        self.assertRaises(AttributeError, setattr, self.home, "name", "Daniel Greenfeld")
        
    def testState(self):
        self.assertEqual(self.home.state, "VA")
        self.assertRaises(StateError, setattr, self.home, "state", "Not a state")
        self.home.state = "CO"
        self.assertEqual(self.home.state, "CO")
        setLogLevel('info')
        
    def testZipCode(self):
        self.assertEqual(self.home.zipCode, "12345")
        self.assertRaises(ZipCodeError, setattr, self.home, "zipCode", "123456")
        self.home.zipCode = "54321"
        self.assertEqual(self.home.zipCode, "54321")
    
if __name__ == "__main__":
    startLogging(level = "error")
    unittest.main()
    