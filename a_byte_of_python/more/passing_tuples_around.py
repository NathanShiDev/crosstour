def get_error_details():
    return (2, 'this is error detail')


err_code, err_message = get_error_details()

print('error code :', err_code)
print('error message :', err_message)


def swap(a, b):
    return (b, a)

a = 5
b = 10
print('before swap, a : {}, b : {}'.format(a, b))
a, b = swap(a, b)
print('after swap, a : {}, b : {}'.format(a, b))
