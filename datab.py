import sqlite3

conn = sqlite3.connect('chatbot_data.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS questions (id INTEGER Auto Increment PRIMARY KEY,question TEXT)''')

# cursor.execute('''INSERT INTO questions VALUES (3,'biet')''')

conn.commit()
# cursor.execute('delete from questions')
cursor.execute('SELECT * FROM questions')

print(cursor.fetchall())