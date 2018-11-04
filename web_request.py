import urllib.request
import re

def get_source(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return html

def print_source(url):
    print(get_source(url).decode())

html = get_source("http://www.pythonchallenge.com/pc/def/ocr.html")

# https://docs.python.org/3.6/howto/regex.html#greedy-versus-non-greedy
# https://docs.python.org/3.6/howto/regex.html#compilation-flags
input_string = re.findall(b"<!--(.*?)-->", html, flags = re.DOTALL)[-1].strip().decode()
# print(input_string)
print("".join(char for char in input_string if char.isalpha()))

import string
y = list(filter(lambda x: x in string.ascii_letters, html))
print(y)