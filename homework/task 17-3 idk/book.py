class Book:
    def __init__(self, title, authors, year):
        self.title = title
        self.authors = authors
        self.year = year

    def __str__(self):
        return f'Title: {self.title}\nAuthors: {self.authors}\nYear: {self.year}'