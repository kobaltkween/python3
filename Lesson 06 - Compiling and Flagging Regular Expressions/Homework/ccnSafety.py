import re

def ccnReplace(txt):
    """Return input text with phrase 'CCN REMOVED FOR YOUR SAFETY' 
    substituted for all but the last four digits of any credit 
    card numbers in the text."""
    regex = re.compile(r"""
            (\d{4}-){3}        # 3 multiples of 4 digits followed by a dash
            \d{4}              # 4 digits in a row 
            """, re.VERBOSE)
    
    return regex.sub("CCN REMOVED FOR YOUR SAFETY", txt)