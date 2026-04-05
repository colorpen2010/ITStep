from library import *
from book import *

library = Library('Central Library', 'Main street')

while True:
    print('\n1 - Add book')
    print('2 - Show books')
    print('3 - Remove book')
    print('4 - Search by title')
    print('5 - Search by author')
    print('0 - Exit')

    choice = input('Choose: ')

    if choice == '1':
        title = input('Title: ')
        authors = input('Authors: ')
        year = input('Year: ')

        book = Book(title, authors, year)
        library.add_book(book)

    elif choice == '2':
        library.show_books()

    elif choice == '3':
        title = input('Title: ')
        library.remove_book(title)

    elif choice == '4':
        title = input('Title: ')
        library.search_by_title(title)

    elif choice == '5':
        author = input('Author: ')
        library.search_by_author(author)

    elif choice == '0':
        break