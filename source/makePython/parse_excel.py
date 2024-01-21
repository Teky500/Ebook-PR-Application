import pandas as pd
def parse_excel():
    xfile = pd.read_excel('source/storage/spreadsheets/spreadsheet_1.xlsx', sheet_name= "PA-Rights")
    print(xfile)
    xfile.to_csv('source/storage/spreadsheets/spreadsheet_1.csv')