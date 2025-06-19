class Cat :
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Hi I am a cat. My name is {self.name} and i am {self.age} years old")
    
    def make_sound(self):
        print("Meow")
class Dog :
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def info(self):
        print (f"Hi I am a dog. My name is {self.name} and i am {self.age} years old") 
    def make_sound(self):
        print("Bark")  

Cat1 = Cat('Dogo', 3)
Dog1 = Dog('Tyson' , 2)  

for animal in (Cat1 , Dog1):
    animal.make_sound()
    animal.info()
