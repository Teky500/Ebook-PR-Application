import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from .StartingPage import WelcomePage
import os
import yaml

def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class LanguageChoice(QWidget):
    def __init__(self, errorM):
        super(LanguageChoice, self).__init__()

        loadUi(img_resource_path("source/features/ui/language_choice.ui"), self)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        self.setFixedSize(500, 400)  # Set the fixed size of the window
        self.ui.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")
        self.English_button.clicked.connect(self.english_text)
        self.French_button.clicked.connect(self.french_text)

    def english_text(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            yaml_file['Language'] = 0
        with open('source/config/config.yaml', 'w') as config_file:
            yaml.dump(yaml_file, config_file)            
        self.new_page = WelcomePage()
        self.new_page.window().show()
        self.window().close()
    def french_text(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            yaml_file['Language'] = 1
        with open('source/config/config.yaml', 'w') as config_file:
            yaml.dump(yaml_file, config_file)
        self.new_page = WelcomePage()
        self.new_page.window().show()
        self.window().close()

    def close_window(self):
        self.window().close()
        