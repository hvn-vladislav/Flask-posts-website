import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect('sqqql.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    );
''')

cursor.execute('ALTER TABLE posts ADD author_id INTEGER;')

cursor.execute('INSERT INTO user VALUES (?,?,?)',
               (1, 'admin', generate_password_hash('123456')))

cursor.execute('UPDATE posts SET author_id = 1;')

cursor.execute('ALTER TABLE user ADD email TEXT;')
cursor.execute('UPDATE user SET email = "admin@example.com" WHERE id = "1";')

connection.commit()
connection.close()
