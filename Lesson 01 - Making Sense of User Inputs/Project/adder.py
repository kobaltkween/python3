"""
adder.py: take two integers and add them together
"""

def adder(int1, int2):
    if not (type(int1) == type(int2) == int):
        raise TypeError("Both arguments must be integers.")
    return  int1 + int2