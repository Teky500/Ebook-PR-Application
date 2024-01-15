import sqlite3 as sl
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sl.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT * from users")
        results = cur.fetchall()
        print(results)
        conn.close()
    except Exception as e:
        print('FAILED', e)

if __name__ == '__main__':
    create_connection("code/storage/tests/test.db")