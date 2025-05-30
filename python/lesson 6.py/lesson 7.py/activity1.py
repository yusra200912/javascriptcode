lst = ['Apple','Guava','Mango','Berry']

print("Length of the list:" , len(lst))
print("First element", lst[0])
print("Last element", lst[-1])

lst.append('Kiwi')
print('Updatted list:', lst)

lst.remove('Guava')
print('Updated list:', lst)

lst.sort()
print("Updated List:", lst)

lst.pop(1)
print('Updated list:', lst)

lst.reverse()
print('Updated list:', lst)

print('Multiplication of list:', lst*2)

lst= lst[:4]
print('Sliced list:', lst)

lst.clear()
print('Updated list:', lst)