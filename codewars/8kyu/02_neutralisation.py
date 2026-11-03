"""
Problem:
    Two strings of the same length contain only "+" and "-".
    Compare them character by character: identical signs stay the same,
    different signs become "0". Return the resulting string.

Example:
    neutralise("+-+", "+--")  ->  "+-0"

What I learned:
    In a for loop, range() moves the index forward by itself,
    so there is no need to increment it manually.

Source: https://www.codewars.com/kata/COLLE-TON-LIEN-ICI
"""

def neutralise(s1, s2):
    result = ""
    for position in range(len(s1)):
        if s1[position] == s2[position]:
            result += s1[position]
        else:
            result += "0"
    return result
