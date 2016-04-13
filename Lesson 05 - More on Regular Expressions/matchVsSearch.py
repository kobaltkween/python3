"""
Demonstrate the difference between match() and search().
"""

import re

def checkNumber(text):
    regex = r"(\d{3}|\(\d{3}\))(-| )\d{3}-\d{4}"
    match = re.match(regex, text)
    if match:
        return match.group()
    match = re.search(regex, text)
    if match:
        return len(text)