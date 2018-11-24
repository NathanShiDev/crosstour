# 2-1
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
          + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

year = input('Year:')
month = int(input('Month:'))
day = input('Day:')

month_name = months[month - 1]
ordinal = day + endings[int(day) - 1]

print(ordinal + ' ' + month_name + ' ' + year)
