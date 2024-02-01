divide = lambda x,y:x/y
print(divide(55,3))


print((lambda x,y:x**y)(12,3))



avg = lambda marks:sum(marks)/len(marks)

student = [
    {'name':'jayu','grade':(76,56,87,97,45)},
    {'name':'vij','grade':(44,55,33,65,45)},
    {'name':'nir','grade':(76,56,45,76,98)},
    {'name':'hir','grade':(88,65,67,43,56)},
]
for i in student:
    print(avg(i['grade']))