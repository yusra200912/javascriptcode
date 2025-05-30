#empty tupled
my_tuple = ()
print(my_tuple)

#tuple having integers
my_tuple = (1,2,3)
print(my_tuple)

#tuple with mixed data types
my_tuple = (1,'hello',3.4)
print(my_tuple)

#nested loop
my_tuple=('mouse', [3,4,5],(1,2,3))
print(my_tuple)

#acessing tuple elements using indexes
my_tuple=('p','q','r','s','t')
print(my_tuple[0])
print(my_tuple[3])

#nested tuple
n_tuple = ('mouse',[3,4,5],(1,2,7))

#nested index
print(n_tuple[0][3])
print(n_tuple[1][1])

#slicing
print("sliced:" , my_tuple[1:4])

#iterating through tuple
for letter in (my_tuple):
    print("hello" , letter)