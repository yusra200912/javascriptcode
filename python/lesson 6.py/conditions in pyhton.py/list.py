list = ['apple', 'kiwi', 'strawberry', 'mango']

print('Length of list:', len(list))
print("First element", list[0])
print("Lsst element", list[-1])

list.append('Papaya')
print("Updated list:", list)

list.remove('kiwi')
print("Updated list:", list)

list.sort()
print("Sorted list", list)

list.pop(1)
print("Updated list:", list)

list.reverse()
print("Reversed list:", list)

print("Multiplication on list", list*2)

list= list[:2]
print("Sliced list:", list)

list.clear()
print("Updated list:", list)