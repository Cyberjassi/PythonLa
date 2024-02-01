def greet():
    print("jai shree ram")

hello = greet
hello()


total = lambda marks:sum(marks)
avg = lambda marks:total(marks)/len(marks)
highest = lambda marks:max(marks)

student = [
    {'name':'jayu','grade':(76,56,87,97,45)},
    {'name':'vij','grade':(44,55,33,65,45)},
    {'name':'nir','grade':(76,56,45,76,98)},
    {'name':'hir','grade':(88,65,67,43,56)},
]
operation = {
    'total':total,
    'avg':avg,
    'highest':highest
}

for i in student:
    op = input("what you want perform total/avg/highest")
    final_op = operation[op]
    print(final_op(i['grade']))