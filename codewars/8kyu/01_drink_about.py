"""
Kata: Drink about
Level: 8 kyu
Link: https://www.codewars.com/kata/COLLE-TON-LIEN-ICI
Date: 2026-11-02
What I learned: if/elif/else conditions are checked in order,
so each elif only needs the upper limit of its age range.
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
