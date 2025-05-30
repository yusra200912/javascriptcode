#def intro(name):
#    print("Hello my name is" , name)

#user_name = input("Enter your name")
#intro(user_name)

def recur_factorial(n):
    if n==1:
        return n
    else: 
        n*recur_factorial(n-1)

num= int(input("Enter a number"))            


