import sys
import os
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
import yaml

from .searchPageDriver import searchPageDriver
from .UploadPage import UploadSpreadsheet
from .UnloadPage import UnloadSpreadsheet
from .helpers.crknUpdater import UpdateChecker
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

def img_resource_path(relative_path):
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


        loadUi(img_resource_path("source/features/ui/homepage.ui"), self)

        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")
        self.current_page = None
        #If set to french
        if getLanguage() == 1:
            self.search.setText("Chercher")
            self.change.setText("Changer")
            self.update.setText("Mettre à jour")
            self.upload.setText("Mettre en ligne")
            self.unload.setText("Decharger")    #Check
            self.exit.setText("Sortir")

        self.search.clicked.connect(self.search_page_show)
        self.upload.clicked.connect(self.upload_page_show)
        self.unload.clicked.connect(self.unload_page_show)
        self.update.clicked.connect(self.update_page_show)
        self.change.clicked.connect(self.change_page_show)
        self.exit.clicked.connect(self.exit_homepage)
        self.set_university_name.setText(self.getUniversity())

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
            if getLanguage() == 1:
                msg = "Impossible de vérifier les mises à jour CRKN en raison d'une erreur réseau. Veuillez vérifier votre connexion internet et réessayer!"
            self.NPage = NetworkPage(msg)
            self.NPage.window().show()
            return 

        checker = UpdateChecker()
        url = checker.config.get('link')
        new_excel_files = checker.get_website_excel_files(url)
        if new_excel_files == []:
            logging.info('Did not find any excel files on the URL!')
            from .NetworkFailurePage import NetworkPage
            self.NPage = NetworkPage('Your link is not correct, no excel files found!')
            self.NPage.window().show()
            return 
        (added, removed) = checker.compare(new_excel_files)

        if (len(added) + len(removed)) == 0:
            logging.info('Found no updates')
            from .FirstTimeUpdateConfirm import SetFirstTimeUpdateConfirm

            if getLanguage() == 1:
                self.update_confirm_page = SetFirstTimeUpdateConfirm("<b>Vos données CRKN sont déjà à jour !<b>", 0)
            else:
                self.update_confirm_page = SetFirstTimeUpdateConfirm('Your CRKN data is already up to date!', 0)
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
