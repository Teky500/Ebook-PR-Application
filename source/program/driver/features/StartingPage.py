import sys
from Themes import Theme, getTheme
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QStackedWidget
from SetInstitutionPage import SetInstitution

theme = Theme(getTheme())
themeColour = theme.getColor()
class WelcomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel(f"Starting", self)

        font = label.font()
        font.setPointSize(35) 
        font.setBold(True)
        label.setFont(font)

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.animate_text)
        self.animation_counter = 0

        self.page_timer = QTimer(self)
        self.page_timer.timeout.connect(self.show_next_page)

        self.animation_timer.start(600)
        self.page_timer.start(5000)

        self.window().setFixedSize(400, 250)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint) 


    def animate_text(self):
        dots = '.' * (self.animation_counter % 4)
        label = self.findChild(QLabel)
        label.setText(f"Starting{dots}")
        self.animation_counter += 1

    def show_next_page(self):
        self.page_timer.stop()
        self.window().close()
        self.openNewWindow()
        
    def setFixedSize(self, width, height):
        super().setFixedSize(width, height)

    def openNewWindow(self):
        global m
        new_window = MainPage()
        m = new_window
        new_window.show()

class MainPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
    
        layout = QVBoxLayout(self)
        institution_widget = SetInstitution()
        layout.addWidget(institution_widget)  
        self.window().resize(963, 571)


        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet("""
    QWidget {
        background-color: #333333;
        color: #ffffff;
        border: none;
    }
    QPushButton {
        background-color: #4d4d4d;
        border: 1px solid #4d4d4d;
        border-radius: 4px;
        color: #ffffff;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #5a5a5a;
        border: 1px solid #5a5a5a;
    }
    QCheckBox {
        color: #ffffff;
    }
    QLineEdit {
        background-color: #4d4d4d;
        border: 1px solid #4d4d4d;
        color: #ffffff;
        padding: 5px;
    }
    QTextEdit {
        background-color: #4d4d4d;
        border: 1px solid #4d4d4d;
        color: #ffffff;
        padding: 5px;
    }
    QProgressBar {
        border: 1px solid #444444;
        border-radius: 7px;
        background-color: #2e2e2e;
        text-align: center;
        font-size: 10pt;
        color: white;
    }
    QProgressBar::chunk {
        background-color: #3a3a3a;
        width: 5px;
    }
    QScrollBar:vertical {
        border: none;
        background-color: #3a3a3a;
        width: 10px;
        margin: 16px 0 16px 0;
    }
    QScrollBar::handle:vertical {
        background-color: #444444;
        border-radius: 5px;
    }
    QScrollBar:horizontal {
        border: none;
        background-color: #3a3a3a;
        height: 10px;
        margin: 0px 16px 0 16px;
    }
    QScrollBar::handle:horizontal {
        background-color: #444444;
        border-radius: 5px;
    }
    QTabWidget {
        background-color: #2e2e2e;
        border: none;
    }
    QTabBar::tab {
        background-color: #2e2e2e;
        color: #b1b1b1;
        padding: 8px 20px;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        border: none;
    }
 
    QTabBar::tab:selected, QTabBar::tab:hover {
        background-color: #3a3a3a;
        color: white;
    }"""
    )
    
    main_window = QWidget()
    main_layout = QVBoxLayout(main_window)
    if themeColour == "default":
        pass
    else:
        main_window.setStyleSheet(f'background-color: {themeColour};')

    stacked_widget = QStackedWidget(main_window)
    welcome_page = WelcomePage(stacked_widget)
    main_page = MainPage(stacked_widget)
  
    stacked_widget.addWidget(welcome_page)
    stacked_widget.addWidget(main_page)

    main_layout.addWidget(stacked_widget)

    
    main_window.show()

    sys.exit(app.exec())

