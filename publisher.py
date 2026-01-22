class Author: 
    # This is for names, and the list of books 
    def __init__(self, name, email):
        self.name = name
        self.books = []

    def publisher(self, book_name):
        self.books.append(book_name)



    def main():
        a = Author('Alice')
        b = Author('Bob')

        print (a.name)  # Output: Alice
        print (b.name)  # Output: Bob

        a.publisher('First Book')
        a.publisher('Second Book')

        print (a.books)  # This prints Alice's books
        print (b.books)  # This prints bob's empty book list

