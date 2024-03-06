import sqlite3 as sq
import os
import pandas as pd

def openExcel(file):
    workbook = pd.read_excel(file, sheet_name='PA-Rights')
    workbook = pd.DataFrame(workbook)
    value = workbook.columns
    return value[0]

def access_csv(file):
  spreadsheet_csv = pd.read_csv(f'source/storage/spreadsheets/{file}', skiprows=[0,1])
  df = pd.DataFrame(spreadsheet_csv)
  df = df[df['Platform_eISBN'].notna()]
  df['Platform_eISBN'] = (df['Platform_eISBN'].apply(int).astype(str))
  return df
def singleAddition(df, cursor, platform, University, filename, man_stat):
  try:
    cursor.execute('INSERT INTO platforms (spreadsheet, platform, CRKN) VALUES(?, ?, ?)', (filename, platform, man_stat))
    print(f'SUCCESSFULL ADD OF PLATFORM {filename}')
  except sq.IntegrityError as e:

    print('Already added file previously!')
    print(str(e))
    return 0
  for row in df.iterrows():
    title = row[1]['Title']
    publisher = row[1]['Publisher']
    platform_yob = row[1]['Platform_YOP']
    ISBN = row[1]['Platform_eISBN']
    OCN = row[1]['OCN']
    result = row[1][University]
    print('ADDING ROW TO DATABASE', (title, publisher, platform_yob, ISBN, OCN, result, filename))
    try:
      cursor.execute("INSERT INTO books (title, publisher, platform_yop, ISBN, OCN, result, spreadsheet) VALUES(?, ?, ?, ?, ?, ?, ?)", 
                    (title, publisher, platform_yob, ISBN, OCN, result, filename))
    # sometimes the the same ISBN will be there twice. For now, ignore those rows.
    except sq.IntegrityError as e:
      print('FAILED ADDITION', (title, publisher, platform_yob, ISBN, OCN, result, filename))
      print(str(e))

def removeFromDatabase():
  db_path = 'source/storage/database/proj.db'
  db = sq.connect(db_path)
  cursor = db.cursor()
  cursor.execute("DELETE FROM books WHERE spreadsheet in (SELECT spreadsheet FROM platforms WHERE CRKN = 'Y')")
  cursor.execute("DELETE FROM platforms WHERE spreadsheet in (SELECT spreadsheet FROM platforms WHERE CRKN = 'Y')")
  db.commit()
  db.close()
   
def setDatabaseUni(university):
  University = university
  with open('source/sqlscripts/db_setup.sql', 'r') as sql_file:
      sql_script = sql_file.read()
  db_path = 'source/storage/database/proj.db'
  # check if the db exists first
  if os.path.isfile(db_path):
      print('Removed Old Path')
      os.remove(db_path)
  # clean csv file (should be done in another file, but done here for now)
  # using skiprows=[0,1] to skip the first two fluff lines. Not a long term solution, we have to look for something else, but this will do for now.
  entries = os.listdir('source/storage/spreadsheets/')
  csv_files = [i for i in entries if ('.csv' in i) and ('CRKN_EbookPARightsTracking' in i)]
  db = sq.connect(db_path)
  cursor = db.cursor()
  cursor.executescript(sql_script)
  for i in csv_files:
      filename =i[:-4] + '.xlsx'
      df = access_csv(i)
      try:  
        uni = df.columns.get_loc(University)
      except KeyError as e:
        print(str(e))
        print(f'Ignored {filename}. Does not include {University}')
        continue      
      db.commit()
      platform = openExcel(f'source/storage/excel/{filename}')
      singleAddition(df, cursor, platform, University, filename, 'Y')
  db.commit()
  db.close()

