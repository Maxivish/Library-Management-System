# database.py
import sqlite3
from config import Config

def init_db():
    conn = sqlite3.connect(Config.DATABASE_URI[10:])
    cursor = conn.cursor()

    # Create the tables for Books and Members
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        year INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE)''')

    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(Config.DATABASE_URI[10:])
    return conn
