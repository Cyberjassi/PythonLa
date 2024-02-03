# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx
    
# @greet
# def hello():
#     print("hello how are you")

# hello()


def greet(fx):
    def mfx(*args):
        print("Good Morning")
        fx(*args)
        print("Thanks for using this function")
    return mfx
    
@greet
def add(a,b):
    print(a+b)
add(2,3)

