import sys
######################### THREADING IMPORT
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import Qt
from .helpers.unload_file import removeFile, getFiles
from .helpers.getLanguage import getLanguage
from .unload_success import UnloadSuccess
import os
import logging

def img_resource_path(relative_path):
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

    def __init__(self, parent, file_picked, c_index):
        super(Worker, self).__init__()
        self.parent = parent
        self.file_picked = file_picked
        self.c_index = c_index

    def run(self):
        try:
            removeFile(self.file_picked)
            self.finished.emit()
        except Exception as e:
            logging.info('FAILURE')
            logging.info(e)

class UnloadSpreadsheet(QWidget):
    def __init__(self, HomePage):
        super(UnloadSpreadsheet, self).__init__()
        self.filePicked = ''
        self.homePage = HomePage
        loadUi(img_resource_path("source/features/ui/unloadpage.ui"), self)
        if getLanguage() == 1:
            self.unload.setText("Sélectionner le Tableau à Décharger")
            self.unload.setStyleSheet('''font-size: 45pt;
                                        font-weight: bold;
                                           ''')
            self.submit_button.setText("Soumettre")
            self.cancel_button.setText("Annuler")

        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")

        fileList = getFiles()
        for aF in fileList:
            logging.info(aF)
            self.unload_sheets.addItem(aF[0])

        # Add unload functionality here
        self.submit_button.clicked.connect(self.unloadSpreadsheets)

        # Cancel process here
        self.cancel_button.clicked.connect(self.close_window)

    def close_window(self):
        self.window().close()

    def unloadSpreadsheets(self):
        if self.unload_sheets.currentText() == '':
            logging.info('Must pick a spreadsheet!')
            msg = QMessageBox()
            msg.setWindowTitle("messageBox")
            if getLanguage() == 1:
                msg.setText("Veuillez Sélectionner un Tableau")
            else:
                msg.setText("Please select a spreadsheet")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok )

            # Remove the default window title
            msg.window().setWindowTitle("     ")

            # Create a transparent QPixmap
            transparent_pixmap = QtGui.QPixmap(1, 1)
            transparent_pixmap.fill(Qt.GlobalColor.transparent)

            # Set the window icon with the transparent QPixmap
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
            return
        # Disable buttons before starting the thread
        self.setButtonsEnabled(False)  
        self.homePage.setHomePageButtonsEnabled(False)
        self.worker = Worker(self, self.unload_sheets.currentText(), self.unload_sheets.currentIndex())
        self.worker.finished.connect(self.handle_thread_finished)
        self.worker.start()

    def handle_thread_finished(self):
        self.cIndex = self.unload_sheets.currentIndex()
        self.setButtonsEnabled(True)
        self.homePage.setHomePageButtonsEnabled(True)
        self.unload_page = UnloadSuccess(self.filePicked)
        self.unload_page.window().show()
        self.unload_sheets.removeItem(self.cIndex)
        self.filePicked = ''

    def setButtonsEnabled(self, enabled):
        self.submit_button.setEnabled(enabled)
        self.cancel_button.setEnabled(enabled)