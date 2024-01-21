import sqlite3 as sq
import os
import pandas as pd
University = 'Univ. of Prince Edward Island'
with open('source/sqlscripts/newdb.sql', 'r') as sql_file:
    sql_script = sql_file.read()
db_path = 'source/storage/tests/database/proj.db'
# check if the db exists first
if os.path.isfile(db_path):
    os.remove(db_path)
# clean csv file (should be done in another file, but done here for now)
# using skiprows=[0,1] to skip the first two fluff lines. Not a long term solution, we have to look for something else, but this will do for now.
spreadsheet_csv = pd.read_csv('source/spreadsheets/spreadsheet_1.csv', skiprows=[0,1])
df = pd.DataFrame(spreadsheet_csv)
db = sq.connect(db_path)
cursor = db.cursor()
cursor.executescript(sql_script)
db.commit()
for row in df.iterrows():
  print(row)
  title = row['Title']
  publisher = row['Publisher']
  platform_yob = row['Platform_YOP']
  ISBN = row['Platform_eISBN']
  OCN = row['OCN']
  result = row[University]
  cursor.execute(f'INSERT INTO books (title, publisher, platform_yob, ISBN, OCN, result) VALUES ({title}, {publisher}, {platform_yob}, {ISBN}, {OCN}, {result});')
db.close()