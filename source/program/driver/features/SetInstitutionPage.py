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
                           
            QCheckBox {
                color: #ffffff;
            }
            QLineEdit {
                background-color: #4d4d4d;
                border: 1px solid #4d4d4d;
                color: #ffffff;
                padding: 5px;
            }
            QTextEdit {
                background-color: #4d4d4d;
                border: 1px solid #4d4d4d;
                color: #ffffff;
                padding: 5px;
            }
            QProgressBar {
                border: 1px solid #444444;
                <!--border-radius: 7px;-->
                background-color: #2e2e2e;
                text-align: center;
                font-size: 10pt;
                color: white;
            }
            QProgressBar::chunk {
                background-color: #3a3a3a;
                width: 5px;
            }
            QScrollBar:vertical {
                border: none;
                background-color: #CCCCCC;
                width: 10px;
                margin: 16px 0 16px 0;

            }
            QScrollBar::handle:vertical {
                background-color: #444444;
                border-radius: 5px;
            }
            QScrollBar:horizontal {
                border: none;
                background-color: #CCCCCC;
                height: 10px;
                margin: 0px 16px 0 16px;
            }
            QScrollBar::handle:horizontal {
                background-color: #444444;
                border-radius: 5px;
            }
                           
            QTabWidget {
                background-color: #2e2e2e;
                border: none;
            }
            QTabBar::tab {
                background-color: #2e2e2e;
                color: #b1b1b1;
                padding: 8px 20px;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                border: none;
            }
        
            QTabBar::tab:selected, QTabBar::tab:hover {
                background-color: #3a3a3a;
                color: white;
            }

            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
     
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
	            background: none;
            }   

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	            background: none;
            }       
        ''')

        self.window().setWindowTitle("Ebook PR Application")
        # self.window().resize(963, 571)
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
            self.show_splash_screen()
            self.window().hide()
            setDatabaseUni(selected_text)


    
    def show_splash_screen(self):
        self.splash_screen = SplashScreen()
        self.splash_screen.show()

    def run(self):
        self.window().show()




