import sqlite3 as sq
def start_connection(db_path):
  db = sq.connect(db_path)
  return db
def search_title_substring(title, db_path):
  db = start_connection(db_path)
  cursor = db.cursor()
  cursor.execute(f"SELECT * FROM books where title LIKE '%{title}%'")
  result = cursor.fetchall()
  return result
def search_ISBN(ISBN, db_path):
  db = start_connection(db_path)
  cursor = db.cursor()
  cursor.execute(f"SELECT * FROM books where ISBN = '{ISBN}'")
  result = cursor.fetchall()
  return result
def search_OCN(OCN, db_path):
  db = start_connection(db_path)
  cursor = db.cursor()
  cursor.execute(f"SELECT * FROM books where OCN = '{OCN}'")
  result = cursor.fetchall()
  return result