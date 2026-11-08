"""
Problem:
You get an array of numbers, return the sum of all of the positives ones.

Example
[1, -4, 7, 12] => 1+7+12=20

Note
If there is nothing to sum, the sum is default to 0.

What I learned:
-The built-in sum() function can be used to calculate the sum of an iterable. 
- A generator expression can be used to filter and sum values in a concise way.

ALtenative solution:
def positive_sum(arr):
    return sum( x for x in arr if x > 0 )

Source:
https://www.codewars.com/kata/5715eaedb436cf5606000381/python
"""
def positive_sum(arr):
    total = 0
    for i in arr:
        if i > 0:
            total += i
    return total
