'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

import math


def prime(num):
    for div in range(3, round(math.sqrt(num)) + 1, 2):
        if num % div == 0:
            return False
    return True


num = 600851475143
factors = list(filter(lambda factor: num % factor == 0, range(1, int(math.sqrt(num)) + 1)))
print(max(list(filter(prime, factors))))
