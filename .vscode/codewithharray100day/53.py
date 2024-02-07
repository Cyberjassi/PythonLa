from functools import reduce

# # Map
# cube = lambda x:x*x*x
# li = [2,4,3,5,7,6,56]
# newl = list(map(cube,li))
# print(newl)

# short_l = list(map(lambda x:x*x,li))
# print(short_l)



# # Filer
# def filter_f(x):
#     return x>4
# newlist = list(filter(filter_f,li))
# print(newlist)


# Reduce
li = [1,2,3,4,5]
red = reduce(lambda x,y:x+y,li)
print(red)

