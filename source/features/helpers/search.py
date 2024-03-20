import sqlite3 as sq
def start_connection(db_path):
  db = sq.connect(db_path)
  return db
def search_title_substring(title, db_path):
  title = title.strip()
  newtitle = ''
  for lt in title:
    if lt == '*':
      newtitle += '%'
    else:
      newtitle += lt
  db = start_connection(db_path)
  cursor = db.cursor()
  cursor.execute(f"SELECT books.*, platforms.platform  FROM BOOKS JOIN PLATFORMS ON Books.spreadsheet  = platforms.spreadsheet where title LIKE '{newtitle}'")
  result = cursor.fetchall()
  return result
def search_ISBN(ISBN, db_path):
  ISBN = ISBN.strip()
  db = start_connection(db_path)
  cursor = db.cursor()
  cursor.execute(f"SELECT books.*, platforms.platform  FROM BOOKS JOIN PLATFORMS ON Books.spreadsheet  = platforms.spreadsheet where ISBN = '{ISBN}'")
  result = cursor.fetchall()
  return result
def search_OCN(OCN, db_path):
  OCN = OCN.strip()
  db = start_connection(db_path)
  cursor = db.cursor()
  cursor.execute(f"SELECT books.*, platforms.platform FROM BOOKS JOIN PLATFORMS ON Books.spreadsheet  = platforms.spreadsheet where OCN = '{OCN}'")
  result = cursor.fetchall()
  return result