class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return "Book borrowed successfully"
        else:
            return "Book is currently unavailable"

    def return_book(self):
        self.available = True
        return "Book returned successfully"

book = Book("1984", "George Orwell")

print(book.return_book())