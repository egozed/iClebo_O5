# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admin\PycharmProjects\iClebo_O5\GUI\w30001.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form30001(object):
    def setupUi(self, Form30001):
        Form30001.setObjectName("Form30001")
        Form30001.setWindowModality(QtCore.Qt.WindowModal)
        Form30001.resize(338, 258)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form30001.sizePolicy().hasHeightForWidth())
        Form30001.setSizePolicy(sizePolicy)
        Form30001.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form30001)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_jpg = QtWidgets.QLabel(Form30001)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_jpg.sizePolicy().hasHeightForWidth())
        self.label_jpg.setSizePolicy(sizePolicy)
        self.label_jpg.setMinimumSize(QtCore.QSize(320, 240))
        self.label_jpg.setText("")
        self.label_jpg.setScaledContents(True)
        self.label_jpg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_jpg.setObjectName("label_jpg")
        self.verticalLayout_2.addWidget(self.label_jpg)

        self.retranslateUi(Form30001)
        QtCore.QMetaObject.connectSlotsByName(Form30001)

    def retranslateUi(self, Form30001):
        _translate = QtCore.QCoreApplication.translate
        Form30001.setWindowTitle(_translate("Form30001", "ip:30001"))
