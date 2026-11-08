"""Problem:
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined

What I learned:
- The count() method can be used to count occurrences of a value in a list.
- A boolean value can be used directly in a condition.

Alternative solution:
 def count_sheeps(sheep):
    return sheep.count(True)

Source:https://www.codewars.com/kata/54edbc7200b811e956000556/solutions/python
"""
def count_sheeps(sheep):
    number = 0
    for i in sheep:
        if i is True:
            number += 1
    return number
