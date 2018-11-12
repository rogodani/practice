'''
generating/testing prime numbers
'''
__version__ = '0.0.1'
__author__ = 'Daniel'

import math


class Prime:

    def __init__(self, number=2, up_to=2):
        self.number = number
        self.up_to = up_to

    def check_if_prime(self, num):
        for div in range(2, round(math.sqrt(num)) + 1):
            if num % div == 0:
                return False
        return True

    def get_prime_numbers(self, up_to):
        return [num for num in range(2, up_to + 1) if self.check_if_prime(num)]

    def get_sum_of_prime_numbers(self, up_to):
        return sum(self.get_prime_numbers(up_to))
