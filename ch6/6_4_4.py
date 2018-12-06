def print_params(*params):
    print(params)


print_params()
print()
print_params(1)
print()
print_params(1, 2, 3, 4)
print()


def print_params_1(title, *params):
    print('title :', title)
    print('params :', params)


print_params_1('multiple parameters', 'a', 'b', 'c')


def print_params_2(x, *y, z):
    print('x :', x)
    print('y :', y)
    print('z :', z)


print_params_2(1, 2, 3, 4, 5, 6, z='9')


def print_params_3(**params):
    print('params :', params)


print_params_3(a=1, b=2, c=3)
