# dict methods
# https://www.programiz.com/python-programming/methods/dictionary

# clear
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print('Before dictionary clear, d : ', d)
d.clear()
print('After dictionary clear, d : ', d)
print()

# copy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
print('x :', x)
print('y :', y)
print()

# fromkeys
d = dict.fromkeys(['name', 'age'])
print('After fromkeys, d : ', d)
d = dict.fromkeys(['key1', 'key2'], 'unknown')
print('After fromkeys, default value "unknown", d : ', d)
print()

# get
# 4-2

# items
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'spam': 0
}
items = d.items()
print('Dict d :', d)
print('Items items :', items)
print('Items length : ', len(items))
print()

# keys
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'spam': 0
}

keys = d.keys()
print('Keys of d :', keys)
print()

# pop
d = {'x': 1, 'y': 2}
print('Before dict pop, d :', d)
pop_value = d.pop('x')
print('After dict pop x, d :', d)
print('pop value :', pop_value)
print()

# setdefault
d = {}
value = d.setdefault('name', 'n/a')
print('d after setdefault, d : ', d)
print('value : ', value)
print()
d['name'] = 'sheldon'
value = d.setdefault('name', 'n/a')
print('d after setdefault, d:', d)
print('value : ', value)
print()

# update
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}
print('Before dict update, d :', d)
x = {'title': 'Python Language Website'}
d.update(x)
print('After dict update, d :', d)
print()

# values
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}
values = d.values()
print('values of d :', values)
print()