"""
Write a function that computes the volume of a sphere given its radius.
"""

from math import pi, pow


def vol(rad):
    return 4 / 3 * pi * pow(rad, 3)


print(vol(2))
