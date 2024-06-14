import sqlite3
import hashlib


DB_NAME = "database.db"
conn = sqlite3.connect(DB_NAME)

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT NOT NULL, lastname TEXT NOT NULL, username TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL, user_logo BLOB NOT NULL )")

conn.commit()