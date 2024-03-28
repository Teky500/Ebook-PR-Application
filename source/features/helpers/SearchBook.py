import sqlite3 as sq
def startConnection(db_path):
  db = sq.connect(db_path)
  return db
def searchTitle(title, db_path):
  title = title.strip()
  newTitle = ''
  for letter in title:
    if letter == '*':
      newTitle += '%'
    else:
      newTitle += letter
  db = startConnection(db_path)
  cursor = db.cursor()
  query = f"SELECT books.*, platforms.platform  FROM BOOKS JOIN PLATFORMS ON Books.spreadsheet  = platforms.spreadsheet where title LIKE ?"
  cursor.execute(query, (newTitle, ))
  result = cursor.fetchall()
  return result
def searchISBN(ISBN, db_path):
  ISBN = ISBN.strip()
  db = startConnection(db_path)
  cursor = db.cursor()
  query = f"SELECT books.*, platforms.platform  FROM BOOKS JOIN PLATFORMS ON Books.spreadsheet  = platforms.spreadsheet where ISBN = ?"
  cursor.execute(query, (ISBN, ))
  result = cursor.fetchall()
  return result
def searchOCN(OCN, db_path):
  OCN = OCN.strip()
  db = startConnection(db_path)
  cursor = db.cursor()
  query = f"SELECT books.*, platforms.platform  FROM BOOKS JOIN PLATFORMS ON Books.spreadsheet  = platforms.spreadsheet where ISBN = ?"
  cursor.execute(query, (OCN, ))
  result = cursor.fetchall()
  return result