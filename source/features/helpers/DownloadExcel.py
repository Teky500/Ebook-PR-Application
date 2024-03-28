from urllib.request import urlretrieve
import yaml
import pandas as pd
import os
from .CrknScrapping import CrknExcelExtractor
import logging
import ssl
import sys
def openYaml(f_p):
    with open(f_p, "r") as stream:
        x = (yaml.safe_load(stream))
        return x['excel_links']

def downloadExcel(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    name_convention = url.split('/')
    file_name = name_convention[-1]
    try:
        urlretrieve(url, f'source/storage/excel/{file_name}')
    except Exception as e:
        logging.critical(f'{file_name}')
        logging.critical('Failed to fetch file content. Are you still connected to the internet?')
        sys.exit()
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
def updateConfig():
    extractor = CrknExcelExtractor()
    links = extractor.extractExcelLinks()
    logging.info('NEW CONFIG LINKS')
    logging.info(links)
    with open('source/config/config.yaml', 'r') as config_file:
        yaml_file = yaml.safe_load(config_file)
        yaml_file['excel_links'] = links
    with open('source/config/config.yaml', 'w') as config_file:
        yaml.dump(yaml_file, config_file)