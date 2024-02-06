import openpyxl 
from openpyxl.worksheet.datavalidation import DataValidation
import pandas as pd
from add_to_database import singleAddition
import sqlite3 as sq

def openExcel(file):
    workbook = pd.read_excel(file, sheet_name='PA-Rights')
    workbook = pd.DataFrame(workbook)
    value = workbook.columns
    return value[0]
def validate_headers(file):
    # Create the workbook and worksheet we'll be working with
    file = f"source/storage/excel/{file}"
    wb = openpyxl.load_workbook(file)
    ws = wb["PA-Rights"]

    valid_header = True
    error_message = []

    headers = '"Title, Publisher, Platform_YOP, Platform_eISBN, OCN, agreement_code, collection_name, title_metadata_last_modified"'
    #Create a data-validation object with list validation

    dv = DataValidation(type="list", formula1=headers, allow_blank=False)


    cellDictionairy = {
                        "A3" : "Title",
                        "B3": "Publisher",
                        "C3": "Platform_YOP", #int
                        "D3": "Platform_eISBN", #int
                        "E3": "OCN",            #int
                        "F3": "agreement_code",
                        "G3": "collection_name",
                        "H3": "title_metadata_last_modified" #date
    }


    cellKeys = list(cellDictionairy.keys())
    cellValues = list(cellDictionairy.values())
    for i in range(len(cellDictionairy)):


        cell = cellKeys[i]
        cell_field = ws[cell]
        dv.add(cell_field)

        correct_value = cellValues[i]

        if cell_field.value.upper() != correct_value.upper():
            error_message.append("Invalid header: Set cell " + cell + " to " + correct_value)
        
    print
    if len(error_message) != 0:
        valid_header = False
        print(error_message)
        return error_message
    print("Success")
    return []

    dv.showInputMessage = True
    dv.showErrorMessage = True
    ws.add_data_validation(dv)

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

def man_upload(file, University):
    if validate_headers(file) == []:
        if parseExcelManual(file) == 1:
            filename = file
            file = file[:-5]
            db = sq.connect('source/storage/database/proj.db')
            cursor = db.cursor()
            df = access_csv(file)
            try:
                uni = df.columns.get_loc(University)
            except KeyError as e:
                print(str(e))
                print(f'Ignored {filename}. Does not include {University}')
                return 0
            singleAddition(df, cursor, 'MANUAL', University, filename)
            db.commit()
            db.close()
        else:
            print("doesn't work")
    else:
        print('invalid')

def access_csv(file):
  spreadsheet_csv = pd.read_csv(f'source/storage/spreadsheets/{file}.csv', skiprows=[0,1])
  df = pd.DataFrame(spreadsheet_csv)
  df = df[df['Platform_eISBN'].notna()]
  df['Platform_eISBN'] = (df['Platform_eISBN'].apply(int).astype(str))
  return df

