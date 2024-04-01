import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from .helpers.DatabaseManagement import setDatabaseUni
from .helpers.getLanguage import getLanguage
import pandas as pd
from .SplashScreenPage import SplashScreen
import yaml
import os

import logging
def packagingPath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS

    except Exception:

        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#################### WORKER THREAD CLASS #########################
class Worker(QThread):
    finished = pyqtSignal()
    def __init__(self, parent, text):
        super(Worker, self).__init__()
        self.parent = parent
        self.selected_text = text


    #Here is where the time consuming task is placed
    def run(self):

        if self.selected_text == '':
            if getLanguage() == 1:
                logging.info('Tu as besoin de selectionez une institution')
            else:
                logging.info('You need to select an institution')
                              
        else:   
            setDatabaseUni(self.selected_text)
            with open('source/config/config.yaml', 'r') as config_file:
                yaml_file = yaml.safe_load(config_file)
                yaml_file['University'] = self.selected_text
                yaml_file['Status'] = 1
            with open('source/config/config.yaml', 'w') as config_file:
                yaml.dump(yaml_file, config_file) 
            #self.window().hide()

        self.finished.emit()

class SetInstitution(QWidget):
    def __init__(self):
        super(SetInstitution, self).__init__()
        loadUi(packagingPath("source/features/ui/dropdown.ui"), self)


        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
        
        # Remove title default name
        self.window().setWindowTitle("     ")
        
        if getLanguage() == 1:
            self.institution.setText("<b>Sélectionnez l\'Institution ci-dessous<b>")
            self.institution.setStyleSheet('''font-size: 48pt;
                                           background-color: #333333;
                                            color: #ffffff;
                                           padding: 5px;
                                          border-color: #333333;''')
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
      
        ''')

        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            uniList = yaml_file['Universities'] 
        for i in uniList:
            self.institutions.addItem(i)
        self.submit_button_1.clicked.connect(self.clicked_function)
    
    def clicked_function(self):
        selected_text = self.institutions.currentText()
        if selected_text == '':
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("messageBox")
            if getLanguage() == 1:
                msg.setText("Translate")
            else:
                msg.setText("You need to select an Institution!")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

            msg.window().setWindowTitle("     ")
            transparent_pixmap = QtGui.QPixmap(1, 1)
            transparent_pixmap.fill(Qt.GlobalColor.transparent)
            msg.setWindowIcon(QIcon(transparent_pixmap))

            msg.resize(400, 200)

            msg.setStyleSheet("""
                                    QPushButton {
                                        font-weight: bold;
                                        min-width: 60px;
                                    }         
                                      
                            """)

            font = QtGui.QFont()
            font.setPointSize(14) 
            font.setBold(True) 
            msg.setFont(font)

            msg.exec()
            logging.info('You need to select an institution')
            return 
        self.window().hide()
        self.worker = Worker(self, selected_text)
        self.worker.finished.connect(self.post_thread_action)
        self.worker.start()
        if getLanguage() == 1:
            self.ss = self.show_splash_screen('Chargement des données CRKN', 20)
        else:
            self.ss = self.show_splash_screen('Loading CRKN Data', 30)


    def post_thread_action(self):
        self.home_page = self.ss.show_home_page()
    
    def show_splash_screen(self, text, size):
        self.splash_screen = SplashScreen(text, size)
        self.splash_screen.show()
        self.window().hide()
        return self.splash_screen
    
    def run(self):
        self.window().show()