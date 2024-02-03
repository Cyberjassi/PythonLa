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
        Animal.show(self)
        print(f"Your animal name is {self.name} and your dog name is {self.dog}")
class Breed(Dog,Animal):
    def __init__(self,name,dog,breed):
        Dog.__init__(self,name,dog)
        self.breed = breed
    def show(self):
        Dog.show(self)
        print(f"your breed name is {self.breed}")

mdb = Breed('dog','tony','simple')
mdb.show()
print(Breed.mro())

