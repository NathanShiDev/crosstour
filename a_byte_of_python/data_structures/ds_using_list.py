shopping_list = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shopping_list), 'to purchase.')

print('These items are:', end=' ')
for item in shopping_list:
    print(item, end=' ')

print()

print('I also have to buy some rice.')
shopping_list.append('rice')
print('My shopping list is now', shopping_list)

print('I will sort my shopping list now.')
shopping_list.sort()
print('My sorted shopping list is now', shopping_list)

print('The first item I will buy is', shopping_list[0])
olditem = shopping_list[0]
del shopping_list[0]
print('I bought the', olditem)
print('My shopping list is now', shopping_list)
