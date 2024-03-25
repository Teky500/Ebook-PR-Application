import sqlite3 as sq
import os
import pandas as pd
import logging
def openExcel(file):
    workbook = pd.read_excel(file, sheet_name='PA-Rights')
    workbook = pd.DataFrame(workbook)
    value = workbook.columns
    return value[0]
def access_csv(file):
  spreadsheet_csv = pd.read_csv(f'source/storage/spreadsheets/{file}', skiprows=[0,1])
  df = pd.DataFrame(spreadsheet_csv)
  try:
    df = df[df['Platform_eISBN'].notna()]
    df['Platform_eISBN'] = (df['Platform_eISBN'].apply(int).astype(str))
  except Exception as e:
    logging.info('ERROR FORMING DATAFRAME')
    logging.info(e)

  return df
def singleAddition(df, cursor, platform, University, filename, man_stat):
  try:
    cursor.execute('INSERT INTO platforms (spreadsheet, platform, CRKN) VALUES(?, ?, ?)', (filename, platform, man_stat))
    logging.info(f'SUCCESSFULL ADD OF PLATFORM {filename}')
  except sq.IntegrityError as e:

    logging.info('Already added file previously!')
    logging.info(str(e))
    return 0
  counter = 0
  for row in df.iterrows():
    title = row[1]['Title']
    publisher = row[1]['Publisher']
    platform_yob = row[1]['Platform_YOP']
    ISBN = row[1]['Platform_eISBN']
    OCN = row[1]['OCN']
    result = row[1][University]
    logging.info(f'ADDING ROW TO DATABASE: {row[0] + 4}')
    try:
      cursor.execute("INSERT INTO books (title, publisher, platform_yop, ISBN, OCN, result, spreadsheet) VALUES(?, ?, ?, ?, ?, ?, ?)", 
                    (title, publisher, platform_yob, ISBN, OCN, result, filename))
      counter += 1
    # sometimes the the same ISBN will be there twice. For now, ignore those rows.
    except sq.IntegrityError as e:
      logging.info(f'FAILED ADDITION: {str([title, publisher, platform_yob, ISBN, OCN, result, filename])}')
      logging.info(str(e))
  return (1, counter)

def removeFromDatabase():
  for i in os.listdir('source/storage/excel'):
    if 'CRKN_EbookPARightsTracking' in i:
      os.remove(f'source/storage/excel/{i}')
  for i in os.listdir('source/storage/spreadsheets'):
    if 'CRKN_EbookPARightsTracking' in i:
      os.remove(f'source/storage/spreadsheets/{i}')
  db_path = 'source/storage/database/proj.db'
  db = sq.connect(db_path)
  cursor = db.cursor()
  cursor.execute("DELETE FROM books WHERE spreadsheet in (SELECT spreadsheet FROM platforms WHERE CRKN = 'Y')")
  cursor.execute("DELETE FROM platforms WHERE spreadsheet in (SELECT spreadsheet FROM platforms WHERE CRKN = 'Y')")
  db.commit()
  db.close()
   
def setDatabaseUni(university):
  University = university
  db_path = 'source/storage/database/proj.db'
  # check if the db exists first
  if os.path.isfile(db_path):
      logging.info('Removed Old Path')
      os.remove(db_path)
  # clean csv file (should be done in another file, but done here for now)
  # using skiprows=[0,1] to skip the first two fluff lines. Not a long term solution, we have to look for something else, but this will do for now.
  entries = os.listdir('source/storage/spreadsheets/')
  csv_files = [i for i in entries if ('.csv' in i) and ('CRKN_EbookPARightsTracking' in i)]
  db = sq.connect(db_path)
  cursor = db.cursor()
  cursor.executescript("""CREATE TABLE books 
    (ISBN text NOT NULL, 
    title text NOT NULL, 
    publisher text NOT NULL, 
    platform_yop int, 
    OCN int, 
    result text NOT NULL,
    spreadsheet text NOT NULL);
CREATE TABLE platforms 
    (spreadsheet text PRIMARY KEY,
    platform text NOT NULL,
    CRKN text NOT NULL);

""")
  for i in csv_files:
      filename =i[:-4] + '.xlsx'
      df = access_csv(i)
      try:  
        uni = df.columns.get_loc(University)
      except KeyError as e:
        logging.info(str(e))
        logging.info(f'Ignored {filename}. Does not include {University}')
        continue      
      db.commit()
      platform = openExcel(f'source/storage/excel/{filename}')
      singleAddition(df, cursor, platform, University, filename, 'Y')
  db.commit()
  db.close()

