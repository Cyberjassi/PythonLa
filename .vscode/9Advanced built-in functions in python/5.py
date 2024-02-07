class FirstHundredGenrator:
    def __init__(self) -> None:
        self.number = 1

    def __next__(self):
        if self.number<100:
            current = self.number
            self.number+=1
            return current
        else:
            raise StopIteration()
        
class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenrator()
    
print(sum(FirstHundredIterable()))

class AnotherIterable:
    def __init__(self) -> None:
        self.cars = ['fiesta','focus']
    def __len__(self):
        return len(self.cars)
    def __getitem__(self,i):
        return self.cars[i]
        
for car in AnotherIterable():
    print(car)

