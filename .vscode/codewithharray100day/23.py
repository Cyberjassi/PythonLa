l1 = [0,1,2,3]
l2 = l1
l2[0] = 1
print(l1)


l1 = [0,1,2,3]
l2 = l1.copy()
l2[0] = 1
print(l1)
print(l2)

l1 = [1,2,3]
l2 = [4,5,6]
l1.insert(1,123);
l1.insert(0,321)
print(l1)

l1.extend(l2)
print(l1)


l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2
print(l3)