from math import sqrt

num = int(input("Enter a number: "))

if num > 1:
    is_prime = True
    for i in range(2, int(sqrt(num)) + 1):  # Using sqrt for optimization
        if num % i == 0:
            is_prime = False
            break  # No need to check further

    if is_prime:
        print("The number is prime")
    else:
        print("The number is not prime")
else:
    print("The number is not prime")
