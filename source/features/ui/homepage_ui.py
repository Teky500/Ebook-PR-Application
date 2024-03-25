# Form implementation generated from reading ui file 'c:\Users\hp\Desktop\VSC\Cloned\Ebook-PR-Application\source\features\ui\homepage.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1092, 683)
        Form.setMinimumSize(QtCore.QSize(700, 500))
        Form.setStyleSheet("  QWidget {\n"
"        background-color: #333333;\n"
"        color: #ffffff;\n"
"        border: none;\n"
"    }\n"
"    QPushButton {\n"
"        background-color: #4d4d4d;\n"
"        border: 1px solid #4d4d4d;\n"
"        border-radius: 4px;\n"
"        color: #ffffff;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #5a5a5a;\n"
"        border: 1px solid #5a5a5a;\n"
"    }\n"
"    QCheckBox {\n"
"        color: #ffffff;\n"
"    }\n"
"    QLineEdit {\n"
"        background-color: #4d4d4d;\n"
"        border: 1px solid #4d4d4d;\n"
"        color: #ffffff;\n"
"        padding: 5px;\n"
"    }\n"
"    QTextEdit {\n"
"        background-color: #4d4d4d;\n"
"        border: 1px solid #4d4d4d;\n"
"        color: #ffffff;\n"
"        padding: 5px;\n"
"    }\n"
"    QProgressBar {\n"
"        border: 1px solid #444444;\n"
"        border-radius: 7px;\n"
"        background-color: #2e2e2e;\n"
"        text-align: center;\n"
"        font-size: 10pt;\n"
"        color: white;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #3a3a3a;\n"
"        width: 5px;\n"
"    }\n"
"    QScrollBar:vertical {\n"
"        border: none;\n"
"        background-color: #3a3a3a;\n"
"        width: 10px;\n"
"        margin: 16px 0 16px 0;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"        background-color: #444444;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QScrollBar:horizontal {\n"
"        border: none;\n"
"        background-color: #3a3a3a;\n"
"        height: 10px;\n"
"        margin: 0px 16px 0 16px;\n"
"    }\n"
"    QScrollBar::handle:horizontal {\n"
"        background-color: #444444;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QTabWidget {\n"
"        background-color: #2e2e2e;\n"
"        border: none;\n"
"    }\n"
"    QTabBar::tab {\n"
"        background-color: #2e2e2e;\n"
"        color: #b1b1b1;\n"
"        padding: 8px 20px;\n"
"        border-top-left-radius: 5px;\n"
"        border-top-right-radius: 5px;\n"
"        border: none;\n"
"    }\n"
" \n"
"    QTabBar::tab:selected, QTabBar::tab:hover {\n"
"        background-color: #3a3a3a;\n"
"        color: white;\n"
"    }")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.switch_language = QtWidgets.QPushButton(parent=Form)
        self.switch_language.setMinimumSize(QtCore.QSize(0, 70))
        self.switch_language.setMaximumSize(QtCore.QSize(260, 70))
        self.switch_language.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.switch_language.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.switch_language.setStyleSheet("    QPushButton {\n"
"        background-color: #333333;\n"
"        border: 1px solid #333333;\n"
"        border-radius: 4px;\n"
"        color: #ffffff;\n"
"        padding: 5px;\n"
"        font: 700 17pt \"Segoe UI\";\n"
"    }\n"
"    QPushButton:hover {\n"
"        font: 700 18pt \"Segoe UI\";\n"
"    }")
        self.switch_language.setObjectName("switch_language")
        self.verticalLayout.addWidget(self.switch_language)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 20, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.set_university_name = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_university_name.sizePolicy().hasHeightForWidth())
        self.set_university_name.setSizePolicy(sizePolicy)
        self.set_university_name.setMaximumSize(QtCore.QSize(1000, 208))
        self.set_university_name.setStyleSheet("font: 700 45pt \"Segoe UI\";")
        self.set_university_name.setText("")
        self.set_university_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.set_university_name.setWordWrap(True)
        self.set_university_name.setObjectName("set_university_name")
        self.horizontalLayout.addWidget(self.set_university_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(5, 20, 5, 70)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.search = QtWidgets.QPushButton(parent=Form)
        self.search.setMinimumSize(QtCore.QSize(100, 70))
        self.search.setMaximumSize(QtCore.QSize(700, 90))
        self.search.setSizeIncrement(QtCore.QSize(0, 0))
        self.search.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.search.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.search.setObjectName("search")
        self.horizontalLayout_5.addWidget(self.search)
        self.change = QtWidgets.QPushButton(parent=Form)
        self.change.setMinimumSize(QtCore.QSize(100, 60))
        self.change.setMaximumSize(QtCore.QSize(550, 80))
        self.change.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.change.setObjectName("change")
        self.horizontalLayout_5.addWidget(self.change)
        self.update = QtWidgets.QPushButton(parent=Form)
        self.update.setMinimumSize(QtCore.QSize(100, 60))
        self.update.setMaximumSize(QtCore.QSize(550, 80))
        self.update.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.update.setObjectName("update")
        self.horizontalLayout_5.addWidget(self.update)
        self.upload = QtWidgets.QPushButton(parent=Form)
        self.upload.setMinimumSize(QtCore.QSize(100, 60))
        self.upload.setMaximumSize(QtCore.QSize(550, 80))
        self.upload.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.upload.setObjectName("upload")
        self.horizontalLayout_5.addWidget(self.upload)
        self.unload = QtWidgets.QPushButton(parent=Form)
        self.unload.setMinimumSize(QtCore.QSize(100, 60))
        self.unload.setMaximumSize(QtCore.QSize(550, 80))
        self.unload.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.unload.setObjectName("unload")
        self.horizontalLayout_5.addWidget(self.unload)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(200, 220, 200, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.exit = QtWidgets.QPushButton(parent=Form)
        self.exit.setMinimumSize(QtCore.QSize(100, 60))
        self.exit.setMaximumSize(QtCore.QSize(180, 80))
        self.exit.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.exit.setObjectName("exit")
        self.horizontalLayout_7.addWidget(self.exit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.switch_language.setText(_translate("Form", "Switch Language (EN)"))
        self.search.setText(_translate("Form", "Search E-book"))
        self.change.setText(_translate("Form", "Reset All"))
        self.update.setText(_translate("Form", "Update CRKN"))
        self.upload.setText(_translate("Form", "Upload Local"))
        self.unload.setText(_translate("Form", "Unload Local"))
        self.exit.setText(_translate("Form", "Exit"))
