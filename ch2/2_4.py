# 2-4
database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

user_name = input('User name: ')
pin_code = input('PIN Code : ')

if [user_name, pin_code] in database:
    print('Access granted')
else:
    print('Error User Name or Pin Code')
