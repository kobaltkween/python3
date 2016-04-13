"""
A simple iterator object specification
"""

class gen123:
    
    def __init__(self, lst):
        "Initialize the iterator object."
        self.lst = lst
        self.itemNum = 0
        self.count = 1
    
    def __iter__(self):
        "This object is not an iterable"
        return self
    
    def __next__(self):
        if self.count > self.itemNum:
            try:
                self.val = self.lst[self.itemNum]
            except IndexError:
                raise StopIteration
            self.itemNum += 1
            self.count = 1
        self.count += 1
        return self.val