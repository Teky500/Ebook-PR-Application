import sys
################# THREAD IMPORT
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import Qt
from .FirstTimeUpdateConfirm import SetFirstTimeUpdateConfirm
from .helpers.getLanguage import getLanguage
from .helpers.DownloadExcel import downloadFiles
from .helpers.DatabaseManagement import accessCSV, singleAddition, openExcel, removeFromDatabase
import os
import sqlite3 as sq
import yaml
import os
import logging
from .helpers.DownloadExcel import updateConfig
def packagingPath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

########################### THREAD WORKER CLASS
class Worker(QThread):
    finished = pyqtSignal()

    def __init__(self, checker):
        super(Worker, self).__init__()
        self.checker = checker

    #Time consuming task
    def run(self):

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
            df = accessCSV(i)
            try:  
                uni = df.columns.get_loc(University)
            except KeyError as e:
                logging.info(str(e))
                logging.info(f'Ignored {filename}. Does not include {University}')
                continue      
            platform = openExcel(f'source/storage/excel/{filename}')
            singleAddition(df, cursor, platform, University, filename, 'Y')
            db.commit()
        self.finished.emit()


class SetFirstTimeUpdate(QWidget):
    def __init__(self, check):
        super(SetFirstTimeUpdate, self).__init__()

        loadUi(packagingPath("source/features/ui/updatefirst-timepage.ui"), self)
        self.checker = check
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        if getLanguage() == 1:
            self.confirm_update_1.setText("Oui")
            self.cancel_update_1.setText("Non")
            self.label.setText("<b>Vos données CRKN ne sont pas à jour,<b>")
            self.label_2.setText("<b>souhaitez-vous les mettre à jour?<b>")
            # French "j" gets cut off by buttons so I moved it up
            current_geometry = self.label_2.geometry()
            self.label_2.setGeometry(current_geometry.x(), current_geometry.y() - 5, current_geometry.width(), current_geometry.height())

            self.label.setStyleSheet('''    
                                            font-size: 16pt;
                                            background-color: #333333;
                                            color: #ffffff;
                                            padding: 5px;
                                            border-color: #333333;
                                     ''')
            self.label_2.setStyleSheet('''    
                                            font-size: 16pt;
                                            background-color: #333333;
                                            color: #ffffff;
                                            padding: 5px;
                                            border-color: #333333;
                                     ''')

        self.confirm_update_1.clicked.connect(self.load_confirm_page)
        self.cancel_update_1.clicked.connect(self.load_home_page)

    
    ######## THREADING: MODIFIED THIS CLASS
    def load_confirm_page(self):
        from .SplashScreenPage import SplashScreen
        self.setButtonsEnabled(False)
        self.worker = Worker(self.checker)
        self.worker.finished.connect(self.handle_thread_finished)
        self.worker.start()
        if getLanguage() == 1:
            self.ss = SplashScreen("Mise à jour en cours", 32)
        else:
            self.ss = SplashScreen("Updating", 35)
        self.ss.window().show()
        self.window().hide()

    ############ THREADING: CREATE NEW FUNCTION    
    def handle_thread_finished(self):
        self.setButtonsEnabled(True)
        self.ss.window().close()
        updateConfig()
        if getLanguage() == 1:
            self.first_time_update = SetFirstTimeUpdateConfirm("<b>Vos données CRKN sont désormais à jour.<b>", 0)
        else:
            self.first_time_update = SetFirstTimeUpdateConfirm('Your CRKN data is now up to date.', 0)

        self.window().hide()
        self.first_time_update.run()

    def load_home_page(self):
        from .HomePage import SetHomePage
        self.home_page = SetHomePage()
        self.window().hide()
        self.home_page.run()

    def setButtonsEnabled(self, enabled):
        self.confirm_update_1.setEnabled(enabled)
        self.cancel_update_1.setEnabled(enabled)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = SetFirstTimeUpdate()
    widget.show()
    sys.exit(app.exec())