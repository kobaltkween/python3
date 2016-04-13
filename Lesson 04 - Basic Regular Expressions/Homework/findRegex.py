"""
findRegex.py - A simple regex finder that takes a string, looks for it in another string, 
            and returns a dictionary with the start and end positions of the first instance.
"""
import re

def finder(str, txt):
    s = re.search(str, txt)
    if s:
        return {'start' : s.start(), 'end' : s.end()}
    else:
        print("String not found in text")
        return None