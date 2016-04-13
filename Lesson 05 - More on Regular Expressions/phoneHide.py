import re

def phoneHide(text):
    # Don't forget to use a raw string constant!
    return re.subn(r"\d{3}-\d{4}", "XXX-XXXX", text)