def greet():
    print('hello')

def before_and_after(func):
    print("Before ")
    func()
    print("After")

before_and_after(greet)