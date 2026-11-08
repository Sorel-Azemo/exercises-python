"""
Problem:
Your phone shows its battery as a row of 5 bars. Each full bar represents 20% of charge. A bar only lights up when its whole 20% is reached.

Write a function battery_bars(percent) that returns the battery as a string: # for a lit bar, . for an empty one, all wrapped in square brackets.

Examples
battery_bars(100)  # => "[#####]"
battery_bars(70)   # => "[###..]"
battery_bars(20)   # => "[#....]"
battery_bars(19)   # => "[.....]"
battery_bars(0)    # => "[.....]"
Notes
percent is an integer from 0 to 100

What I learned:
- Use string concatenation to build the final result
- Integer division (//) returns the quotient without the remainder.
- String multiplication (*) repeats a string a specified number of times.

Source:
https://www.codewars.com/kata/6ad649de715eb5f5359a7e62/python
"""

def battery_bars(percent):
   
    lit_bar = percent // 20
    empty_bar = 5 - (percent // 20)
    
    return ("["+ ("#" * lit_bar) + ('.' * empty_bar) + "]")
    
