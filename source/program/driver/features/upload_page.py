import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout
from helpers.manual_upload import man_upload

class FileUploader(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create a layout
        layout = QVBoxLayout()

        # Create a button for file upload
        self.upload_button = QPushButton('Upload File')
        self.upload_button.clicked.connect(self.upload_file)

        # Add the button to the layout
        layout.addWidget(self.upload_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set the window title and size
        self.setWindowTitle('File Uploader')
        self.setGeometry(200, 200, 300, 100)

    def upload_file(self):
        # Open a file dialog to select a file
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*);;Python Files (*.py)')

        if file_path:
            print('Selected File:', file_path)
            man_upload(file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    uploader = FileUploader()
    uploader.show()
    sys.exit(app.exec())
