from models.author import Author
from models.book import Book

from repositories import author_repository
from repositories import book_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author("Ian M. Banks")
author2 = Author("Neil Gaiman")
author3 = Author("Terry Pratchett")
author_repository.save(author1)
author_repository.save(author2)
author_repository.save(author3)

book1 = Book("The Use of Weapons", author1, "Sci-Fi", 1990)
book2 = Book("The Player of Games", author1, "Sci-Fi", 1988)
book3 = Book("Night Watch", author3, "Fantasy", 2002)
book4 = Book("Men at Arms", author3, "Fantasy", 1993)
book5 = Book("American Gods", author2, "Horror Fiction", 2001)
book6 = Book("Stardust", author2, "Fantasy", 1999)

book_repository.save(book1)
book_repository.save(book2)
book_repository.save(book3)
book_repository.save(book4)
book_repository.save(book5)
book_repository.save(book6)