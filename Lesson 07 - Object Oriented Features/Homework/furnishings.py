"""
Establish Furnishings class, and Sofa, 
Bookshelf, Bed, and Table classes.
"""

class Furnishings():
    
    def __init__(self, room):
        self.room = room
        
class Sofa(Furnishings):
    pass

class Bookshelf(Furnishings):
    pass

class Bed(Furnishings):
    pass

class Table(Furnishings):
    pass

def mapTheHome(homeList):
    """
    Takes in a list of Furnishing sub-class objects as a list.
    Returns a dictionary of rooms and lists of objects in the room.
    """
    homeMap = {}
    for item in homeList:
        if item.room in homeMap.keys():
            homeMap[item.room].append(item)
        else:
            homeMap[item.room] = [item]
    return homeMap

def counter(homeList, printOut = True):
    """
    Takes in a list of Furnishing sub-class objects as a list
    Returns a dictionary of types of objects and their number.
    Also optionally prints out a list.
    """
    homeCount = {"Bed" : 0, "Bookshelf" : 0, "Sofa" : 0, "Table" : 0}
    for item in homeList:
        homeCount[type(item).__name__] += 1
    if printOut:
        for k, v in homeCount.items():
            if k == "Bookshelf":
                print("Bookshelves:", v)
            else: 
                print(k + "s:", v)
    return homeCount
        
if __name__ == "__main__":
    home = [] 
    home.append(Bed('Bedroom'))
    home.append(Sofa('Living Room'))
    home.append(Bookshelf('Bedroom'))
    home.append(Bookshelf('Dining Room'))
    for k,v in mapTheHome(home).items():
        print(k, v)
    counter(home)

        
    