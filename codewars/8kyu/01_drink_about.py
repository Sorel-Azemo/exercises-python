"""
Problem:
    Return what a person drinks depending on their age:
    under 14 -> toddy, under 18 -> coke, under 21 -> beer,
    21 or more -> whisky.

Example:
    people_with_age_drink(17)  ->  "drink coke"

What I learned:
    if/elif/else conditions are checked in order,
    so each elif only needs the upper limit of its age range.

Source: https://www.codewars.com/kata/56170e844da7c6f647000063

"""

def people_with_age_drink(age):
    if age < 14:
        drink = "drink toddy"
    elif age < 18:
        drink = "drink coke"
    elif age < 21:
        drink = "drink beer"
    else:
        drink = "drink whisky"
    return drink
