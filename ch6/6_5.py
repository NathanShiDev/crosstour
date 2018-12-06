x = 1
scope = vars()
print(scope)
print()
print(scope['x'])


def combine(parameter):
    print('locals :', locals())
    print(parameter, globals()['parameter'])


parameter = 'good'
combine('a')

