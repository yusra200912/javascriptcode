class parrot :
    species = "bird"

    def __init__(self , name , age):
        self.name = name
        self.age = age

blu = parrot("blu" , 3)
woo = parrot("woo" , 5)

print("blu ia a {}" .format (blu.species))
print("woo ia a {}".format (woo.species))

print("{} is {} years old".format (blu.name , blu.age))
print("{} is {} years old".format (woo.name , woo.age))

