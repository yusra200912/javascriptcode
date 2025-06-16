class Parrot:  # Class name should be capitalized by convention
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# Creating an object
blu = Parrot("blu", 10)

# Calling methods
print(blu.sing("'Happy'"))
print(blu.dance())
