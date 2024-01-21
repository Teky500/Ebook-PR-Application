import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QPushButton
import sqlite3 as sq
import pandas as pd

class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("DropDown")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.combo_box = QComboBox(self)
        self.combo_box.addItem("")
        self.combo_box.addItem("Univ. of Prince Edward Island")
        self.combo_box.addItem("Acadia Univ.")
        self.combo_box.addItem("Algoma Univ.")

        layout.addWidget(self.combo_box)

        confirm_button = QPushButton("Confirm", self)
        confirm_button.clicked.connect(self.on_confirm_clicked)

        layout.addWidget(confirm_button)

    def on_combobox_changed(self):
        selected_text = self.sender().currentText()
        print(f"Selected option: {selected_text}")
        setDatabaseUni(selected_text)

    def on_confirm_clicked(self):
        selected_text = self.combo_box.currentText()
        print(f"Confirmed option: {selected_text}")
        setDatabaseUni(selected_text)

import sqlite3 as sq
import os

def setDatabaseUni(university):
  University = university
  with open('source/sqlscripts/db_setup.sql', 'r') as sql_file:
      sql_script = sql_file.read()
  db_path = 'source/storage/database/proj.db'
  # check if the db exists first
  if os.path.isfile(db_path):
      print('Removed Old Path')
      os.remove(db_path)
  # clean csv file (should be done in another file, but done here for now)
  # using skiprows=[0,1] to skip the first two fluff lines. Not a long term solution, we have to look for something else, but this will do for now.
  spreadsheet_csv = pd.read_csv('source/storage/spreadsheets/spreadsheet_1.csv', skiprows=[0,1])
  df = pd.DataFrame(spreadsheet_csv)
  df = df[df['Platform_eISBN'].notna()]
  uni = df.columns.get_loc(University)
  db = sq.connect(db_path)
  cursor = db.cursor()
  cursor.executescript(sql_script)
  db.commit()
  for row in df.iterrows():
    title = row[1]['Title']
    publisher = row[1]['Publisher']
    platform_yob = row[1]['Platform_YOP']
    ISBN = row[1]['Platform_eISBN']
    OCN = row[1]['OCN']
    result = row[1][University]
    print('ADDING ROW TO DATABASE', (title, publisher, platform_yob, ISBN, OCN, result))
    try:
      cursor.execute("INSERT INTO books (title, publisher, platform_yop, ISBN, OCN, result) VALUES(?, ?, ?, ?, ?, ?)", 
                    (title, publisher, platform_yob, ISBN, OCN, result))
    # sometimes the the same ISBN will be there twice. For now, ignore those rows.
    except sq.IntegrityError:
      print('FAILED ADDITION', (title, publisher, platform_yob, ISBN, OCN, result))
  db.commit()
  db.close()


def parse_excel():
    xfile = pd.read_excel('source/storage/spreadsheets/spreadsheet_1.xlsx', sheet_name= "PA-Rights")
    print(xfile)
    xfile.to_csv('source/storage/spreadsheets/spreadsheet_1.csv')

from urllib.request import urlretrieve
def download_excel():
    url = 'https://library.upei.ca/sites/default/files/TaylorFrancis_CRKN_EbookPARightsTracking.xlsx'
    filename = ('source/storage/spreadsheets/spreadsheet_1.xlsx')
    urlretrieve(url, filename)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

