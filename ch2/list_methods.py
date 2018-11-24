# list methods
# https://www.programiz.com/python-programming/methods/list

# append
lst = [1, 2, 3]
print('Before list append: ', lst)
lst.append(4)
print('After list append:', lst)
print()

# clear
lst = [1, 2, 3]
print('Before list clear: ', lst)
lst.clear()
# same effect:
# lst[:] = []
print('After list clear: ', lst)
print()

# copy
list1 = [1, 2, 3]
list2 = list1.copy()
# same effect
# list2 = list1[:]
# list2 = list(list1)
print('After list copy:')
print('list1 :', list1, ', list2 :', list2)
list2[1] = 100
print('After change list2:')
print('list1 :', list1, ', list2 :', list2)
print()

# count
lst = ['good', 'good', 'ok', 'good']
print('count of good:', lst.count('good'))
lst = [[1, 2], [1], 1, 2, 1, [1, 1, 1]]
print('count of 1 :', lst.count(1))
print()

# extend
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print('Before list extend, list1 : ', list1, ', list2 : ', list2)
list1.extend(list2)
print('After list extend, list1 : ', list1, ', list2 : ', list2)
print()

# index
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print('index of who in knights : ', knights.index('who'))
print()

# insert
lst = [1, 2, 3, 5, 6, 7]
print('Before list insert, lst : ', lst)
lst.insert(3, 'gooooood')
print('After list insert, lst : ', lst)
print()

# pop
lst = [1, 2, 3, 4, 5]
print('Before list pop, lst:', lst)
pop_value = lst.pop()
print('After list pop, lst:', lst, ', pop value :', pop_value)
print()

# remove
# If a list contains duplicate elements
# the remove() method removes only the first instance
lst = ['to', 'be', 'or', 'not', 'to', 'be']
print('Before list remove, lst : ', lst)
lst.remove('to')
print('After list remove, remove word "to", lst:', lst)
print()

# reverse
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print('Before list reverse, lst:', lst)
lst.reverse()
print('After list reverse, lst:', lst)
print()

# sort
lst = [1, 90, 23, 456, 0, 2, 45, 65, 2]
print('Before list sort, lst:', lst)
lst.sort()
print('After list sort, lst:', lst)
print()


