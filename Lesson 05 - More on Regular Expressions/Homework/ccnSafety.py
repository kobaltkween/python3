import re

def ccnReplace(txt):
    "Return input text with X substituted for all but the last four digits of any credit card numbers in the text."
    return re.sub("(\d{4}-){3}", (("X" * 4) +  "-") * 3, txt)