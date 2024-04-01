import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from .helpers.LocalUpload import localFileUpload
from .helpers.getLanguage import getLanguage
import os

def packagingPath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class UploadSuccess(QWidget):
    def __init__(self, msg='Success!'):
        super(UploadSuccess, self).__init__()
        self.filePicked = ''

        loadUi(packagingPath("source/features/ui/uploadpage_success.ui"), self)
        
        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")
        
        if getLanguage() == 1:
            self.upload_sucess.setStyleSheet('''font-size: 38pt;
                                         font-weight: bold;''')  
            self.upload_sucess.setText("Succès!")
        else:
            self.upload_sucess.setText(msg)
        self.cancel_button.clicked.connect(self.close_window)

    def close_window(self):
        self.window().close()

