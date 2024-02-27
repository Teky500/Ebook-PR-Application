
# for tpl in list:
#     last_two_items = tpl[-2:]  
#     print(last_two_items)

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

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




