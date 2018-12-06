# store
# def store(data, full_name):
#     names = full_name.split()
#     if len(names) == 2:
#         names.insert(1, '')
#     labels = ['first', 'middle', 'last']
#
#     for label, name in zip(labels, names):
#         people = lookup(data, label, name)
#         if people:
#             people.append(full_name)
#         else:
#             data[label][name] = [full_name]


def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = ['first', 'middle', 'last']

        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


# lookup
def lookup(data, label, name):
    return data[label].get(name)


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


storage = {}
init(storage)

me = 'Magnus Lie Hetland'
print('storage before store me, storage :', storage)
print()
store(storage, me)
print('storage after store me, storage :', storage)
print()
sheldon = 'sheldon shi'
store(storage, sheldon)
print('storage after store sheldon, storage :', storage)
print()
