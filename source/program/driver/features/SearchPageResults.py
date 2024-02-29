import csv
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self._header_labels = []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]
        
        if role == Qt.ItemDataRole.ToolTipRole:
            return self._data[index.row()][index.column()]


    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal and section < len(self._header_labels):
                return self._header_labels[section]
            elif orientation == Qt.Orientation.Vertical:
                return str(section + 1)

    def setHeaderLabels(self, labels):
        self._header_labels = labels
        self.headerDataChanged.emit(Qt.Orientation.Horizontal, 0, len(labels) - 1)



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, itemData, sType):
        super().__init__()
        self.setStyleSheet("""
             
            QTableView {    
                background-color: #333333;
                alternate-background-color: white;
                selection-background-color: white;
            }

            QHeaderView::section {
                background-color: white; 
                color: #333333; 
                padding: 4px;
                font-weight: bold;
            }
                                       
            QTableView::corner {
            background-color: #333333; 
            }
                           
            QTableView::item {
            background-color: white;
            color: #333333; 
            font-weight: bold;
            }
                           
            """)

        if sType == 0 or sType == 3:
            data = [itemData[0][:-2]]
            print(data)
            data2 = []
            for i in itemData:
                data2.append(i[-2:])
            print(data2)
            main_widget = QWidget()
            self.setCentralWidget(main_widget)
            layout = QVBoxLayout()
            main_widget.setLayout(layout)
            self.table = QtWidgets.QTableView()
            self.table2 = QtWidgets.QTableView()


            self.model = TableModel(data)
            self.model2 = TableModel(data2)
            self.table.setModel(self.model)
            self.table2.setModel(self.model2)

            header_labels = ['eISBN', 'Title', 'Publisher', 'Year', 'OCN']
            self.model.setHeaderLabels(header_labels)

            header_labels2 = ['PA Rights', 'File Path']
            self.model2.setHeaderLabels(header_labels2)

            self.table.resizeColumnsToContents()
            self.table2.resizeColumnsToContents()

            layout.addWidget(self.table)
            layout.addWidget(self.table2)

            # Add a button for downloading
            self.download_button = QPushButton("Download")
            layout.addWidget(self.download_button)
            self.download_button.clicked.connect(self.downloadTable) # backend function here

        if sType == 1 or sType == 2:
            data = itemData
            main_widget = QWidget()
            self.setCentralWidget(main_widget)
            layout = QVBoxLayout()
            main_widget.setLayout(layout)
            self.table = QtWidgets.QTableView()


            self.model = TableModel(data)
            self.table.setModel(self.model)

            header_labels = ['eISBN', 'Title', 'Publisher', 'Year', 'OCN', 'PA Rights','File Path']
            self.model.setHeaderLabels(header_labels)


            self.table.resizeColumnsToContents()

            layout.addWidget(self.table)

            # Add a button for downloading
            self.download_button = QPushButton("Download")
            layout.addWidget(self.download_button)
            self.download_button.clicked.connect(self.downloadTable) # backend function here 


    def generateTableData(self, model):
        data = []

        # Get header data
        header_data = [model.headerData(i, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole) for i in range(model.columnCount(None))]
        data.append(header_data)

        # Get row data
        for row in range(model.rowCount(None)):
            row_data = [model.data(model.index(row, col), Qt.ItemDataRole.DisplayRole) for col in range(model.columnCount(None))]
            data.append(row_data)

        return data

    def downloadTable(self):
        # Get the file path using a file dialog
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV Files (*.csv);;TSV Files (*.tsv)')

        if file_path:
            # Determine delimiter based on file extension
            delimiter = ',' if file_path.endswith('.csv') else '\t'

            # Get data for the first table
            data = self.generateTableData(self.model)

            # For the second table (if applicable)
            if hasattr(self, 'model2'):
                data2 = self.generateTableData(self.model2)
                data.extend(data2)

            # Open the file and write the data
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=delimiter)

                for row_data in data:
                    writer.writerow(row_data)