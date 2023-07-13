class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False

    def borrow_book(self):
        self.borrowed = True

    def return_book(self):
        self.borrowed = False

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)
        print("Borrowed:", "Yes" if self.borrowed else "No")

# Example
book1 = Book("Transformers", "K.N Ombongi", 2023)
book1.display_info()  # Display book information

book1.borrow_book()  # Borrow the book
book1.display_info()  # Display updated information

book1.return_book()  # Return the book
book1.display_info()  # Display updated information
