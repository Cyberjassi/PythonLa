import time
print(time.time())

def powers(x):
    return [x**2 for x in range(x)]

start = time.time()
powers(50000000)
end = time.time()

print(f"Our program taken time -{end - start}")