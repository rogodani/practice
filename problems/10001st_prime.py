'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

import math


def prime(num):
    for div in range(2, round(math.sqrt(num)) + 1):
        if num % div == 0:
            return False
    return True

def find_10001st_prime():
    count = 0
    n = 1
    while count < 10001:
        n += 1
        if prime(n):
            count += 1
    return n

print(find_10001st_prime())
print(prime(104729))