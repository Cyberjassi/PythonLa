class M:
    def __init__(self):
        print("hello")
    
    @staticmethod
    def add(a,b):
        return a+b
    
math = M()
print(M.add(1,2))