class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)

    def show_books(self):
        for book in self.books:
            print(book)
            print('------')

    def search_by_title(self, title):
        for book in self.books:
            if book.title == title:
                print(book)

    def search_by_author(self, author):
        for book in self.books:
            if author in book.authors:
                print(book)

    def __str__(self):
        return f'Library: {self.name}\nAddress: {self.address}'