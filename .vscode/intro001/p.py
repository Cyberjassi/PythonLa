# 1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.

# 3) Below you’ll find a short list of quotes:

#  quotes = [
#     "'What a waste my life would be without all the beautiful mistakes I've made.'",
#     "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
#     "'The very essence of romance is uncertainty.'",
#     "'We are not here to do what has already been done.'"
#  ]

# Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, extract the text from each string, without these extra quote marks, and print each quote.

# You may also want to try a solution using strip.

# 4) Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input, so you’re going to have to process the string before you find its length.

# If you want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them how many how many characters are in the text overall, and you can also provide them a word count.

# You can find our solutions to the exercises here.

# name = input("Enter your full name")
# first_split = name.split(" ")
# print(first_split)
# first = first_split[0]
# sername = first_split[1]
# print(f"Your name is {first} and sername is {sername}")

# 2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.
# li = [1,2,3,4,5]
# str = " | ".join(map(str, li))
# print(str)

list = []
dic = {"title":"abc","director":"asjkfh"}
list.append(dic)
print(list)