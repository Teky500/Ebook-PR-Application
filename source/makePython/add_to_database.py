import sqlite3 as sq
import os
import pandas as pd
University = 'Univ. of Prince Edward Island'
with open('source/sqlscripts/db_setup.sql', 'r') as sql_file:
    sql_script = sql_file.read()
db_path = 'source/storage/database/proj.db'
# check if the db exists first
if os.path.isfile(db_path):
    print('Removed Old Path')
    os.remove(db_path)
# clean csv file (should be done in another file, but done here for now)
# using skiprows=[0,1] to skip the first two fluff lines. Not a long term solution, we have to look for something else, but this will do for now.
spreadsheet_csv = pd.read_csv('source/storage/spreadsheets/spreadsheet_1.csv', skiprows=[0,1])
df = pd.DataFrame(spreadsheet_csv)
df = df[df['Platform_eISBN'].notna()]
uni = df.columns.get_loc(University)
db = sq.connect(db_path)
cursor = db.cursor()
cursor.executescript(sql_script)
db.commit()
for row in df.iterrows():
  title = row[1]['Title']
  publisher = row[1]['Publisher']
  platform_yob = row[1]['Platform_YOP']
  ISBN = row[1]['Platform_eISBN']
  OCN = row[1]['OCN']
  result = row[1][University]
  print('ADDING ROW TO DATABASE', (title, publisher, platform_yob, ISBN, OCN, result))
  try:
    cursor.execute("INSERT INTO books (title, publisher, platform_yop, ISBN, OCN, result) VALUES(?, ?, ?, ?, ?, ?)", 
                   (title, publisher, platform_yob, ISBN, OCN, result))
  # sometimes the the same ISBN will be there twice. For now, ignore those rows.
  except sq.IntegrityError:
     print('FAILED ADDITION', (title, publisher, platform_yob, ISBN, OCN, result))
db.commit()
db.close()
