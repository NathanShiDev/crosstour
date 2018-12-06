#
x, y, z = 1, 2, 3
print('x =', x, ', y =', y, ', z =', z)
print()

x, y = y, x
print('x =', x, ', y =', y)
print()

scoundrel = {
    'name': 'Robin',
    'girlfriend': 'Marion'
}

key, value = scoundrel.popitem()
print('key =', key, ', value=', value)
print('After popitem, scoundrel :', scoundrel)
print()

a, b, *rest = [1, 2, 3, 4]
print('a=', a, ', b=', b, ', rest =', rest)
print()

a, *b, c = "abc"
print('a=', a, ', b=', b, ', c =', c)
print()

