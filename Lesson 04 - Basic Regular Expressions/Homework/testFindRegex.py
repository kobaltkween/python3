'''
Created on Jan 4, 2016

@author: mboyd

A test for a simple function that uses regular expression to search a text.
'''
import unittest
from findRegex import finder


class TestFindRegex (unittest.TestCase):

    def testFinder(self):
        txt = 'In the 1950s, mathematician Stephen Cole Kleene described automata theory '
        txt += 'and formal language theory in a set of models using a notation called '
        txt += '"regular sets" as a method to do pattern matching. Active usage of this '
        txt += 'system, called Regular Expressions, started in the 1960s and continued '
        txt += 'under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, '
        txt += 'Ken Thompson, and Henry Spencer.'
        res = finder("Regular Expressions", txt)
        self.assertEqual(res['start'], 231, "The start position should be 231.")
        self.assertEqual(res['end'], 250, "The end position should be 250.")

if __name__ == "__main__":
    unittest.main()