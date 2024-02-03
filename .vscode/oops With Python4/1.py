class Student:
    def __init__(self,name,grade):
        self.n = name
        self.g = grade
    def avg(self):
        return sum(self.g)/len(self.g)
    
stu = Student('jay',[23,54,65,45])
print(stu.n)
print(stu.g)
print(stu.avg())
print(stu.__class__)

def average(student):
    return sum(student.g)/len(student.g)

print(average(stu))