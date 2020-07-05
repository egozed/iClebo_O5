# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'w30001.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form30001(object):
    def setupUi(self, Form30001):
        if not Form30001.objectName():
            Form30001.setObjectName(u"Form30001")
        Form30001.setWindowModality(Qt.WindowModal)
        Form30001.resize(338, 258)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form30001.sizePolicy().hasHeightForWidth())
        Form30001.setSizePolicy(sizePolicy)
        Form30001.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(Form30001)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_jpg = QLabel(Form30001)
        self.label_jpg.setObjectName(u"label_jpg")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_jpg.sizePolicy().hasHeightForWidth())
        self.label_jpg.setSizePolicy(sizePolicy1)
        self.label_jpg.setMinimumSize(QSize(320, 240))
        self.label_jpg.setScaledContents(True)
        self.label_jpg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_jpg)


        self.retranslateUi(Form30001)

        QMetaObject.connectSlotsByName(Form30001)
    # setupUi

    def retranslateUi(self, Form30001):
        Form30001.setWindowTitle(QCoreApplication.translate("Form30001", u"ip:30001", None))
        self.label_jpg.setText("")
    # retranslateUi

