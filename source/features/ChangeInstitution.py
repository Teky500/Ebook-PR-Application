import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import Qt
import yaml
import os
from .helpers.getLanguage import getLanguage

def packagingPath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class ChangeInstitution(QWidget):
    def __init__(self):
        super(ChangeInstitution, self).__init__()

        loadUi(packagingPath("source/features/ui/changeOfInstitution.ui"), self)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)

        if getLanguage() == 1:
            self.cancel_change.setText("Non")
            self.confirm_change.setText("Oui")
            self.label.setText("<b>Cela commencera comme une nouvelle installation, et supprimera toutes les données chargées, êtes-vous sûr?<b>")
            # self.label.setStyleSheet('''font-size: 14pt;
            #                                background-color: #333333;
            #                                 color: #ffffff;
            #                                padding: 5px;
            #                               border-color: #333333;''')
            # self.label_2.setText("<b>et supprimera toutes les données chargées, êtes-vous sûr?<b>")
            # self.label_2.setStyleSheet('''font-size: 14pt;
            #                                background-color: #333333;
            #                                 color: #ffffff;
            #                                padding: 5px;
            #                               border-color: #333333;''')

        self.cancel_change.clicked.connect(self.load_home_page)
        self.confirm_change.clicked.connect(self.start_again)

    def load_home_page(self):
        from .HomePage import SetHomePage
        self.home_page = SetHomePage()
        self.window().hide()
        self.home_page.show()

    def start_again(self):
        from .LanguageChoice import LanguageChoice

        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            yaml_file['Status'] = 0

        with open('source/config/config.yaml', 'w') as config_file:
            yaml.dump(yaml_file, config_file)        

        self.welcome_page = LanguageChoice('N')
        self.welcome_page.show()
        self.window().close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ChangeInstitution()
    widget.show()
    sys.exit(app.exec())