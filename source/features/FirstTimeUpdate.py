import sys
################# THREAD IMPORT
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget
from PyQt6.QtCore import Qt
from .FirstTimeUpdateConfirm import SetFirstTimeUpdateConfirm

from .helpers.download_excel import downloadFiles
from .helpers.add_to_database import access_csv, singleAddition, openExcel, removeFromDatabase
import os
import sqlite3 as sq
import yaml

########################### THREAD WORKER CLASS
class Worker(QThread):
    finished = pyqtSignal()

    def __init__(self, checker):
        super(Worker, self).__init__()
        self.checker = checker
    #Time consuming task
    def run(self):
        self.checker.update_config()
        removeFromDatabase()
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            University = yaml_file['University'] 
        downloadFiles()
        entries = os.listdir('source/storage/spreadsheets/')
        csv_files = [i for i in entries if ('.csv' in i) and ('CRKN_EbookPARightsTracking' in i)]
        db = sq.connect('source/storage/database/proj.db')
        cursor = db.cursor()
        for i in csv_files:
            filename = i[:-4] + '.xlsx'
            df = access_csv(i)
            try:  
                uni = df.columns.get_loc(University)
            except KeyError as e:
                print(str(e))
                print(f'Ignored {filename}. Does not include {University}')
                continue      
            platform = openExcel(f'source/storage/excel/{filename}')
            singleAddition(df, cursor, platform, University, filename, 'Y')
            db.commit()
        self.finished.emit()



class SetFirstTimeUpdate(QWidget):
    def __init__(self, check):
        super(SetFirstTimeUpdate, self).__init__()

        loadUi("source/features/ui/updatefirst-timepage.ui", self)
        self.checker = check
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.confirm_update_1.clicked.connect(self.load_confirm_page)
        self.cancel_update_1.clicked.connect(self.load_home_page)

    
    ######## THREADING: MODIFIED THIS CLASS
    def load_confirm_page(self):
        self.setButtonsEnabled(False)
        self.worker = Worker(self.checker)
        self.worker.finished.connect(self.handle_thread_finished)
        self.worker.start()

    ############ THREADING: CREATE NEW FUNCTION    
    def handle_thread_finished(self):
        self.setButtonsEnabled(True)
        global m
        new_window = SetFirstTimeUpdateConfirm()
        m = new_window
        self.window().hide()
        new_window.run()

    def load_home_page(self):
        from .HomePage import SetHomePage
        global m
        new_window = SetHomePage()
        m = new_window
        self.window().hide()
        new_window.run()

    def setButtonsEnabled(self, enabled):
        self.confirm_update_1.setEnabled(enabled)
        self.cancel_update_1.setEnabled(enabled)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = SetFirstTimeUpdate()
    widget.show()
    sys.exit(app.exec())