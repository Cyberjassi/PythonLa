l = ["a",'b','c']
for item in l:
    print(item)


for i in range(10):
    print(i)
print("\n")

for i in range(2,10):
    print(i)
print("\n")

for i in range(2,5,10):
    print(i)
print("\n")

students = [
    {'name':'jay','grade':67},
    {'name':'vijay','grade':97},
    {'name':'ajay','grade':86},
    {'name':'sajay','grade':33}
]
for student in students:
    name= student['name']
    grade = student['grade']

    print(f"{name} has a grade of {grade}")



for i in range(1,10,2):
    print(i)