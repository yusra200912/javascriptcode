my_dict = {}

#dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

#dictionary with mixed keys
my_dict={'name':'john' ,1: [2,4,5]}
my_dict = {'name': 'yusra' , 'age': '15'}

print(my_dict['name'])
print(my_dict['age'])

#updated vallue
my_dict['age'] = 17
print(my_dict)

#add item
my_dict['class']= '10th'
print(my_dict)

#remove element
my_dict.pop('age')
print(my_dict)

#acess pirticular element
print("class :", my_dict.get('class'))

#remove all element
my_dict.clear()
print(my_dict)