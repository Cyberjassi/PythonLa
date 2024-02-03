# Welcome back to another coding exercise solution!

# This is my solution to the coding exercise. Again, it may be slightly different from yours!

# """
# for the function below, add your code in appropriate place that checks the input n.
# n should be a non-negative integer, otherwise a ValueError should be raised
# and a proper error message should be provided informing the user of the error
# for simplicity, you may assume that the input is always an integer for this exercise
# """

# def count_from_zero_to_n(n):
#     if n < 0:
#         raise ValueError('Input should be a non-negative integer')
#     for x in range(0, n+1):
#         print(x)
# Let me know how you got on!

# Kind regards,

# Jose and the Teclado team

def count(n):
    if n<=0:
        raise ValueError('Input should be greater then 0:')
    for i in range(0,n+1):
        print(i)

count(0)