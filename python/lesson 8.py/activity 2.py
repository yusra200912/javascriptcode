class student :
    grade= 10
    name = "penguin"

    def introduction(self):
        print("Hello , im a student")  

    def me(self):
        print("My name is ",self.name)
        print("I study in grade ",self.grade)   

ob = student()
ob.introduction()
ob.me()           