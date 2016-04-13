import re

def sentenceSplit(text):
    return re.split(r"[?.!]\s+", text)