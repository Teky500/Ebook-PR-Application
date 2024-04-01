from PyQt6.QtWidgets import  QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtCore import Qt, QTimer, QPoint, QPointF
import yaml
from .HomePage import SetHomePage
from .helpers.getLanguage import getLanguage

class SplashScreen(QWidget):
    def __init__(self, loading_text, size_font):
        super().__init__()
        self.oldPosition = QPointF()

        
        self.loading_text = loading_text
        self.size_font = size_font
        self.setWindowTitle('Splash Screen')
        self.setFixedSize(500, 280)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.initUI()
        self.setStyleSheet('''                   
                           
            QWidget {
                background-color: #333333;
                color: #ffffff;
                border-color: #333333;
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

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.oldPosition = event.globalPosition()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPosition() - self.oldPosition
            window_position = self.window().pos() + delta.toPoint()
            self.window().move(window_position)
            self.oldPosition = event.globalPosition()

    def animate_text(self):
        dots = '.' * (self.animation_counter % 4)
        label = self.findChild(QLabel)
        label.setText(f"{self.loading_text}{dots}")
        self.animation_counter += 1
    
    def show_home_page(self):
        self.home_page = SetHomePage()
        self.home_page.run()
        self.window().close()

