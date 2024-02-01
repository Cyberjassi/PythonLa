guest = ['a','b','c','d','b','d']
friends = ['B','D','E','F']
friends_lower = {
    n.lower()
    for n in friends
}
present_friend = {
    n.title()
    for n in friends_lower.intersection(guest)
}
print(f"guest = {guest}")
print(f"friend = {friends_lower}")
print(f"present friends = {present_friend}")


friends  = ['A','B','C','D','E']
age = [12,34,33,67,46]
merge = {
    friends[i] : age[i]
    for i in range(len(friends))
}
print(merge)


friends  = ['A','B','C','D','E','a','e','r','f','t','g']
age = [12,3,3,7,46,76,5,6,5,6,9]
merge = {
    friends[i] : age[i]
    for i in range(len(friends))
    if age[i]>18
}
print(merge)

