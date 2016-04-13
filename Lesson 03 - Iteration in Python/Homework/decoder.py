"""
decoder.py: go through a list, and if a value is an integer
            between 1 and 26, replace it with a letter
"""
from string import ascii_uppercase

def alphabator(lst):
    for item in lst:
        if item in range(1, 27):
            yield list(ascii_uppercase)[item - 1]
        else:
            yield item
