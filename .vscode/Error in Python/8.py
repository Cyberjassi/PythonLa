class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} self.model'
    
class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self,car):
        if not isinstance(car,Car):
            raise MemoryError(f"Tried to add a {car.__class__.__name__} to the garage,but you can only add car ")
        self.cars.append(car)

ford = Garage()
car = Car('ford','Fiesta')

try:
    ford.add_car('fiesta')
except TypeError:
    print('Your car was not a Car!')
except MemoryError:
    print('Your car was not in memory Car!')
finally:
    print("i am always execute:")