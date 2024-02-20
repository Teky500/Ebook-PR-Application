import sqlite3 as sq
def removeFile(rFilename):
    db = sq.connect('source/storage/database/proj.db')
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM books WHERE spreadsheet = '{rFilename}'")
    cursor.execute(f"DELETE FROM platforms WHERE spreadsheet = '{rFilename}'")
    db.commit()
    db.close()

def getFiles():
    db = sq.connect('source/storage/database/proj.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM platforms")
    fileList = db.fetchall()
    db.close()
    return fileList
