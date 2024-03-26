import sys
import os
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
import yaml

from .SearchDriverPage import searchPageDriver
from .UploadPage import UploadSpreadsheet
from .UnloadPage import UnloadSpreadsheet
from .helpers.CrknUpdating import UpdateChecker
from .helpers.getLanguage import getLanguage
from .FirstTimeUpdate import SetFirstTimeUpdate
from .ChangeInstitution import ChangeInstitution

import os
from urllib import request

import logging

def internet_on():
    try:
        request.urlopen('https://www.google.com/', timeout=1)
        return True
    except request.URLError as err: 
        return False

def packagingPath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class SetHomePage(QWidget):
    
    def getUniversity(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            University = yaml_file['University']
        return University

    def __init__(self):

        super(SetHomePage, self).__init__()


        loadUi(packagingPath("source/features/ui/homepage.ui"), self)

        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")
        self.current_page = None
        #If set to french
        self.language = getLanguage()
        self.switch_language.setText('Passer en Français')
        if self.language == 1:
            self.search.setText("Chercher")
            self.change.setText("Remise à zéro")
            self.update.setText("Mettre à jour")
            self.upload.setText("Mettre en ligne")
            self.unload.setText("Decharger")    #Check
            self.exit.setText("Fermer")
            self.switch_language.setText("Switch to English")
        self.search.clicked.connect(self.search_page_show)
        self.upload.clicked.connect(self.upload_page_show)
        self.unload.clicked.connect(self.unload_page_show)
        self.update.clicked.connect(self.update_page_show)
        self.change.clicked.connect(self.change_page_show)
        self.exit.clicked.connect(self.exit_homepage)
        self.set_university_name.setText(self.getUniversity())
        self.switch_language.clicked.connect(self.switch_display_language)
    def switch_display_language(self):
        if self.language == 1:
            self.search.setText("Search Book")
            self.change.setText("Reset All")
            self.update.setText("Update CRKN")
            self.upload.setText("Upload Local")
            self.unload.setText("Unload Local")    #Check
            self.exit.setText("Exit")
            self.switch_language.setText("Passer en français")
            with open('source/config/config.yaml', 'r') as config_file:
                yaml_file = yaml.safe_load(config_file)
                yaml_file['Language'] = 0
            with open('source/config/config.yaml', 'w') as config_file:
                yaml.dump(yaml_file, config_file) 
            self.language = 0
        else:
            self.search.setText("Chercher")
            self.change.setText("Remise à zéro")
            self.update.setText("Mettre à jour")
            self.upload.setText("Mettre en ligne")
            self.unload.setText("Decharger")    #Check
            self.exit.setText("Fermer")
            self.switch_language.setText("Switch to English")
            with open('source/config/config.yaml', 'r') as config_file:
                yaml_file = yaml.safe_load(config_file)
                yaml_file['Language'] = 1
            with open('source/config/config.yaml', 'w') as config_file:
                yaml.dump(yaml_file, config_file)
            self.language = 1
    def exit_homepage(self):
        sys.exit()
    
    def setHomePageButtonsEnabled(self, enabled):
        self.search.setEnabled(enabled)
        self.upload.setEnabled(enabled)
        self.unload.setEnabled(enabled)
        self.change.setEnabled(enabled)
        self.update.setEnabled(enabled)
    
    ######################## THREAD
    def upload_page_show(self):
        self.current_page = UploadSpreadsheet(self)
        self.current_page.show()

    def search_page_show(self):
        self.current_page = searchPageDriver()
        self.current_page.show()

    ######################## THREAD
    def unload_page_show(self):
        self.current_page = UnloadSpreadsheet(self)
        self.current_page.show()

    def change_page_show(self):
        self.change_page = ChangeInstitution()
        self.change_page.show()
        self.window().close()
        if self.current_page:
            self.current_page.close()

    def update_page_show(self):

        if not internet_on():
            logging.info('NO INTERNET')
            from .NetworkFailurePage import NetworkPage
            msg = 'Could not check for updates due to network error. Please check your network connection and try again.'
            if self.language == 1:
                msg = "Impossible de vérifier les mises à jour CRKN en raison d'une erreur réseau. Veuillez vérifier votre connexion internet et réessayer!"
            self.NPage = NetworkPage(msg)
            self.NPage.window().show()
            return 

        checker = UpdateChecker()
        url = checker.config.get('link')
        new_excel_files = checker.getWebsiteExcelFiles(url)
        if new_excel_files == []:
            logging.info('Did not find any excel files on the URL!')
            from .NetworkFailurePage import NetworkPage
            msg = 'Your link is not correct, no excel files found!'
            if self.language == 1:
                msg = "Le lien est incorrect, pas de fichier excel trouvé!"
            self.NPage = NetworkPage(msg)
            self.NPage.window().show()
            return 
        (added, removed) = checker.compare(new_excel_files)

        if (len(added) + len(removed)) == 0:
            logging.info('Found no updates')
            from .FirstTimeUpdateConfirm import SetFirstTimeUpdateConfirm
            msg = 'Your CRKN data is already up to date!'
            if getLanguage() == 1:
                msg = "<b>Vos informations CRKN sont à jour!<b>"
            self.update_confirm_page = SetFirstTimeUpdateConfirm(msg, 0)
            self.update_confirm_page.show()

            self.window().close()
            if self.current_page:
                self.current_page.close()
        else:
            self.update = SetFirstTimeUpdate(checker)
            self.update.window().show()
            self.window().close()
            if self.current_page:
                self.close()

    def run(self):

        self.setStyleSheet ("""
            QWidget {
                background-color: #333333;
                color: #ffffff;
                border: none;
            }
                        
        """)

        self.window().show()
