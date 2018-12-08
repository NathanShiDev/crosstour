print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

mylist = shoplist
print('shoplist is', shoplist)
print('mylist is', mylist)

del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')
mylist = shoplist[:]
print('shoplist is', shoplist)
print('mylist is', mylist)
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
