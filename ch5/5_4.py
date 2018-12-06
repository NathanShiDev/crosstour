# if elif els
name = input('What is your name?')
if name.endswith('Gumby'):
    print('Hello, Mr. Gumby')
elif name.endswith('sheldon'):
    print('Hello, Sheldon')
else:
    print('Hello, stranger')

print()

status = 'friend' if name.endswith('sheldon') else 'stranger'
print('status : ', status)
print()

if name.endswith('Gumby'):
    if name.startswith('Mr'):
        print('Hello, Mr, Gumby')
    elif name.startswith('Mrs'):
        print('Hello, Mrs, Gumby')
    else:
        print('Hello, Ms, Gumby')
elif name.endswith('sheldon'):
    if name.startswith('Mr'):
        print('Hello, Mr, Sheldon')
    elif name.startswith('Mrs'):
        print('Hello, Mrs, Sheldon')
    else:
        print('Hello, Ms, Sheldon')
else:
    print('Hello, stranger')

