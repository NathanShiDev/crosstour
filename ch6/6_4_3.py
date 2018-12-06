def hello_1(greeting, name):
    print('{}, {}'.format(greeting, name))


def hello_2(name, greeting):
    print('{}, {}'.format(greeting, name))


hello_1('hello', 'nathan')
hello_2('nathan', 'hello')

hello_1(name='nathan', greeting='hello')
hello_2(greeting='hello', name='nathan')


def hello_3(greeting='hello', name='nathan'):
    print('{}, {}'.format(greeting, name))


hello_3()
hello_3(greeting='how are you')
hello_3(name='sheldon')
hello_3(greeting='okay', name='Jie')


def hello_4(name, greeting='Hello', punctuation='!'):
    print('{}, {}{}'.format(greeting, name, punctuation))


hello_4('nathan')
