import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from .StartingPage import WelcomePage
from PyQt6.QtCore import Qt, QTimer, QPointF
import os
import yaml

def packagingPath(relative_path):
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
        self.oldPosition = QPointF()


        loadUi(packagingPath("source/features/ui/language_choice.ui"), self)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)

        
        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")
        self.English_button.clicked.connect(self.english_text)
        self.French_button.clicked.connect(self.french_text)

        self.setFixedSize(500, 280)


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

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.oldPosition = event.globalPosition()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPosition() - self.oldPosition
            window_position = self.window().pos() + delta.toPoint()
            self.window().move(window_position)
            self.oldPosition = event.globalPosition()