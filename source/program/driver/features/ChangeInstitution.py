import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget
from PyQt6.QtCore import Qt
import yaml
from .helpers.getLanguage import getLanguage

# from SetInstitutionPage import SetInstitution
# from .helpers.download_excel import downloadFiles

class ChangeInstitution(QWidget):
    def __init__(self):
        super(ChangeInstitution, self).__init__()

        loadUi("source/program/driver/features/ui/changeOfInstitution.ui", self)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # self.confirm_change.clicked.connect(self.reset)
        self.cancel_change.clicked.connect(self.load_home_page)
        self.confirm_change.clicked.connect(self.start_again)

        #If set to french, change text to french
        if getLanguage(self) == 1:
            self.label.setText("Cette modification va réinitialiser votre")
            self.label_2.setText("application, étes-vous sûre?")
            #Make text smaller
            self.label.setStyleSheet("""
    QLabel {
        font: 700 18pt "Segoe UI";
        color: #ffffff;
        background-color: #333333; /* Change color */
        border: 1px solid #333333;
        padding: 5px;
    }
""")
            #Make text smaller
            self.label_2.setStyleSheet("""
    QLabel {
        font: 700 18pt "Segoe UI";
        color: #ffffff;
        background-color: #333333; /* Change color */
        border: 1px solid #333333;
        padding: 5px;
    }
""")
            self.confirm_change.setText("Oui")
            self.cancel_change.setText("Non")

    # # reset function here
    # def reset(self):
    #     if self.getStatus() == 0:
    #         print('Status 0')
    #         downloadFiles()
    #         global m
    #         new_window = SetInstitution()
    #         m = new_window
    #         new_window.run()
 

    def load_home_page(self):
        from .HomePage import SetHomePage
        global m
        new_window = SetHomePage()
        m = new_window
        self.window().hide()
        new_window.show()
    def start_again(self):
        from .StartingPage import WelcomePage
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            yaml_file['Status'] = 0
        with open('source/config/config.yaml', 'w') as config_file:
            yaml.dump(yaml_file, config_file)        

        global m
        m = WelcomePage()
        m.show()
        self.window().close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ChangeInstitution()
    widget.show()
    sys.exit(app.exec())