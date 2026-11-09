"""
Problem:
Create a function that always returns True/true for every item in a given list.
However, if an element is the word 'flick', switch to always returning the opposite boolean value.

Examples
['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
Notes
"flick" will always be given in lowercase.
A list may contain multiple flicks.
Switch the boolean value on the same element as the flick itself.

What I learned:
- (1- state) enabled me to obtain the opposite bolean value 

Alternative solution:
- Instead of state = (1-state), I could use state = not state 
Source:
https://www.codewars.com/kata/64fbfe2618692c2018ebbddb/python
"""

def flick_switch(lst):
    result = []
    state = True 
    for i in lst:
        if i != 'flick' :
            result.append(state)
            
        else:
            state = (1 - state )
            result.append(state)
    return result
