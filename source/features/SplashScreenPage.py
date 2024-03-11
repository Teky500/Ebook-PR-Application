import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QHBoxLayout, QVBoxLayout, QFrame, QLabel
from PyQt6.QtCore import Qt, QTimer
import yaml
from .HomePage import SetHomePage
from .helpers.getLanguage import getLanguage

class SplashScreen(QWidget):
    def __init__(self, loading_text, size_font):
        super().__init__()
        self.loading_text = loading_text
        self.size_font = size_font
        self.setWindowTitle('Splash Screen')
        self.setFixedSize(500, 280)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.initUI()
        self.setStyleSheet('''
                                       
        QFrame {
            background-color: #333333;
            color: white;

        }
       
        ''')

    def initUI(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        label = QLabel(f"{self.loading_text}..", self)
        font = label.font()
        font.setPointSize(self.size_font) 
        font.setBold(True)
        label.setFont(font)

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.animate_text)
        self.animation_counter = 0
        self.page_timer = QTimer(self)

        self.animation_timer.start(600)
        self.page_timer.start(5000)

    def animate_text(self):
        dots = '.' * (self.animation_counter % 4)
        label = self.findChild(QLabel)
        label.setText(f"{self.loading_text}{dots}")
        self.animation_counter += 1

    def getLanguage(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            language = yaml_file['Language']
        return language
    
    def show_home_page(self):
        global m
        new_window = SetHomePage()
        m = new_window
        new_window.run()
        self.window().close()

