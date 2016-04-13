'''
Created on Jan 3, 2016

@author: mboyd
'''
import unittest
from coconuts import Coconut, Inventory


class TestCoconuts(unittest.TestCase):

    def setUp(self):
        """
        Create an inventory and coconuts to add to the inventory.
        """
        self.inv = Inventory()
        self.coco1 = Coconut("South Asian")
        self.coco2 = Coconut("American")
        self.coco3 = Coconut("Middle Eastern")
    
    def testCoconuts(self):
        """
        Make sure each type of coconut has the right weight property
        """
        self.assertEqual(self.coco1.weight, 3, "South Asian coconuts should weigh 3")
        self.assertEqual(self.coco2.weight, 3.5, "American coconuts should weigh 3.5")
        self.assertEqual(self.coco3.weight, 2.5, "Middle Eastern coconuts should weigh 2.5")
        self.assertRaises(AttributeError, Coconut, "Pacific Island")
        
    def testAddCoconut(self):
        """
        Make sure that the addCoconut method of the Inventory class raises an exception when trying to add something other than coconuts.
        """
        self.assertRaises(AttributeError, self.inv.addCoconut, "foobar")
        
    def testTotalWeight(self):
        """
        Verify that the addCoconut method adds coconuts to the inventory properly and that Inventory's totalWeight method adds properly.
        """
        self.inv.addCoconut(self.coco1, 2)
        self.inv.addCoconut(self.coco3)
        self.inv.addCoconut(self.coco2, 3)
        self.assertEqual(self.inv.totalWeight(), 19, "The total weight of the inventoray should now by 19.")
        
if __name__ == "__main__":
    unittest.main()