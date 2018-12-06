try:
    x = int(input('Enter the first number:'))
    y = int(input('Enter the second number:'))
    print('x/y =', x / y)
except ZeroDivisionError:
    print('The second number is zero')
except Exception:
    print('The first or second number is not number')
