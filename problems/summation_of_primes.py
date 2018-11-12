'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import time

from pkg.prime import Prime

start = time.time()

print(Prime().get_sum_of_prime_numbers(2000000))

elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))
