print(bool(0))
print(bool(12))
print(bool(""))
print(bool([]))
print(bool("[3,3]"))


default_greeting = "There"
name = input("enter your name:(optional)")
user_name = name or default_greeting
print(f"Hello , {user_name}")