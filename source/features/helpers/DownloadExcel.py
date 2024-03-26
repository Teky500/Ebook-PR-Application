from urllib.request import urlretrieve
import yaml
import pandas as pd
import os
from .CrknScrapping import CrknExcelExtractor
import logging
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
    logging.info(xfile)
    xfile.to_csv(f'source/storage/spreadsheets/{file[:-5]}.csv')

def downloadFiles():
    extractor = CrknExcelExtractor()
    excel_links = extractor.extractExcelLinks()
    logging.info("Excel Links Found:")
    logging.info(excel_links)
    if excel_links == []:
        return False
    entries = os.listdir('source/storage/excel/')
    excel_files = [i for i in entries if ('xlsx' in i) and ('CRKN_EbookPARightsTracking' in i)]
    for i in excel_files:
        os.remove(f"source/storage/excel/{i}")
    csv_files = [i for i in entries if ('csv' in i) and ('CRKN_EbookPARightsTracking' in i)]
    for i in csv_files:
        os.remove(f"source/storage/csv/{i}")
    logging.info(excel_files)
    logging.info('Removed Files!')
    for i in excel_links:
        downloadExcel(i)
    entries = os.listdir('source/storage/excel/')
    excel_files = [i for i in entries if ('xlsx' in i) and ('CRKN_EbookPARightsTracking' in i)]
    for i in excel_files:
        parseExcel(i) 
    return True