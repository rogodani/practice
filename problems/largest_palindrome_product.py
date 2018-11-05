'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


# version 1
def palindrome(n):
    return str(n) == str(n)[::-1]


def large_product():
    z = 0
    for x in reversed(range(100, 1000)):
        for y in reversed(range(100, x)):
            product = x * y
            if palindrome(product) and product > z:
                z = product
    return z


print(large_product())

# version 2
large_prod = [x * y for x in reversed(range(100, 1000)) for y in reversed(range(100, x))]
large_palindrome = max(list(filter(lambda n: str(n) == str(n)[::-1], large_prod)))
print(large_palindrome)
