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
        
my_gen = FirstHundredGenrator()
print(next(my_gen))
print(my_gen.__next__())

# for i in next(my_gen):
#     print(i)

# class FirstFiveIterator:
#     def __init__(self) -> None:
#         self.numbers = [1,2,3,4,5]
#         self.i = 0
#     def __next__(self):
#         if self.i < len(self.numbers):
#             current = self.numbers[self.i]
#             i += 1
#             return current
#         else:
#             raise StopIteration()