import sys
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QStackedWidget
from .SetInstitutionPage import SetInstitution
import yaml
from .helpers.DownloadExcel import downloadFiles
from .helpers.CrknUpdating import UpdateChecker
import time
from .helpers.getLanguage import getLanguage
import os
from urllib import request
from .NetworkFailurePage import NetworkPage
import logging
def internet_on():
    try:
        request.urlopen('https://www.google.com/', timeout=1)
        return True
    except request.URLError as err: 
        logging.info(err)
        return False


class Worker(QThread):
    finished = pyqtSignal()
    def __init__(self, var):
        super(Worker, self).__init__()
        self.var = var
    #Here is where the time consuming task is placed
    def run(self):
        for i in os.listdir('source/storage/excel'):
            if i == '.gitignore':
                continue
            os.remove(f'source/storage/excel/{i}')
        for i in os.listdir('source/storage/spreadsheets'):
            if i == '.gitignore':
                continue
            os.remove(f'source/storage/spreadsheets/{i}')
        download_result = downloadFiles()
        if not download_result:
            logging.info('No excel links found to download!')
            self.var.valid_link = False
        self.finished.emit()

class Worker2(QThread):
    finished = pyqtSignal()
    def __init__(self, var):
        super(Worker2, self).__init__()
        self.var = var

    #Here is where the time consuming task is placed
    def run(self):
        checker = UpdateChecker()
        url = checker.config.get('link')
        new_excel_files = checker.getWebsiteExcelFiles(url)
        if new_excel_files == []:
            self.var.valid_link = False
        (added, removed) = checker.compare(new_excel_files)
        self.var.added = added
        self.var.removed = removed
        self.var.checker = checker
        self.finished.emit()

class WelcomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.language = getLanguage()
        self.valid_link = True
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        if self.language == 1:
            label = QLabel(f"Démarrage", self)
        else:
            label = QLabel(f"Starting", self)
        font = label.font()
        font.setPointSize(35) 
        font.setBold(True)
        label.setFont(font)

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.animate_text)
        self.animation_counter = 0

        self.page_timer = QTimer(self)

        self.animation_timer.start(600)

        self.window().setFixedSize(500, 280)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.show_next_page()

    def getStatus(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            status = yaml_file['Status']
        return status
    
    def animate_text(self):
        dots = '.' * (self.animation_counter % 4)
        label = self.findChild(QLabel)
        if self.language == 1:
            label.setText(f"Démarrage{dots}")
        else:
            label.setText(f"Starting{dots}")
        self.animation_counter += 1

    def show_next_page(self):
        self.window().close()

        self.openNewWindow()
  
    def setFixedSize(self, width, height):
        super().setFixedSize(width, height)
        
    def post_thread_show_status_1(self):
        if not self.valid_link:
            logging.info('No network connection: cant fetch data.')
            msg = "Did not find any excel files. URL is incorrect!" 
            if getLanguage() == 1:
                msg = "Cannot download spreadsheets. Veuillez vérifier votre connexion internet et réessayer!"
            self.network_page = NetworkPage(msg)
            self.network_page.show()
            QTimer.singleShot(0, self.window().close)            
            return
        self.window().close()
        self.set_institution = SetInstitution()
        self.set_institution.run()

    def post_thread_show_status_2(self):
        self.animation_timer.stop()
        global m

        self.close()
        if not self.valid_link:
            logging.info('No excel files found on link!')
            from .UpdateFailureNetworkPage import NetworkUpdateFailurePage
            self.new_window = NetworkUpdateFailurePage()
            self.new_window.window().show()
            self.window().close()                
            QTimer.singleShot(0, self.window().close)
            return        
        if (len(self.added) + len(self.removed)) == 0:
            from .HomePage import SetHomePage
            logging.info('Status 1, found no updates')
            self.window().close()
            self.home_page = SetHomePage()
            self.home_page.window().show()
            self.window().close()
        else:
            from .FirstTimeUpdate import SetFirstTimeUpdate
            logging.info('Status 1, found update')
            logging.info(self.added, self.removed)
            self.window().close()
            self.update = SetFirstTimeUpdate(self.checker)
            self.update.window().show()
            self.window().close()

    def openNewWindow(self):
        global m
        if self.getStatus() == 0:
            logging.info('Status 0')
            if internet_on():
                self.worker = Worker(self)
                self.worker.finished.connect(self.post_thread_show_status_1)
                self.worker.start()
            else:

                logging.info('No network connection: cant fetch data.')
                msg = "Can't download spreadsheets for initial launch due to network connection error. Please check your internet connection and try again" 
                if getLanguage() == 1:
                    msg = "Cannot download spreadsheets. Veuillez vérifier votre connexion internet et réessayer!"
                self.network_page = NetworkPage(msg)
                self.network_page.show()
                QTimer.singleShot(0, self.window().close)

        else:
            if not internet_on():
                logging.info('No network connection: Can not check for updates')
                from .UpdateFailureNetworkPage import NetworkUpdateFailurePage
                self.new_window = NetworkUpdateFailurePage()
                self.new_window.window().show()
                self.window().close()                
                QTimer.singleShot(0, self.window().close)


            else:
                self.worker = Worker2(self)
                self.worker.finished.connect(self.post_thread_show_status_2)
                self.worker.start()  



def extra_run():

    app = QApplication(sys.argv)
    app.setStyleSheet("""
                           
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
            
            QScrollBar:vertical {
                border: 1px solid #444444;
                background-color: #3a3a3a;
                width: 15px;
                height: 25px;
                margin: 16px 0 16px 0;

            }
            QScrollBar::handle:vertical {
                background-color: #444444;
                border-radius: 5px;
            }
                      
            QScrollBar:horizontal {
                border: 1px solid #444444;
                background-color: #3a3a3a;
                height: 15px;
                margin: 0px 16px 0 16px;
            }
                      
            QScrollBar::handle:horizontal {
                background-color: #444444;
                border-radius: 5px;
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

            """)

    main_window = QWidget()
    main_layout = QVBoxLayout(main_window)

    stacked_widget = QStackedWidget(main_window)
    welcome_page = WelcomePage(stacked_widget)
  
    stacked_widget.addWidget(welcome_page)
    main_layout.addWidget(stacked_widget)

    main_window.show()

    sys.exit(app.exec())

