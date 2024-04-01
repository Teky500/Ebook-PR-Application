import sys
import logging
######################### THREADING IMPORT
from PyQt6.QtCore import Qt, QThread, pyqtSignal 
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QFileDialog
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
import yaml
from .helpers.LocalUpload import localFileUpload
from .UploadSuccess import UploadSuccess
from .UploadFailure import UploadFailure
from .helpers.getLanguage import getLanguage

import os
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
    finished = pyqtSignal(list)

    def __init__(self, file_path):
        super(Worker, self).__init__()
        self.file_path = file_path

    #Here is where the time consuming task is placed
    def run(self):

        result = localFileUpload(self.file_path) 
        self.finished.emit(result)

class UploadSpreadsheet(QWidget):
    ########################################### THREAD (ADD PARAMTER): HomePage object
    def __init__(self, HomePage): 
        super(UploadSpreadsheet, self).__init__()
        self.home_page = HomePage ############################### THREADING: Initialize home page
        self.filePicked = ''
        self.worker = Worker(None) ############################## THREAD: initialize worker
        loadUi(packagingPath("source/features/ui/upload.ui"), self)

        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")

        if getLanguage() == 1:
            self.label.setText("<b>Ajouter un fichier local<b>")
            #Change style sheet to reduce font size and fit text
            self.label.setStyleSheet("""
                QLabel {
                    font: 700 38pt "Segoe UI";
                    padding: 5px;
                }
            """)
    
            self.upload_button_1.setText("Ajouter")
            self.upload_local_file.setText("Soumettre")
            self.cancel_process.setText("Annuler")
            self.file_label_1.setText("aucun fichier sélectionné")

        # Add upload button
        self.upload_button_1.clicked.connect(self.uploadFile)

        # Cancel process
        self.cancel_process.clicked.connect(self.close_window)
        self.upload_local_file.clicked.connect(self.submitFile)
        self.upload_local_file.hide()

    def uploadFile(self):
        # Open file dialog to select a file
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Spreadsheet Files (*.xlsx)")
        if fileName:
            logging.info(f"File selected: {fileName}")
            # Update the label to show the selected file path
            self.filePicked = fileName
            if getLanguage() == 1:
                self.file_label_1.setText(f"Fichier sélectionné: {fileName}")
                self.upload_button_1.setText("Changer de fichier")
                self.upload_button_1.setStyleSheet('''font-size: 16pt;
                                                      font-weight: bold;
                                           ''')
            else:
                self.file_label_1.setText(f"Selected File: {fileName}")
                self.upload_button_1.setText('Change File')
            self.upload_local_file.show()

    ################################### THREAD (MODIFIED FUNCTION)
    def submitFile(self):
        if self.filePicked == "":
            logging.info('NO FILE SELECTED')
        else:
            self.home_page.setHomePageButtonsEnabled(False)
            self.setUploadPageButtonsEnabled(False)
            self.worker.file_path = self.filePicked
            self.worker.finished.connect(self.handle_upload_result)
            self.worker.start()
            if getLanguage() == 1:
               self.show_splash_screen('Chargement des Données du Tableau', 18)
            else:
                self.show_splash_screen('Loading Spreadsheet Data', 20)
            self.setStyleSheet("""
                    QWidget{
                        background-color: gray;
                        color: #ffffff;
                        border-color: #333333;
                    }
                               
                    QPushButton {
                        background-color: #A8A8A8;
                        border: 1px solid gray;
                        border-radius: 4px;
                        color: #ffffff;
                        padding: 5px;
                    }
                               
                    QPushButton:hover {
                        background-color: gray;
                        border: 1px solid #5a5a5a;
                    }
                               
            """)

    def show_splash_screen(self, text, size):
        from .SplashScreenPage import SplashScreen
        self.splash_screen = SplashScreen(text, size)
        self.splash_screen.window().show()
    def close_window(self):
        self.window().close()
    
    ################################# THREAD (NEW FUNCTION): TO DISABLE BUTTONS
    def setUploadPageButtonsEnabled(self, enabled):
        self.upload_button_1.setEnabled(enabled)
        self.upload_local_file.setEnabled(enabled)
        self.cancel_process.setEnabled(enabled)

    ############################## THREAD (NEW FUNCTION): to handle what happens after upload occurs
    def handle_upload_result(self, result):
        self.setUploadPageButtonsEnabled(True)
        self.home_page.setHomePageButtonsEnabled(True)
        self.splash_screen.window().close()
        if result[0] == 'Y':
            if getLanguage() == 1:
                self.upload_success = UploadSuccess(f'{result[1]} lignes ajoutées avex succès!')
            else:
                self.upload_success = UploadSuccess(f'Successfully added {result[1]} rows!')
            self.upload_success.window().show()
        elif type(result[0]) == str:
            r = result[0]
            logging.info(r)
            self.upload_success_page = UploadFailure(r)
            self.upload_success_page.window().show()            

        else:
            if result[0] == 3:
                r = 'No PA-Rights sheet.'
            if 5 in result:
                r = 'Chosen university does not match cell I3.'
            if 4 in result:
                r = 'One or more columns or headers are missing or wrong. \n Check documentation.'
            if 2 in result:
                r = 'Missing platform on cell A1.'
            if 1 in result:
                r = 'Invalid file, please upload a .xlsx file.'
            self.upload_success_page = UploadFailure(r)
            self.upload_success_page.window().show()
        self.filePicked = ''
        self.upload_local_file.hide()
        if getLanguage() == 1:
            self.file_label_1.setText('Aucun Fichier Sélectionné')
            self.upload_button_1.setText('Télécharger vers')
        else:
            self.file_label_1.setText('No File Selected')
            self.upload_button_1.setText('Upload')
        self.setStyleSheet("""
                    QWidget {
                        background-color: #333333;
                        color: #ffffff;
                        border-color: #333333;
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
            """)
