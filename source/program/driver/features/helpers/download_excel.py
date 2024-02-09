from urllib.request import urlretrieve
import yaml
import pandas as pd
import os
from .crknScrapper import CrknExcelExtractor
def openYaml(f_p):
    with open(f_p, "r") as stream:
        x = (yaml.safe_load(stream))
        return x['excel_links']

def downloadExcel(url):
    name_convention = url.split('/')
    file_name = name_convention[-1]
    urlretrieve(url, f'source/storage/excel/{file_name}')
def parseExcel(file):
    xfile = pd.read_excel(f'source/storage/excel/{file}', sheet_name= "PA-Rights")
    print(xfile)
    xfile.to_csv(f'source/storage/spreadsheets/{file[:-5]}.csv')

def downloadFiles():
    extractor = CrknExcelExtractor()
    excel_links = extractor.extract_excel_links()
    print("Excel Links Found:")
    print(excel_links)
    entries = os.listdir('source/storage/excel/')
    excel_files = [i for i in entries if ('xlsx' in i) and ('CRKN_EbookPARightsTracking' in i)]
    for i in excel_files:
        os.remove(f"source/storage/excel/{i}")
    print(excel_files)
    print('Removed Files!')
    for i in excel_links:
        downloadExcel(i)
    entries = os.listdir('source/storage/excel/')
    excel_files = [i for i in entries if ('xlsx' in i) and ('CRKN_EbookPARightsTracking' in i)]
    for i in excel_files:
        parseExcel(i) 