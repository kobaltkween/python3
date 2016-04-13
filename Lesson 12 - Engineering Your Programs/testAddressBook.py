import unittest, shelve
import addressbook

class TestEmailHandlers(unittest.TestCase):
    
    def setUp(self):
        self.email = "test123@t.com"
        shelfLocation = addressbook.shelfLocation
        shelf = shelve.open(shelfLocation)
        if "emails" in shelf:
            if self.email in shelf["emails"]:
                shelf["emails"] = []
        shelf.close()
    
    def testEmailDelete(self):
        addressbook.emailAdd(self.email) # ensure the email is active
        self.assertEqual(addressbook.emailDelete(self.email)[0], True)
        self.assertEqual(addressbook.emailDelete(self.email)[0], False)
        
    def testEmailAdd(self):
        self.assertEqual(addressbook.emailAdd(self.email)[0], True)
        self.assertEqual(addressbook.emailAdd(self.email)[0], False)
        
    def testEmailDisplay(self):
        addressbook.emailAdd(self.email)
        val, display = addressbook.emailDisplay()
        self.assertTrue(self.email in display)
                        
        
if __name__ == "__main__":
    unittest.main()