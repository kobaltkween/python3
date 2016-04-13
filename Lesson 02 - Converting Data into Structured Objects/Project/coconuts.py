from copy import deepcopy

class Coconut():
    """
    Class makes coconut objects
    """
    typeDict = {
                    "South Asian" : 3,
                    "Middle Eastern" : 2.5,
                    "American" : 3.5
                }
    
    def __init__(self, aType):
        """
        Create a coconut object with a type (string) and a weight (int or float)
        """
        if aType in self.typeDict.keys():
            self.type = aType
            self.weight = self.typeDict[aType]
        else:
            raise AttributeError("{0} is not a known type of coconut.".format(aType))
 
class Inventory():
    """
    Inventory class to keep track of what is in a collection of coconut objects
    """
    def __init__(self):
        self.inv = []
    
    def addCoconut(self, coco, amt = 1):
        """
        Adds one or more coconuts to the inventory's list.
            The object passed must be of type "Coconut".
            If an amount higher than 1 is provided, then copies of the coconut will make up the rest.
            The coconuts are copied so that they aren't all pointing to the same object, and can have independent properties.
        """
        if type(coco) == Coconut:
            for i in range(amt):
                if i == 0:
                    self.inv.append(coco)
                else:
                    newCoco = deepcopy(coco)
                    self.inv.append(newCoco)
        else:
            raise AttributeError("A {0} is not a coconut".format(type(coco)))
        
    def totalWeight(self):
        """
        Return the weight of all the coconuts.
        """
        totalWeight = 0
        for c in self.inv:
            totalWeight += c.weight
        return totalWeight