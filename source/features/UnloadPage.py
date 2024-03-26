import sys
######################### THREADING IMPORT
from PyQt6.QtCore import Qt, QThread, pyqtSignal 
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import Qt
from .helpers.LocalUnload import remove_file, get_files
import sqlite3 as sq
from .UnloadSuccess import UnloadSuccess
import os
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
            remove_file(self.file_picked)
            self.finished.emit()
        except Exception as e:
            print('FAILURE')
            print(e)

class UnloadSpreadsheet(QWidget):
    def __init__(self, HomePage):
        super(UnloadSpreadsheet, self).__init__()
        self.file_picked = ''
        self.home_page = HomePage
        loadUi(img_resource_path("source/features/ui/unloadpage.ui"), self)

        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")

        fileList = get_files()
        for aF in fileList:
            print(aF)
            self.unload_sheets.addItem(aF[0])

        # Add unload functionality here
        self.submit_button.clicked.connect(self.unload_spreadsheets)

        # Cancel process here
        self.cancel_button.clicked.connect(self.close_window)



    def close_window(self):
        self.window().close()


    def unload_spreadsheets(self):
        if self.unload_sheets.currentText() == '':
            print('Must pick a spreadsheet!')
            msg = QMessageBox()
            msg.setWindowTitle("messageBox")
            msg.setText("Please pick a spreadsheet!")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.exec()
            return
        self.set_buttons_enabled(False)  # Disable buttons before starting the thread
        self.home_page.set_homepage_buttons_enabled(False)
        self.worker = Worker(self, self.unload_sheets.currentText(), self.unload_sheets.currentIndex())
        self.worker.finished.connect(self.handle_thread_finished)
        self.worker.start()

    def handle_thread_finished(self):
        self.cIndex = self.unload_sheets.currentIndex()
        self.set_buttons_enabled(True)
        self.home_page.set_homepage_buttons_enabled(True)
        global m
        m = UnloadSuccess(self.file_picked)
        m.window().show()
        self.unload_sheets.removeItem(self.cIndex)
        self.file_picked = ''

    def set_buttons_enabled(self, enabled):
        self.submit_button.setEnabled(enabled)
        self.cancel_button.setEnabled(enabled)