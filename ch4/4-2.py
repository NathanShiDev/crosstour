people = {
    'Alice': {
        'phone': '2431',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name: ')
request = input('Phone number (p) or address (a)? ')

key = request
if request == 'a':
    key = 'addr'
if request == 'p':
    key = 'phone'

person = people.get(name, {})
print('person', person)
label = labels.get(key, key)
result = person.get(key, 'not available')

print("{}'s {} is {}.".format(name, label, result))
