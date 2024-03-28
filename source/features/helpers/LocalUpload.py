import openpyxl
import logging
from openpyxl.worksheet.datavalidation import DataValidation
import pandas as pd
from .DatabaseManagement import singleAddition
import sqlite3 as sq
from .FileValidator import FileTemplate, FileValidator
import yaml
import shutil
import os
from .getLanguage import getLanguage
import sys
# Open excel file, and returns the platform name in cell A1.
def openExcel(file) -> str:
    try:
        workbook = pd.read_excel(file, sheet_name='PA-Rights')
        workbook = pd.DataFrame(workbook)
        reqSheet = workbook.columns
        return reqSheet[0]
    except Exception as e:
        logging.info(file)
        logging.critical(str(e))
        logging.critical('Failed to open excel file to get platform.')

# Parse the excel file. Returns an Integer to confirm the parse status, and adds a CSV file to `source/storage/spreadsheets`.
def parseExcelManual(file):
    try:
        # Excel files are stored in `source/storage/excel`.
        excelFile = pd.read_excel(f'source/storage/excel/{file}', sheet_name= "PA-Rights")
    except Exception as e:
        logging.info(file)
        logging.critical(str(e))
        logging.critical('Failed to parse the excel file into CSV.')
        sys.exit()
    logging.info(excelFile)
    excelFile.to_csv(f'source/storage/spreadsheets/{file[:-5]}.csv')
    return 1
# Local file upload functionality. Returns a list of errors or numbers that are later mapped to errors.
def localFileUpload(file) -> list:
    fileTemplate = FileTemplate(file)
    validator = FileValidator(fileTemplate)
    if validator.validFile():
        baseFileName = os.path.basename(file)
        shutil.copyfile(file, f'source/storage/excel/{baseFileName}')
        platform = openExcel(file)
        if parseExcelManual(baseFileName) == 1:
            fileNameWithExtension = baseFileName
            baseFileName = baseFileName[:-5]
            db = sq.connect('source/storage/database/proj.db')
            cursor = db.cursor()
            df = accessCSV(baseFileName)

            with open('source/config/config.yaml', 'r') as config_file:
                yaml_file = yaml.safe_load(config_file)
                University = yaml_file['University']
            # Check for null values in University column.
            if df[University].isnull().values.any():
                db.close()
                if getLanguage() == 1:
                    os.remove(f'source/storage/excel/{baseFileName}.xlsx')
                    os.remove(f'source/storage/spreadsheets/{baseFileName}.csv')
                    return ['Valeur nulle trouvée dans la colonne Université']
                else:
                    os.remove(f'source/storage/excel/{baseFileName}.xlsx')
                    os.remove(f'source/storage/spreadsheets/{baseFileName}.csv')
                    return ['University column is blank for one or more rows.']
            # Add to database, and if the addition result is 0, the file was already here previously.    
            sAddResult =  singleAddition(df, cursor, platform, University, fileNameWithExtension, 'N')
            if sAddResult == 0:
                db.close()
                if getLanguage() == 1:
                    return ['Fichier déjà ajouté']
                else:
                    return ['Already Added File!']
            else:
                db.commit()
                db.close()
                return ['Y', sAddResult[1]]
        else:
            logging.critical(file)
            logging.critical("Something went wrong while parsing the excel file.")
            sys.exit()

            
    else:
        logging.info('Invalid File!')
        logging.info(validator.getErrorMessage())
        return validator.getErrorMessage()
# Access the CSV file and return a DataFrame with only the data without the platform.
def accessCSV(file) -> pd.DataFrame:
  spreadsheet_csv = pd.read_csv(f'source/storage/spreadsheets/{file}.csv', skiprows=[0,1])
  df = pd.DataFrame(spreadsheet_csv)
  # Remove any NA ISBN, and turn ISBN to strings and strip them of decimals.
  try:
    df = df[df['Platform_eISBN'].notna()]
    df['Platform_eISBN'] = (df['Platform_eISBN'].apply(int).astype(str))
  except Exception as e:
      logging.critical(str(e))
      logging.critcal('Failed to parse ISBN column.')
      sys.exit()
  return df

