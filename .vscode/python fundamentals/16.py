name = ["A","B","C"]
age = [13,23,54]
touplecopy = list(zip(name,age))
print(touplecopy)


name = ["A","B","C"]
age = [13,23,54]
touplecopy = dict(zip(name,age))
print(touplecopy)

name = ["A","B","C"]
age = [13,23,54,87]
marks = [1,2,3,54,56,76,67,45,43,76]
child = [2,5,4,6,4,6,4,3,5,6]
touplecopy = list(zip(name,age,marks,child))
print(touplecopy)