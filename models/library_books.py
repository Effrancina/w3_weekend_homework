from models.book import Book

book1 = Book("The city we became", "N.K. Jemisin", "Sci-Fi")
book2 = Book("Between the world and me", "Ta-Nehisi Coates", "Non-fiction")
book3 = Book("Iron widow", "Xiran Jay Zhao", "Fantasy")
book4 = Book("Catch and kill", "Ronan Farrow", "Non-fiction")
book5 = Book("Memorial", "Bryan Washington", "Fiction")

books_list = [book1, book2, book3, book4, book5]


def add_new_book(book):
    books_list.append(book)