import sqlite3 as sq

def remove_file(file_name):
    db = sq.connect('source/storage/database/proj.db')
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM books WHERE spreadsheet = '{file_name}'")
    cursor.execute(f"DELETE FROM platforms WHERE spreadsheet = '{file_name}'")
    db.commit()
    db.close()
    print(f'Successfully removed file with name {file_name}')

def get_files():
    db = sq.connect('source/storage/database/proj.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT spreadsheet FROM platforms WHERE CRKN = 'N'")
    fileList = cursor.fetchall()
    db.close()
    return fileList
