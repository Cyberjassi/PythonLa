def add(x,y = 3):
    return x+y

print(add(x=3,y=7))



print(1,2,3,4,sep='-')



default = 3
def add(x,y = default):
    print(x+y)

add(3)