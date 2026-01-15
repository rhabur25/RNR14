import sqlite3

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()

query = '''
    INSERT INTO points (city,name) VALUES ('Houston','Texans');


'''

cursor.execute(query)
conn.commit()
conn.close()