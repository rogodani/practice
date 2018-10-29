"""
Write a Python function to multiply all the numbers in a list.
Sample List : [1, 2, 3, -4]
Expected Output : -24
"""


def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print(multiply([1, 2, 3, -4]))
