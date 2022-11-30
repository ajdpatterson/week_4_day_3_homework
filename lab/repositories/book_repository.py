from db.run_sql import run_sql

from models.book import Book
from repositories import author_repository

def save(book):
    sql = "INSERT INTO books (title, genre, year_published, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.year_published, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        book = Book(row["title"], row["author"], row["genre"], row["year_published"], row["id"])
        books.append(book)
    return books