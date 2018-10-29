def paper_doll(text):
    return "".join([letter * 3 for letter in text])

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))