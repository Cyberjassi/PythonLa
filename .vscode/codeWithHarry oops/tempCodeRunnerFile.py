class Animal:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"Your animal name is {self.name}")
class Dog:
    def __init__(self,name,dog):
       Animal.__init__(self,name)
       self.dog = dog
    def show(self):
        Animal.show()
        print(f"Your animal name is {self.name} and your dog name is {self.dog}")
class Breed(Animal,Dog):
    def __init__(self,name,dog,breed):
        Animal.__init__(self,name)
        Dog.__init__(self,dog)
        self.breed = breed

mdb = Breed('dog','tony','simple')

