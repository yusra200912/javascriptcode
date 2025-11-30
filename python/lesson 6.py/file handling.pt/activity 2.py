file_read = open('python/lesson 6.py/file handling.pt/Codingal.txt' , 'r')
print("File in read mode-")
print(file_read.read())
file_read.close()

file_write = open('python/lesson 6.py/file handling.pt/Codingal.txt' , 'w')
file_write.write("File in write mode")
file_write.write("Hi , Im Yusra , im 16 years old")
file_write.close()

file_append = open('python/lesson 6.py/file handling.pt/Codingal.txt' , 'a')
file_append.write("\n File in append mode")
file_append.write("Hi im yusra. im 16 yr old")
file_append.close()