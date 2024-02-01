car = ['ok','ok','ok','not','ok','ok']
for status in car:
    if(status=='not'):
        break
    print(f"This car is {status}")
print("skip this car...\n")

car = ['ok','ok','ok','not','ok','ok']
for status in car:
    if(status=='not'):
        continue
    print(f"This car is {status}")
print("skip this car...")