# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddFolderDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_folder_dialog(object):
    def setupUi(self, add_folder_dialog):
        add_folder_dialog.setObjectName("add_folder_dialog")
        add_folder_dialog.resize(380, 240)
        add_folder_dialog.setMinimumSize(QtCore.QSize(380, 240))
        add_folder_dialog.setMaximumSize(QtCore.QSize(380, 300))
        add_folder_dialog.setStyleSheet("QDialog{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QFrame{\n"
"    border-color: rgb(245, 242, 242);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    width: 70px;\n"
"    height: 23px;\n"
"    color: rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 8px;\n"
"    border-color: rgb(174, 171, 171);\n"
"    border-style: solid;\n"
"    background-color: rgb(255, 255, 255);\n"
"    margin: 1px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    width: 70px;\n"
"    height: 23px;\n"
"    color: rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 8px;\n"
"    border-color: rgb(174, 171, 171);\n"
"    border-style: solid;\n"
"    background-color: rgb(249, 247, 247);\n"
"    margin: 1px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-style: solid;\n"
"    border-color: rgb(174, 171, 171);\n"
"    margin: 1px;\n"
"    padding: 2px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.buttonBox = QtWidgets.QDialogButtonBox(add_folder_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 150, 380, 60))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(add_folder_dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 301, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_folder_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_folder_label.sizePolicy().hasHeightForWidth())
        self.name_folder_label.setSizePolicy(sizePolicy)
        self.name_folder_label.setMinimumSize(QtCore.QSize(100, 0))
        self.name_folder_label.setMaximumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.name_folder_label.setFont(font)
        self.name_folder_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_folder_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_folder_label.setWordWrap(True)
        self.name_folder_label.setObjectName("name_folder_label")
        self.horizontalLayout.addWidget(self.name_folder_label)
        self.name_folder = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_folder.sizePolicy().hasHeightForWidth())
        self.name_folder.setSizePolicy(sizePolicy)
        self.name_folder.setMinimumSize(QtCore.QSize(0, 0))
        self.name_folder.setMaximumSize(QtCore.QSize(10000, 23))
        self.name_folder.setObjectName("name_folder")
        self.horizontalLayout.addWidget(self.name_folder)

        self.retranslateUi(add_folder_dialog)
        QtCore.QMetaObject.connectSlotsByName(add_folder_dialog)

    def retranslateUi(self, add_folder_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_folder_dialog.setWindowTitle(_translate("add_folder_dialog", "Создание папки"))
        self.name_folder_label.setText(_translate("add_folder_dialog", "Название папки"))
