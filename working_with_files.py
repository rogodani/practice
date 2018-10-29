file_location = '/Volumes/Data/udemy_python/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test.txt'

with open(file_location) as my_file:
    contents = my_file.read()

print(contents)

with open('my_new_file.txt', mode='r') as f:
    print(f.read())

with open('my_new_file.txt', mode='a') as f:
    f.write('\nfour')

with open('my_new_file.txt', mode='r') as f:
    print(f.read())

with open('test.txt', mode='w') as f:
    f.write('new file')

with open('test.txt', mode='r') as f:
    print(f.read())