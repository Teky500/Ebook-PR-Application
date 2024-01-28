import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QPushButton, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Textbox and Buttons Example")
        self.setGeometry(100, 100, 400, 200)

        # Create the central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Create a textbox
        self.textbox = QLineEdit(self)

        # Create a label to display the entered text
        self.display_label = QLabel(self)

        # Create the "Confirm" button
        confirm_button = QPushButton("Confirm", self)
        confirm_button.clicked.connect(self.display_text)

        # Create the "Exit" button
        exit_button = QPushButton("Exit", self)
        exit_button.clicked.connect(self.close)

        # Add widgets to the layout
        layout.addWidget(self.textbox)
        layout.addWidget(confirm_button)
        layout.addWidget(exit_button)
        layout.addWidget(self.display_label)

        central_widget.setLayout(layout)

    def display_text(self):
        entered_text = self.textbox.text()
        self.display_label.setText(f"Entered Text: {entered_text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
