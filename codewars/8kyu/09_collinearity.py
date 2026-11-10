"""
Problem:
Write the function collinearity(x1, y1, x2, y2), which returns a Boolean type depending on whether the vectors are collinear or not.

Notes
-All vectors start from the origin (x=0, y=0).
-Be careful when handling cases where x1, x2, y1, or y2 are zero to avoid division by zero errors.
-A vector with coordinates (0, 0) is collinear to all vectors.
Examples
collinearity(1,1,1,1) ➞ true
collinearity(1,2,2,4) ➞ true
collinearity(1,1,6,1) ➞ false

What I learned:
- When multiple mathematical approaches can solve a problem, you should generally prefer the one that leads to the simplest,
clearest and most reliable implementation in Python.
-In this case , instead of calculating the ratios, we can apply cross-multiplication,
thereby preventig to deal with Zero Division error


Alternative solution:
def collinearity(x1, y1, x2, y2):
    return x1 * y2 == x2 * y1

Source:
https://www.codewars.com/kata/65ba420888906c1f86e1e680/python
"""

def collinearity(x1, y1, x2, y2):
    if (x1,y1) == (0,0) or (x2,y2) == (0,0):
        return True
        
    try:
        coeffx = x2/x1 
        coeffy = y2/y1 
        
    except ZeroDivisionError:
        return x1 == x2 or y1 == y2
    return coeffx == coeffy
