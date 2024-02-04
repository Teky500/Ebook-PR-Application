from urllib.request import urlretrieve
import yaml
import pandas as pd
import os
def openYaml(f_p):
    with open(f_p, "r") as stream:
        x = (yaml.safe_load(stream))
        return x['excel_links']
link_list = openYaml("source/config/config.yaml")
def downloadExcel(url):
    name_convention = url.split('/')
    file_name = name_convention[-1]
    urlretrieve(url, f'source/storage/spreadsheets/{file_name}')
def parseExcel(file):
    xfile = pd.read_excel(f'source/storage/spreadsheets/{file}', sheet_name= "PA-Rights")
    print(xfile)
    xfile.to_csv(f'source/storage/spreadsheets/{file[:-5]}.csv')
for i in link_list:
    downloadExcel(i)
entries = os.listdir('source/storage/spreadsheets/')
excel_files = [i for i in entries if 'xlsx' in i]
for i in excel_files:
    parseExcel(i)
