import sys
######################### THREADING IMPORT
from PyQt6.QtCore import Qt, QThread, pyqtSignal 
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from .Themes import Theme, getTheme
from .helpers.unload_file import removeFile, getFiles
import sqlite3 as sq
from .unload_success import UnloadSuccess


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
            print('FAILURE')
            print(e)

class UnloadSpreadsheet(QWidget):
    def __init__(self, HomePage):
        super(UnloadSpreadsheet, self).__init__()
        self.filePicked = ''
        self.homePage = HomePage
        loadUi("source/program/driver/features/ui/unloadpage.ui", self)
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



    def close_window(self):
        self.window().close()


    def unloadSpreadsheets(self):
        self.setButtonsEnabled(False)  # Disable buttons before starting the thread
        self.homePage.setHomePageButtonsEnabled(False)
        self.worker = Worker(self, self.unload_sheets.currentText(), self.unload_sheets.currentIndex())
        self.worker.finished.connect(self.handle_thread_finished)
        self.worker.start()

    def handle_thread_finished(self):
        self.cIndex = self.unload_sheets.currentIndex()
        self.setButtonsEnabled(True)
        self.homePage.setHomePageButtonsEnabled(True)
        global m
        m = UnloadSuccess(self.filePicked)
        m.window().show()
        self.unload_sheets.removeItem(self.cIndex)
        self.filePicked = ''

    def setButtonsEnabled(self, enabled):
        self.submit_button.setEnabled(enabled)
        self.cancel_button.setEnabled(enabled)
