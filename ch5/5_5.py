# while
print('while begin************')
x = 1
while x <= 100:
    print('x =', x)
    x = x + 1
print('while end************')
print()

# for
print('for begin************')
for x in range(1, 101):
    print('x =', x)
print('for end************')
print()

# for list
print('for begin************')
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print('word :', word)
print('for end************')
print()

# for dictionary, keys
print('for begin************')
d = {
    'x': 1,
    'y': 2,
    'z': 3
}
for key in d.keys():
    print('key :', key, ', value :', d[key])
print('for end************')
print()

# for dictionary, key/value
print('for begin************')
d = {
    'x': 1,
    'y': 2,
    'z': 3
}
for key, value in d.items():
    print('key :', key, ', value :', value)
print('for end************')
print()

# zip
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
name_age_list = list(zip(names, ages))
print('name age list :', name_age_list)
print()

for name, age in zip(names, ages):
    print('Use zip, name :', name, ', age :', age)
print()

