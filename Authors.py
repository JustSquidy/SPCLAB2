
class Author: 
    # This is for names, and the list of books 
    def __init__(self, name, books=None):
        self.name = name
        self.books = []

    def publish(self, title):
        if title in self.books: # This checks the list for a duplicate book title and gives a message if already published.
            print(f'\nThe book "{title}" is already published by {self.name}.\n')
        else:
            self.books.append(title)

    def __str__ (self): # joins the books and returns a list of the authors book and their name.
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = "None"
        return f'Name: {self.name}. Books published: {book_list}'

    def main():
        Tatsuki_Fujimoto = Author("Tatsuki Fujimoto")
        Tatsuki_Fujimoto.publish("Chainsaw Man")
        Tatsuki_Fujimoto.publish("Fire Punch")
        Tatsuki_Fujimoto.publish("Look Back")
        Tatsuki_Fujimoto.publish("Look Back") # Testing duplicate book publishing
        print(Tatsuki_Fujimoto)

        Javier = Author("Javier Reyes")
        print(Javier)

if __name__ == "__main__":
    Author.main()