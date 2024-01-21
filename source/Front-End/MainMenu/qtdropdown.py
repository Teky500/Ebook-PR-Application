import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget
import sqlite3 as sq

class MyMainWindow(QMainWindow):
    db_path = 'source/storage/database/proj.db'
    db = sq.connect(db_path)
    cursor = db.cursor()
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("DropDown")
        self.setGeometry(100, 100, 400, 200)

        # Create a central widget and set a layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a combo box
        combo_box = QComboBox(self)
        combo_box.addItem("Option 1")
        combo_box.addItem("Option 2")
        combo_box.addItem("Option 3")

        # Connect a slot to handle the selection change
        combo_box.currentIndexChanged.connect(self.on_combobox_changed)

        # Add the combo box to the layout
        layout.addWidget(combo_box)

    def on_combobox_changed(self, index):
        # This method will be called when the selection in the combo box changes
        selected_text = self.sender().currentText()
        print(f"Selected option: {selected_text}")
        cursor.execute("SELECT * FROM books LIMIT 10;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
