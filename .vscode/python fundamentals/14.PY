l = [1,2,3,4,5,6,7,8,9,10]
even = [num for num in l if num%2 == 0]
odd = [n for n in l if n%2 != 0]
print(even)
print(odd)

guest = ['a','b','c','d']
friends = ['B','D','E','F']
friendsLower = [n.lower() for n in friends]
present_friend = [
    n.title() 
    for n in guest 
    if n in  friendsLower
]
print(f" guests = {guest}")
print(f" friends = {friendsLower}")
print(f" present friend = {present_friend}")
