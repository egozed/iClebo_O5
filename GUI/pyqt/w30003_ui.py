# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\PycharmProjects\iClebo_O5\GUI\w30003.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form30003(object):
    def setupUi(self, Form30003):
        Form30003.setObjectName("Form30003")
        Form30003.setWindowModality(QtCore.Qt.WindowModal)
        Form30003.resize(338, 408)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form30003.sizePolicy().hasHeightForWidth())
        Form30003.setSizePolicy(sizePolicy)
        Form30003.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form30003)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_jpg = QtWidgets.QLabel(Form30003)
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
        self.line = QtWidgets.QFrame(Form30003)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form30003)
        self.label.setMinimumSize(QtCore.QSize(17, 20))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_coord_x = QtWidgets.QLabel(Form30003)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_coord_x.sizePolicy().hasHeightForWidth())
        self.label_coord_x.setSizePolicy(sizePolicy)
        self.label_coord_x.setMinimumSize(QtCore.QSize(36, 13))
        self.label_coord_x.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.label_coord_x.setMouseTracking(False)
        self.label_coord_x.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_coord_x.setTextFormat(QtCore.Qt.AutoText)
        self.label_coord_x.setScaledContents(True)
        self.label_coord_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_coord_x.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_coord_x.setObjectName("label_coord_x")
        self.horizontalLayout.addWidget(self.label_coord_x, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_3 = QtWidgets.QFrame(Form30003)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.label_3 = QtWidgets.QLabel(Form30003)
        self.label_3.setMinimumSize(QtCore.QSize(17, 20))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_coord_y = QtWidgets.QLabel(Form30003)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_coord_y.sizePolicy().hasHeightForWidth())
        self.label_coord_y.setSizePolicy(sizePolicy)
        self.label_coord_y.setMinimumSize(QtCore.QSize(36, 13))
        self.label_coord_y.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.label_coord_y.setScaledContents(True)
        self.label_coord_y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_coord_y.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_coord_y.setObjectName("label_coord_y")
        self.horizontalLayout.addWidget(self.label_coord_y, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_5 = QtWidgets.QFrame(Form30003)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.label_5 = QtWidgets.QLabel(Form30003)
        self.label_5.setMinimumSize(QtCore.QSize(30, 20))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_coord_ang = QtWidgets.QLabel(Form30003)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_coord_ang.sizePolicy().hasHeightForWidth())
        self.label_coord_ang.setSizePolicy(sizePolicy)
        self.label_coord_ang.setMinimumSize(QtCore.QSize(36, 13))
        self.label_coord_ang.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.label_coord_ang.setScaledContents(True)
        self.label_coord_ang.setAlignment(QtCore.Qt.AlignCenter)
        self.label_coord_ang.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_coord_ang.setObjectName("label_coord_ang")
        self.horizontalLayout.addWidget(self.label_coord_ang, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(Form30003)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_date = QtWidgets.QLabel(Form30003)
        self.label_date.setScaledContents(True)
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_date.setObjectName("label_date")
        self.horizontalLayout_2.addWidget(self.label_date)
        self.line_6 = QtWidgets.QFrame(Form30003)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_2.addWidget(self.line_6)
        self.label_fVal1 = QtWidgets.QLabel(Form30003)
        self.label_fVal1.setScaledContents(True)
        self.label_fVal1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fVal1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_fVal1.setObjectName("label_fVal1")
        self.horizontalLayout_2.addWidget(self.label_fVal1)
        self.line_7 = QtWidgets.QFrame(Form30003)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_2.addWidget(self.line_7)
        self.label_fVal2 = QtWidgets.QLabel(Form30003)
        self.label_fVal2.setScaledContents(True)
        self.label_fVal2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fVal2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_fVal2.setObjectName("label_fVal2")
        self.horizontalLayout_2.addWidget(self.label_fVal2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_4 = QtWidgets.QFrame(Form30003)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.textBrowser = QtWidgets.QTextBrowser(Form30003)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setSizeIncrement(QtCore.QSize(0, 0))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textBrowser.setTabChangesFocus(True)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textBrowser.setLineWrapColumnOrWidth(0)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setTabStopWidth(80)
        self.textBrowser.setAcceptRichText(False)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)

        self.retranslateUi(Form30003)
        QtCore.QMetaObject.connectSlotsByName(Form30003)

    def retranslateUi(self, Form30003):
        _translate = QtCore.QCoreApplication.translate
        Form30003.setWindowTitle(_translate("Form30003", "ip:30003"))
        self.label.setText(_translate("Form30003", "X ="))
        self.label_coord_x.setText(_translate("Form30003", "-00000.000"))
        self.label_3.setText(_translate("Form30003", "Y ="))
        self.label_coord_y.setText(_translate("Form30003", "-00000.000"))
        self.label_5.setText(_translate("Form30003", "Ang ="))
        self.label_coord_ang.setText(_translate("Form30003", "-000.000"))
        self.label_date.setText(_translate("Form30003", "date time"))
        self.label_fVal1.setText(_translate("Form30003", "0.0"))
        self.label_fVal2.setText(_translate("Form30003", "0.0"))
        self.textBrowser.setHtml(_translate("Form30003", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>"))
