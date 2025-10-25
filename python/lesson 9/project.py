class Adder:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add(self):
        return self.num1 + self.num2 + self.num3


# Take input from user (outside the class)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Create object of Adder class
adder_obj = Adder(num1, num2, num3)

# Call the add method and display the result
print("The sum of the three numbers is:", adder_obj.add())
