def number_upto_100():
    i = 0
    while i<100:
        yield i
        i+=1

g = number_upto_100()
print(next(g))
print(next(g))
print(list(g))
