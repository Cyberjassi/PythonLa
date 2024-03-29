from utils import databas


    
USER_CHOICE = """
-'a' to add a new book
-'l' to list all book
-'r' to make a  book as read
-'d' to delete a book
-'q' to quit
"""
def menu():
    user_input = input(USER_CHOICE)
    while True:
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
           prompt_read_book()
        elif user_input == 'd':
           prompt_delete_book()
        elif user_input == 'q':
            break
        else:
            print("Unknow command. Please try again")
    
 
        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input('Enter the new book name ')
    author = input('Enter the new book author ')
    databas.add_book(name,author)

def prompt_delete_book():
    name = input('Which book want you delete: ')
    databas.delete_book(name)

def list_books():
    books = databas.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']},read: {read}")

def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')
    databas.mark_book_as_read(name)
    
menu()




