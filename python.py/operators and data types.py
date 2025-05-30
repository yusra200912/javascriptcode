num1 = 10 #int
num2 = 20.5 #float

#sequence types
text = "hello"#string
fruits = ["apple" , "banana", "orange"]#list/array

#Mapping type JSON
student_info ={
    "name" : "yusra",
    "age" : 15
} #dict / obj

#Boolean types
is_python_fun = True #bool

#print the data types
print(type(num1)) #int
print(type(text))# string
print(type(student_info))#dict/obj

#arithmetic operators
a = 10
b = 2
print("Addition", a+b) # output: 12
print("Subtraction", a-b) # alt + shift + down arrow for copy and paste the same line output : 8
print("Multiplication", a*b) #output: 20
print("Division", a/b) #output : 5
print("Modulus", a%b) #output : 0 

#comparision operators
print("Is a equal to b ?" , a==b) #output: false
print("Is a greater than b ?" , a>b)#output:true
print("Is a less than b ?" , a<b) # output: false

#logical operators
x=True
y= False
print(" x and y" , x and y) # output: false
print(" x or y" , x or y) # output: true
print(" not y" , not y) # output: true
print("  not x" ,  not x) # output: false

#Assignment operators
c=5
c+= 2 #same as c = c + 2
print("c after +=" ,c) #output: 7

# inputs
print("hello world")
name = input("what is your name ?")
print ("hello" , name)


