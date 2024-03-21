import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from .helpers.getLanguage import getLanguage
import os

def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class UnloadSuccess(QWidget):
    def __init__(self, fileN):
        super(UnloadSuccess, self).__init__()
        self.filePicked = ''

        loadUi(img_resource_path("source/features/ui/unloadpage_success.ui"), self)
        if getLanguage() == 1:
            self.unload.setText("Succès!")
            #Not sure what happen to below message, keeping just in case
            #self.file_label_1.setText("Vous avez mis à jour la base de données avec succès...")
        
        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")

        if getLanguage() == 1:
            self.label.setText(f'Fichier {fileN} supprimé avec succès')
        else:
            self.label.setText(f'Successfully removed file {fileN}')
        self.cancel_button.clicked.connect(self.close_window)

    def close_window(self):
        self.window().close()
        
