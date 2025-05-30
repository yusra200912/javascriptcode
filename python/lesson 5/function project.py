n = int(input("Enter a number:"))

a,b = 0,1
count=0

if n<=0:
    print("Please enter a positive number")
elif n==1:
    print("Fibonacci sequence up to", n, "term:")    
    print(a)
else:
    print("Fibonacci sequence up to", n, "term:")
    while count<n:
        print(a, end=' ')
        next_term = a + b
        a = b
        b = next_term
        count += 1  