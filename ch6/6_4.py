def try_to_change(n):
    n = 'sheldon'


name = 'jie'
print('name before try_to_change, name :', name)
try_to_change(name)
print('name after try_to_change, name :', name)
print()


def change(n):
    n[0] = 'sheldon'


names = ['hello', 'jie', 'nathan']
print('names before change, names :', names)
change(names)
print('names after change, names :', names)


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


storage = {}
init(storage)
print('storage after init, storage : ', storage)

me = 'Magnus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]


def lookup(data, label, name):
    return data[label].get(name)


lookup_name = lookup(storage, 'middle', 'Lie')
print('Look up middle Lie, name:', lookup_name)



