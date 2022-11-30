from flask import render_template, redirect, Blueprint
from repositories import author_repository, book_repository
# from models.book import Book

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route('/books')
def books():
    all_books = book_repository.select_all()
    return render_template('books/index.html', all_books)



