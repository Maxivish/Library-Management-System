# models.py
from database import get_db

class Book:
    @staticmethod
    def create(title, author, year):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all(limit, offset):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books LIMIT ? OFFSET ?", (limit, offset))
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def get_by_id(book_id):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book

    @staticmethod
    def update(book_id, title, author, year):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET title=?, author=?, year=? WHERE id=?", (title, author, year, book_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(book_id):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def search_by_title_or_author(query, limit, offset):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? LIMIT ? OFFSET ?", 
                       (f'%{query}%', f'%{query}%', limit, offset))
        books = cursor.fetchall()
        conn.close()
        return books


class Member:
    @staticmethod
    def create(name, email):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all(limit, offset):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members LIMIT ? OFFSET ?", (limit, offset))
        members = cursor.fetchall()
        conn.close()
        return members
