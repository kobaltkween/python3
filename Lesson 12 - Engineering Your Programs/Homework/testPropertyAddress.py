import unittest
from propertyAddress import *

"""
NOTES: This generates the specified errors, but not in the order specified.
With the new address being created in the setUp before each test, I don't 
see how the first announcement of creating a new address could come after 
two errors that can only be generated by testing.  Also, I don't see how 
the three different tests could generate three new address announcements 
without having them interspersed between errors.  Even if I decided to get 
rid of the setUp method and generate new addresses in exact places, I don't 
see how to get it to raise the exceptions _and_ have anything to work with 
before creating a new address.

I think I could generate the necessary order of errors if I
    1. Got rid of the setUp method or set the logging to error.
    2. Checked that breaking the new state rule generated an error.
    3. Checked that breaking the new zipcode rule generated an error.
    4. Let it create a new address that worked or set logging to info.
    5. Tested changing the name as above.
    6. Created another address that works.
    7. Created a third address that works.

But that would so drastically change the testing, and possibly make the tests messier.
So I thought I'd leave it this way and make it clear I wasn't simply ignoring
instructions.  I'm ready to change it if that's the correct answer, but I thought I'd
best leave it like this, and make sure I wasn't just making it all more complicated and 
messy than I should.
"""

class TestAddresses(unittest.TestCase):
    
    def setUp(self):
        self.home = Address( name = 'Steve Holden', streetAddress = '1972 Flying Circus', city = "Arlington", state = "VAT", zipCode = "12345-6789")
    
    def testName(self):
        self.assertEqual(self.home.name, 'Steve Holden')
        self.assertRaises(AttributeError, setattr, self.home, "name", "Daniel Greenfeld")
        
    def testState(self):
        self.assertEqual(self.home.state, "VAT")
        self.assertRaises(StateError, setattr, self.home, "state", "Not a state")
        self.home.state = "COM"
        self.assertEqual(self.home.state, "COM")
        #setLogLevel('info')
        
    def testZipCode(self):
        self.assertEqual(self.home.zipCode, "12345-6789")
        self.assertRaises(ZipCodeError, setattr, self.home, "zipCode", "12345")
        self.home.zipCode = "54321-9876"
        self.assertEqual(self.home.zipCode, "54321-9876")
    
if __name__ == "__main__":
    startLogging(level = "info")
    unittest.main()

