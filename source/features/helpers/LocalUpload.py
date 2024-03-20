import pandas as pd
from .DatabaseManager import single_addition
import sqlite3 as sq
from .FileValidate import FileTemplate, FileValidator
import yaml
import shutil
import os

def open_excel(file_path):
    workbook = pd.read_excel(file_path, sheet_name='PA-Rights')
    value = workbook.columns
    return value[0]

def parse_excel_manual(file_path):

    excel_file_path = f'source/storage/excel/{file_path}'
    csv_file_path = f'source/storage/spreadsheets/{os.path.splitext(file_path)[0]}.csv'

    try:
        excel_data = pd.read_excel(excel_file_path, sheet_name="PA-Rights")
        print(excel_data)
        excel_data.to_csv(csv_file_path, index=False)
        return 1
    except Exception as e:
        print(f"Error occurred while parsing Excel file: {str(e)}")
        return 0

def man_upload(file_path):
    template = FileTemplate(file_path)
    validator = FileValidator(template)

    if validator.is_valid_file():
        file_name = os.path.basename(file_path)
        shutil.copyfile(file_path, f'source/storage/excel/{file_name}')
        platform = open_excel(file_path)
        if parse_excel_manual(file_name) == 1:
            filename = file_name
            file_name = file_name[:-5]
            db = sq.connect('source/storage/database/proj.db')
            cursor = db.cursor()
            df = access_csv(file_name)

            with open('source/config/config.yaml', 'r') as config_file:
                yaml_file = yaml.safe_load(config_file)
                university_column = yaml_file['University']
            if df[university_column].isnull().values.any():
                return ['Null value found in University Column!']
            if single_addition(df, cursor, platform, university_column, filename, 'N') == 0:
                return ['Already Added File!']
            db.commit()
            db.close()
            return []
        else:
            print("Something went wrong while parsing the excel file.")
            return ['Something went wrong!']
    else:
        print('Invalid File!')
        print(validator.get_error_message())
        return validator.get_error_message()
    
def access_csv(file_path):
  spreadsheet_csv = pd.read_csv(f'source/storage/spreadsheets/{file_path}.csv', skiprows=[0,1])
  df = pd.DataFrame(spreadsheet_csv)
  df = df[df['Platform_eISBN'].notna()]
  df['Platform_eISBN'] = (df['Platform_eISBN'].apply(int).astype(str))
  return df

