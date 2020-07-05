# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'w30003.ui'
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


class Ui_Form30003(object):
    def setupUi(self, Form30003):
        if not Form30003.objectName():
            Form30003.setObjectName(u"Form30003")
        Form30003.setWindowModality(Qt.WindowModal)
        Form30003.resize(338, 408)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form30003.sizePolicy().hasHeightForWidth())
        Form30003.setSizePolicy(sizePolicy)
        Form30003.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(Form30003)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_jpg = QLabel(Form30003)
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

        self.line = QFrame(Form30003)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form30003)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(17, 20))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_coord_x = QLabel(Form30003)
        self.label_coord_x.setObjectName(u"label_coord_x")
        sizePolicy.setHeightForWidth(self.label_coord_x.sizePolicy().hasHeightForWidth())
        self.label_coord_x.setSizePolicy(sizePolicy)
        self.label_coord_x.setMinimumSize(QSize(36, 13))
        self.label_coord_x.setMaximumSize(QSize(1000000, 1000000))
        self.label_coord_x.setMouseTracking(False)
        self.label_coord_x.setFrameShadow(QFrame.Plain)
        self.label_coord_x.setTextFormat(Qt.AutoText)
        self.label_coord_x.setScaledContents(True)
        self.label_coord_x.setAlignment(Qt.AlignCenter)
        self.label_coord_x.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_coord_x, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.line_3 = QFrame(Form30003)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.label_3 = QLabel(Form30003)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(17, 20))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_coord_y = QLabel(Form30003)
        self.label_coord_y.setObjectName(u"label_coord_y")
        sizePolicy.setHeightForWidth(self.label_coord_y.sizePolicy().hasHeightForWidth())
        self.label_coord_y.setSizePolicy(sizePolicy)
        self.label_coord_y.setMinimumSize(QSize(36, 13))
        self.label_coord_y.setMaximumSize(QSize(1000000, 1000000))
        self.label_coord_y.setScaledContents(True)
        self.label_coord_y.setAlignment(Qt.AlignCenter)
        self.label_coord_y.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_coord_y, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.line_5 = QFrame(Form30003)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.label_5 = QLabel(Form30003)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(30, 20))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_coord_ang = QLabel(Form30003)
        self.label_coord_ang.setObjectName(u"label_coord_ang")
        sizePolicy.setHeightForWidth(self.label_coord_ang.sizePolicy().hasHeightForWidth())
        self.label_coord_ang.setSizePolicy(sizePolicy)
        self.label_coord_ang.setMinimumSize(QSize(36, 13))
        self.label_coord_ang.setMaximumSize(QSize(1000000, 1000000))
        self.label_coord_ang.setScaledContents(True)
        self.label_coord_ang.setAlignment(Qt.AlignCenter)
        self.label_coord_ang.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_coord_ang, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(Form30003)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_date = QLabel(Form30003)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setScaledContents(True)
        self.label_date.setAlignment(Qt.AlignCenter)
        self.label_date.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_date)

        self.line_6 = QFrame(Form30003)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_6)

        self.label_fVal1 = QLabel(Form30003)
        self.label_fVal1.setObjectName(u"label_fVal1")
        self.label_fVal1.setScaledContents(True)
        self.label_fVal1.setAlignment(Qt.AlignCenter)
        self.label_fVal1.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_fVal1)

        self.line_7 = QFrame(Form30003)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_7)

        self.label_fVal2 = QLabel(Form30003)
        self.label_fVal2.setObjectName(u"label_fVal2")
        self.label_fVal2.setScaledContents(True)
        self.label_fVal2.setAlignment(Qt.AlignCenter)
        self.label_fVal2.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_fVal2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_4 = QFrame(Form30003)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.textBrowser = QTextBrowser(Form30003)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy3)
        self.textBrowser.setSizeIncrement(QSize(0, 0))
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setAutoFormatting(QTextEdit.AutoNone)
        self.textBrowser.setTabChangesFocus(True)
        self.textBrowser.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textBrowser.setLineWrapColumnOrWidth(0)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setTabStopWidth(80)
        self.textBrowser.setAcceptRichText(False)
        self.textBrowser.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.retranslateUi(Form30003)

        QMetaObject.connectSlotsByName(Form30003)
    # setupUi

    def retranslateUi(self, Form30003):
        Form30003.setWindowTitle(QCoreApplication.translate("Form30003", u"ip:30003", None))
        self.label_jpg.setText("")
        self.label.setText(QCoreApplication.translate("Form30003", u"X =", None))
        self.label_coord_x.setText(QCoreApplication.translate("Form30003", u"-00000.000", None))
        self.label_3.setText(QCoreApplication.translate("Form30003", u"Y =", None))
        self.label_coord_y.setText(QCoreApplication.translate("Form30003", u"-00000.000", None))
        self.label_5.setText(QCoreApplication.translate("Form30003", u"Ang =", None))
        self.label_coord_ang.setText(QCoreApplication.translate("Form30003", u"-000.000", None))
        self.label_date.setText(QCoreApplication.translate("Form30003", u"date time", None))
        self.label_fVal1.setText(QCoreApplication.translate("Form30003", u"0.0", None))
        self.label_fVal2.setText(QCoreApplication.translate("Form30003", u"0.0", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form30003", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
    # retranslateUi

