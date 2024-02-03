from typing import Any


class Stud:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"The name of employee is {self.name}"
    def __call__(self):
        print("hii")
    
s = Stud('jayu')
print(s)
s()