import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
import os

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
        self.filePicked = ''

        loadUi(img_resource_path("source/features/ui/language_choice.ui"), self)
        
        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")

        self.English_button.clicked.connect(self.english_text)
        self.French_button.clicked.connect(self.french_text)

    def english_text(self):
        self.confirmationText.setText("Language set to English")

    def french_text(self):
        self.confirmationText.setText("Language set to French")

    def close_window(self):
        self.window().close()
        
from PyQt6.QtWidgets import QApplication, QWidget
    
app = QApplication(sys.argv)  # Create an instance of QApplication
widget = LanguageChoice("")  # Create an instance of your widget class
widget.show()  # Show the widget
sys.exit(app.exec())  # Start the application's event loop