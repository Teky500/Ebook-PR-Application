import openpyxl 
from openpyxl.worksheet.datavalidation import DataValidation
import pandas as pd
from .add_to_database import singleAddition
import sqlite3 as sq
from .fileValidate import FileTemplate, FileValidator
import yaml
import shutil
import os

def openExcel(file):
    workbook = pd.read_excel(file, sheet_name='PA-Rights')
    workbook = pd.DataFrame(workbook)
    value = workbook.columns
    return value[0]

def parseExcelManual(file):
    try:
        xfile = pd.read_excel(f'source/storage/excel/{file}', sheet_name= "PA-Rights")
    except Exception as e:
        print(str(e))
        print('FAILED')
        return 0
    print(xfile)
    xfile.to_csv(f'source/storage/spreadsheets/{file[:-5]}.csv')
    return 1

def man_upload(file):
    f = FileTemplate(file)
    V = FileValidator(f)
    if V.validFile():
        file_name = os.path.basename(file)
        shutil.copyfile(file, f'source/storage/excel/{file_name}')
        platform = openExcel(file)
        if parseExcelManual(file_name) == 1:
            filename = file_name
            file_name = file_name[:-5]
            db = sq.connect('source/storage/database/proj.db')
            cursor = db.cursor()
            df = access_csv(file_name)

            with open('source/config/config.yaml', 'r') as config_file:
                yaml_file = yaml.safe_load(config_file)
                University = yaml_file['University']
            if df[University].isnull().values.any():
                return ['Null value found in University Column!']
            sAddResult =  singleAddition(df, cursor, platform, University, filename, 'N')
            if sAddResult == 0:
                return ['Already Added File!']
            else:
                db.commit()
                db.close()
                return [sAddResult[1]]
        else:
            print("Something went wrong while parsing the excel file.")
            return ['Something went wrong!']
    else:
        print('Invalid File!')
        print(V.getErrorMessage())
        return V.getErrorMessage()
def access_csv(file):
  spreadsheet_csv = pd.read_csv(f'source/storage/spreadsheets/{file}.csv', skiprows=[0,1])
  df = pd.DataFrame(spreadsheet_csv)
  df = df[df['Platform_eISBN'].notna()]
  df['Platform_eISBN'] = (df['Platform_eISBN'].apply(int).astype(str))
  return df

