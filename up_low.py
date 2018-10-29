"""
**Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**

    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output :
    No. of Upper case characters : 4
    No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**

If you feel ambitious, explore the Collections module to solve this problem!
"""


def up_low(s):
    up = 0
    low = 0
    for letter in s:
        if letter.islower():
            low += 1
        elif letter.isupper():
            up += 1
    return up, low


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
values = up_low(s)
print(f'No. of Upper case characters :  {values[0]}\nNo. of Lower case Characters :  {values[1]}')
