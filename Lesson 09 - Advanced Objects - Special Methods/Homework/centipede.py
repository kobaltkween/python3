"""
centipede.py:  A class to demonstrate magic methods
"""

class Centipede(object):
    def __new__(cls):
        cls.legs = []
        cls.stomach = []
        return object.__new__(cls)
            
    def __call__(self, *args):
        for a in args:
            self.stomach.append(a)
            
    def __str__(self):
        return ",".join(self.stomach)
    
    def __setattr__(self, key, value):
        if  key == "stomach" or key == "legs":
            raise AttributeError("{0} is for internal use only".format(key))
        else:
            self.legs.append(key)
        self.__dict__[key] = value
    
    def __repr__(self):
        return ",".join(self.legs)  

            

if __name__ == "__main__":
    ralph = Centipede()
    ralph('pretzel')
    print(ralph.stomach)
    ralph('pickles')
    print(ralph)
    ralph.shoes = 100
    ralph.hat = 1
    print(ralph.legs)
    print(repr(ralph))
    #  Noting that the class attributes aren't in the instance __dict__
    print(ralph.__dict__)