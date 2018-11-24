# string methods
# https://www.programiz.com/python-programming/methods/string

# center
original_str = 'he Middle by Jimmy Eat World'
print('Before use string center')
print(original_str)
print('Before use string center')
print(original_str.center(40))
print(original_str.center(40, '*'))
print()

# find
###### 0123456789
str = 'With a moo-moo here, and a moo-moo there'
index = str.find('moo')
print('index of first "moo" in str : ', index)
print()
index = str.find('sheldon')
print('index of first "sheldon" in str : ', index)
print()

# rfind
###### 0123456789.....................31.......
str = 'With a moo-moo here, and a moo-moo there'
index = str.rfind('moo')
print('index of last "moo" in str : ', index)
print()
index = str.rfind('sheldon')
print('index of last "sheldon" in str : ', index)
print()

# split
# the default separator is space.
str = 'ab cde fghi'
list_str = str.split()
print('str : ', str, ', list_str:', list_str)
str = 'ab-cde-fghi'
list_str = str.split('-')
print('str : ', str, ', list_str:', list_str)
print()

# join
list_str = ['ab', 'cde', 'fghi']
str = ''.join(list_str)
print('list_str:', list_str, ', after join:', str)
list_str = ['ab', 'cde', 'fghi']
str = '**'.join(list_str)
print('list_str:', list_str, ', after join:', str)
print()

# lower
str = 'Trondheim Hammer Dance'
print('Str :', str, ', lower str:', str.lower())
print()

# upper
str = 'Trondheim Hammer Dance'
print('Str :', str, ', upper str:', str.upper())
print()

# title
str = 'hello world'
print('Str :', str, ', upper str:', str.title())
print()

# replace
str = 'This is a test'
print('Before string replace, str :', str)
str1 = str.replace('is', 'iiiiiiiissssss')
print('After string replace, str :', str, ',str1 : ', str1)
print()


# strip
str = ' internal whitespace is kept '
print('Before string strip, str : ', str)
str1 = str.strip()
print('After string strip, str : ', str, ', str1:' + str1)
print()
