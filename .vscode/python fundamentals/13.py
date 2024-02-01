number = [1,2,3]
doubled_number = [n*2 for n in number]
print(number)
print(doubled_number)



doubled_number = [n*3 for n in range(5)]
print(doubled_number)

age = [12,34,23,56,43,57]
age_string = [f"My friend is {a} years old." for a in age]
print(age_string)

friend = input("enter the friend name ")
friends  = ['Jatin','Kishore','Satya']
friends_lower = [name.lower() for name in friends]
if friend.lower() in friends_lower:
    print(f"{friend} is present in friends")




