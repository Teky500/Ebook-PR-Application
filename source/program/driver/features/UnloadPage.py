import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from .Themes import Theme, getTheme
from .helpers.unload_file import removeFile, getFiles
import sqlite3 as sq
from .unload_success import UnloadSuccess
from .helpers.getLanguage import getLanguage

class UnloadSpreadsheet(QWidget):
    def __init__(self):
        super(UnloadSpreadsheet, self).__init__()
        self.filePicked = ''

        loadUi("source/program/driver/features/ui/unloadpage.ui", self)

        if getLanguage() == 1:
            self.unload.setText("Sélectionnez la feuille de calcul à décharger")
            #Make text smaller
            self.unload.setStyleSheet("""
    QLabel {
        font: 700 32pt "Segoe UI";
        color: #ffffff;
        background-color: #333333; /* Change color */
        border: 1px solid #333333;
        padding: 5px;
    }
""")
            self.submit_button.setText("Soumettre")
            self.cancel_button.setText("Annuler")

        fileList = getFiles()
        for aF in fileList:
            print(aF)
            self.unload_sheets.addItem(aF[0])
        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')

        # Add unload functionality here
        self.submit_button.clicked.connect(self.unloadSpreadsheets)

        # Cancel process here
        self.cancel_button.clicked.connect(self.close_window)

    def unloadSpreadsheets(self):
        global m
        self.filePicked = self.unload_sheets.currentText()
        self.cIndex = self.unload_sheets.currentIndex()
        if self.filePicked == '':
            print('Please pick a file!')
            return False
        try:
            removeFile(self.filePicked)
            m = UnloadSuccess(self.filePicked)
            m.window().show()
        except Exception as e:
            print('FAILURE')
        self.unload_sheets.removeItem(self.cIndex)
        self.filePicked = ''


    def close_window(self):
        self.window().close()

