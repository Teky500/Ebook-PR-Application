import sqlite3 as sq
import logging
def removeFile(rFilename):
    db = sq.connect('source/storage/database/proj.db')
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM books WHERE spreadsheet = '{rFilename}'")
    cursor.execute(f"DELETE FROM platforms WHERE spreadsheet = '{rFilename}'")
    db.commit()
    db.close()
    logging.info(f'Successfully removed file with name {rFilename}')

def getFiles():
    db = sq.connect('source/storage/database/proj.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT spreadsheet FROM platforms WHERE CRKN = 'N'")
    fileList = cursor.fetchall()
    db.close()
    return fileList
