file_read = open('python/lesson 6.py/file handling.pt/Coding.txt')
print(file_read.read())
file_read.close()

file_write = open('python/lesson 6.py/file handling.pt/Coding.txt' , 'w')
file_write.write("File in write mode")
file_write.write("Coding is the precise art of translating human logic into a universal machine language that powers innovation and solves complex problems")
file_write.close()

file_append = open('python/lesson 6.py/file handling.pt/Coding.txt' , 'a')
file_append.write("\n File in append mode")
file_append.write("Coding is the modern superpower that allows us to build the future, one precise instruction at a time")
file_append.close()