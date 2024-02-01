# Welcome back to another coding exercise solutionI hope it went well!

# This is my solution to the coding exercise. Again, it may be slightly different from yours!

# # Ask the user to choose one of two options:
# # if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# # if they type 'q', our program should terminate.

# # Let's begin by asking the user to type either 'p' or 'q':
# user_input = input("Enter q or p: ")

# # Now we must repeat until they type 'q':
# while user_input != "q":
#     # Inside our loop, check if they typed 'p'. If they did, print "Hello"
#     if user_input == "p":
#         print("Hello")
#     # Now we must ask the user for their input againotherwise we would be in an infinite loop!
#     user_input = input("Enter q or p: ")
# Let me know how you got on!

# Kind regards,

# Jose and the Teclado team

is_true = True
while is_true:
    print("Hello")
    user_i = input("choose (p/q)")
    is_true = user_i == 'p'
    
    
    
