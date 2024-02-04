import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QVBoxLayout
from helpers.add_to_database import setDatabaseUni
import pandas as pd
from Themes import Theme, getTheme
from SplashScreenPage import SplashScreen

class SetInstitution(QWidget):
    def __init__(self):
        super(SetInstitution, self).__init__()

        loadUi("source/program/driver/features/dropdown.ui", self)


        self.window().setWindowTitle("Ebook PR Application")
        self.window().resize(963, 571)
        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')
        spreadsheet_csv = pd.read_csv('source/storage/spreadsheets/spreadsheet_1.csv', skiprows=[0,1])
        df = pd.DataFrame(spreadsheet_csv)
        Universities = df.columns[9:]
        for i in Universities:
            # should be changed to show a pop up on the front-end telling them to select an institution.
            self.institutions.addItem(i)
        self.submit_button_1.clicked.connect(self.clicked_function)
        self.splash_screen = None

    def clicked_function(self):
        selected_text = self.institutions.currentText()
        if selected_text == '':
            print('You need to select an institution')
        else:
            setDatabaseUni(selected_text)
            self.window().hide()
            self.show_splash_screen()
    
    def show_splash_screen(self):
        self.splash_screen = SplashScreen()
        self.splash_screen.finished.connect(self.show_set_institution_page)
        self.splash_screen.show()

    def show_set_institution_page(self):
        self.show()
        # self.splash_screen.close()

    def run(self):
        self.setStyleSheet('''

            QWidget {
                background-color: #333333;
                color: #ffffff;
                border: none;
            }
            QPushButton {
                background-color: #4d4d4d;
                border: 1px solid #4d4d4d;
                border-radius: 4px;
                color: #ffffff;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
                border: 1px solid #5a5a5a;
            }

        ''')

        self.window().show()




