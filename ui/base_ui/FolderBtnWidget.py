# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FolderBtnWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_folder_btn_widget(object):
    def setupUi(self, folder_btn_widget):
        folder_btn_widget.setObjectName("folder_btn_widget")
        folder_btn_widget.resize(150, 150)
        folder_btn_widget.setMinimumSize(QtCore.QSize(150, 150))
        folder_btn_widget.setMaximumSize(QtCore.QSize(150, 150))
        self.folder_btn = QtWidgets.QPushButton(folder_btn_widget)
        self.folder_btn.setGeometry(QtCore.QRect(5, 5, 140, 140))
        self.folder_btn.setMinimumSize(QtCore.QSize(130, 130))
        self.folder_btn.setMaximumSize(QtCore.QSize(140, 140))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.folder_btn.setFont(font)
        self.folder_btn.setStyleSheet("QPushButton{\n"
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
"    color: rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 8px;\n"
"    border-color: rgb(174, 171, 171);\n"
"    border-style: solid;\n"
"    background-color: rgb(249, 247, 247);\n"
"    margin: 1px;\n"
"    padding: 2px;\n"
"}")
        self.folder_btn.setObjectName("folder_btn")

        self.retranslateUi(folder_btn_widget)
        QtCore.QMetaObject.connectSlotsByName(folder_btn_widget)

    def retranslateUi(self, folder_btn_widget):
        _translate = QtCore.QCoreApplication.translate
        folder_btn_widget.setWindowTitle(_translate("folder_btn_widget", "Form"))
        self.folder_btn.setText(_translate("folder_btn_widget", "Папка"))
