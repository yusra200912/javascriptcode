def test(lst):
        result = {}
        for item in lst :
             result[item[0]]= item[1:]
        return result 

students = [1,'yusra','V'],[2 , 'zoya','V'],[3,'samya','VI'],[4,'zehra','VI'],[5, 'mona','VII']

print("/n0riginal list of lists:")
print(students)
print("/nCOonverted list to a dictionary")
print(test(students))
