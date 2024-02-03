class ParentClass:
    def parent_method(self):
        print("this is the parent method")

class ChildClass(ParentClass):
    # def parent_method(self):
    #     print("this is child method but name is parent method")
    #     super().parent_method()
    def child_method(self):
        print("This the child methode:")
        super().parent_method()

child_object = ChildClass()
child_object.parent_method()
child_object.child_method()


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def introp(self):
        print(f"Hii My name is {self.name} and my salary is {self.salary}")

class Programmer(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language = language
    def intro(self):
        print(f"Hii My name is {self.name} and my salary is {self.salary} and my Language is {self.language}")
        super().intro()

me = Programmer('jay',12000,'python')
me.introp()
