import sqlite3

with open('code/sqlscripts/cdb.sql', 'r') as sql_file:
    sql_script = sql_file.read()

db = sqlite3.connect('code/storage/tests/test.db')
cursor = db.cursor()
cursor.executescript(sql_script)
db.commit()
db.close()