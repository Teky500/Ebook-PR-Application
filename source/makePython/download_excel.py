from urllib.request import urlretrieve

url = 'https://library.upei.ca/sites/default/files/TaylorFrancis_CRKN_EbookPARightsTracking.xlsx'
filename = ('source/storage/spreadsheets/spreadsheet_1.xlsx')
urlretrieve(url, filename)