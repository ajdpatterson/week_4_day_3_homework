DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS books;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  author_name VARCHAR(255)
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  author VARCHAR(255),
  genre VARCHAR(255),
  year_published INT,
  author_id INT NOT NULL REFERENCES authors(id)
);