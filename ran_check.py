"""
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""


def ran_check(num, low, high):
    if num in range(low, high + 1):
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is not in the range between {low} and {high}')


ran_check(5, 2, 7)


def ran_bool(num, low, high):
    return num in range(low, high + 1)


print(ran_bool(3, 1, 10))
