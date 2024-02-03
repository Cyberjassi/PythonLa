class Library:
    books = []

    def __init__(self):
        self.books
    def add(self,book):
        self.books.append(book)
    def show(self):
        print(self.books)
    def howmany(self):
        print(len(self.books))

me = Library()
me.add('a')
me.add('b')
me.add('c')
me.add('d')

me.show()
me.howmany()



