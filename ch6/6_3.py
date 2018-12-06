def fibs(nums):
    result = [0, 1]
    for i in range(nums - 2):
        result.append(result[-1] + result[-2])

    return result


num = int(input('Input the fibs num:'))
print('fibs:', fibs(num))
print()


def square(x):
    'Calculates the square of the number x.'
    return x * x


print('square : ', square(num))
print(square.__doc__)
print()

