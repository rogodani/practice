import math


def prime(num):
    for div in range(3, round(math.sqrt(num)) + 1, 2):
        if num % div == 0:
            return False
    return True


def count_primes(num):
    if num < 2:
        return 0
    count = 1
    for n in range(3, num, 2):
        if prime(n):
            count += 1
    return count


print(count_primes(100))
