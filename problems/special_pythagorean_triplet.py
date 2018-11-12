'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time
from functools import reduce
from math import sqrt
from operator import mul

start = time.time()


def triple(triple_sum):
    euclid_sum = triple_sum / 2
    for m in range(1, int(sqrt(euclid_sum))):
        for n in range(0, int(sqrt(euclid_sum))):
            if m * (n + m) == euclid_sum:
                return 2 * m * n, pow(m, 2) - pow(n, 2), pow(m, 2) + pow(n, 2)


print(reduce(mul, triple(1000), 1))
elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))
