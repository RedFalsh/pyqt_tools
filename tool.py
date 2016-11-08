# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/xiong/PycharmProjects/qt2py_tools/tool.ui'
#
# Created: Sat Nov  5 16:09:55 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 272)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_py = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_py.setObjectName("pushButton_py")
        self.gridLayout.addWidget(self.pushButton_py, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_ui = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ui.setObjectName("lineEdit_ui")
        self.gridLayout.addWidget(self.lineEdit_ui, 0, 1, 1, 1)
        self.pushButton_ui = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ui.setObjectName("pushButton_ui")
        self.gridLayout.addWidget(self.pushButton_ui, 0, 2, 1, 1)
        self.lineEdit_py = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_py.setObjectName("lineEdit_py")
        self.gridLayout.addWidget(self.lineEdit_py, 1, 1, 1, 1)
        self.pushButton_get = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_get.setObjectName("pushButton_get")
        self.gridLayout.addWidget(self.pushButton_get, 2, 1, 1, 1)
        self.label_inf = QtWidgets.QLabel(self.centralwidget)
        self.label_inf.setObjectName("label_inf")
        self.gridLayout.addWidget(self.label_inf, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_py.setText(_translate("MainWindow", "save py file path"))
        self.label_2.setText(_translate("MainWindow", "py file path"))
        self.label.setText(_translate("MainWindow", "ui file path"))
        self.pushButton_ui.setText(_translate("MainWindow", "open ui file"))
        self.pushButton_get.setText(_translate("MainWindow", "get"))
        self.label_inf.setText(_translate("MainWindow", "information"))

