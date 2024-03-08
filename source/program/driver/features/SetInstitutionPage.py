import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QVBoxLayout 
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from .helpers.add_to_database import setDatabaseUni
import pandas as pd
from .Themes import Theme, getTheme
from .SplashScreenPage import SplashScreen
import time
import yaml

#################### WORKER THREAD CLASS #########################
class Worker(QThread):
    finished = pyqtSignal()
    def __init__(self, parent, text, splash):
        super(Worker, self).__init__()
        self.parent = parent
        self.selected_text = text
        self.splash = splash


    #Here is where the time consuming task is placed
    def run(self):

        if self.selected_text == '':
            if self.getLanguage == 1:
                print('Tu as besoin de selectionez une institution')
            else:
                print('You need to select an institution')
        else:
            with open('source/config/config.yaml', 'r') as config_file:
                yaml_file = yaml.safe_load(config_file)
                yaml_file['University'] = self.selected_text
                yaml_file['Status'] = 1
            with open('source/config/config.yaml', 'w') as config_file:
                yaml.dump(yaml_file, config_file) 
            
            setDatabaseUni(self.selected_text)
            #self.window().hide()

        self.finished.emit()

class SetInstitution(QWidget):
    def __init__(self):
        super(SetInstitution, self).__init__()
        loadUi("source/program/driver/features/ui/dropdown.ui", self)
        if self.getLanguage() == 1:
            self.institution.setText("Sélectionnez l\'Institution ci-dessous")
            self.submit_button_1.setText("Soumettre")
            

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
        if themeColour == {}:
            pass
        else:
            bg_col = themeColour['background_color']
            txt_col = themeColour['text_color']
            self.setStyleSheet(f'background-color: {bg_col}; color: {txt_col};')
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            uniList = yaml_file['Universities'] 
        for i in uniList:
            self.institutions.addItem(i)
        global m
        self.splash = self.show_splash_screen()
        self.submit_button_1.clicked.connect(self.clicked_function)




    
    def clicked_function(self):
        selected_text = self.institutions.currentText()
        self.window().hide()
        self.worker = Worker(self, selected_text, self.splash)
        self.worker.finished.connect(self.post_thread_action)
        self.worker.start()

    def post_thread_action(self):
        global m
        m = self.splash.show_home_page()

    
    def show_splash_screen(self):
        self.splash_screen = SplashScreen()
        self.splash_screen.show()
        self.window().hide()
        return self.splash_screen
    
    def run(self):
        self.window().show()

    def getLanguage(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            language = yaml_file['Language']
        return language


