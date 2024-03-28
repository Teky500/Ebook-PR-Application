import sqlite3 as sq
import logging
import os
import sys
# Remove a file from the database. Also removes it from the storage directories.
def removeFile(file):
    try:
        os.remove(f'source/storage/excel/{file}')
        os.remove(f'source/storage/spreadsheets/{file[:-4]}csv')
        db = sq.connect('source/storage/database/proj.db')
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM books WHERE spreadsheet = '{file}'")
        cursor.execute(f"DELETE FROM platforms WHERE spreadsheet = '{file}'")
        db.commit()
        db.close()
    except Exception as e:
        logging.critical(str(e))
        logging.critical('Something went wrong while removing the file.')
        sys.exit()
    logging.info(f'Successfully removed file with name {file}')
# Returns a list of all manually added local files.
def getFiles() -> list:
    db = sq.connect('source/storage/database/proj.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT spreadsheet FROM platforms WHERE CRKN = 'N'")
    fileList = cursor.fetchall()
    db.close()
    return fileList
