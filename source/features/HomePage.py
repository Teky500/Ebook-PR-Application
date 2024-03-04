import sys
from PyQt6.uic import loadUi
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget
import yaml
from .searchPageDriver import searchPageDriver
from .UploadPage import UploadSpreadsheet
from .UnloadPage import UnloadSpreadsheet
from .helpers.crknUpdater import UpdateChecker
from .FirstTimeUpdate import SetFirstTimeUpdate
from .ChangeInstitution import ChangeInstitution
class SetHomePage(QWidget):

    def getLanguage(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            language = yaml_file['Language']
        return language

    def __init__(self):
        super(SetHomePage, self).__init__()
        # self.window_width, self.window_height = 960, 750
        # self.setMinimumSize(self.window_width, self.window_height)

        loadUi("source/features/ui/homepage.ui", self)
        
        #If set to french
        if self.getLanguage() == 1:
            self.search.setText("Chercher")
            self.change.setText("Changer")
            self.update.setText("Mettre à jour")
            self.upload.setText("Mettre en ligne")
            self.unload.setText("Decharger")    #Check
            self.label.setText("PAGE D\'ACCUEIL")   #Too big
            #Change style sheet to reduce font size and fit text
            self.label.setStyleSheet("""
    QLabel {
        font: 700 80pt "Segoe UI";
        color: #ffffff;
        background-color: #333333; /* Change color */
        border: 1px solid #333333;
        padding: 5px;
    }
""")

        # self.window().resize(850, 800)
        self.search.clicked.connect(self.search_page_show)
        self.upload.clicked.connect(self.upload_page_show)
        self.unload.clicked.connect(self.unload_page_show)
        self.update.clicked.connect(self.update_page_show)
        self.change.clicked.connect(self.change_page_show)

    def upload_page_show(self):
        global m
        m = UploadSpreadsheet()
        m.show()
    def search_page_show(self):
        global m
        m = searchPageDriver()
        m.show()
    def unload_page_show(self):
        global m
        m = UnloadSpreadsheet()
        m.show()
    def change_page_show(self): # change this
        global m
        m = ChangeInstitution()
        m.show()
        self.window().hide()
    def update_page_show(self):
        global m
        checker = UpdateChecker()
        url = checker.config.get('link')
        new_excel_files = checker.get_website_excel_files(url)
        (added, removed) = checker.compare(new_excel_files)
        if (len(added) + len(removed)) == 0:
            print('Found no updates')
            from .FirstTimeUpdateConfirm import SetFirstTimeUpdateConfirm
            m = SetFirstTimeUpdateConfirm()
            m.show()
            self.window().close()
        else:

            update = SetFirstTimeUpdate(checker)
            m = update
            m.window().show()
            self.window().close()            
    def run(self):

        self.setStyleSheet ("""
            QWidget {
                background-color: #333333;
                color: #ffffff;
                border: none;
            }
                        
        """)

        self.window().show()


  