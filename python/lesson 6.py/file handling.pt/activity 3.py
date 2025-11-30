file = open('python/lesson 6.py/file handling.pt/Codingal.txt')
Counter = 0
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        Counter+= 1
print("This is the number of the lines in the file:")
print(Counter)