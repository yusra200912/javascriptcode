def is_disarium(num):
    digits = str(num)
    total = 0

    for index, digit in enumerate(digits):
        total += int(digit) ** (index + 1)   
    
    return total == num

number = int(input("Enter a number: "))

if is_disarium(number):
    print(number, "is a Disarium number")
else:
    print(number, "is NOT a Disarium number")
