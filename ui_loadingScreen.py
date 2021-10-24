# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingScreenMEBHUa.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

# import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(582, 307)
        self.splashScreen = QWidget(MainWindow)
        self.splashScreen.setObjectName(u"splashScreen")
        self.verticalLayout = QVBoxLayout(self.splashScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.splashScreen)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-radius: 10px;\n"
"	background-color: #282a36;\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(70, -10, 441, 161))
        self.logo.setStyleSheet(u"\n"
"image:url(Logo_pink.png);\n"
"")
        self.logo.setAlignment(Qt.AlignCenter)
        self.label_desc = QLabel(self.frame)
        self.label_desc.setObjectName(u"label_desc")
        self.label_desc.setGeometry(QRect(0, 130, 561, 31))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(14)
        self.label_desc.setFont(font)
        self.label_desc.setStyleSheet(u"color:#8891b9")
        self.label_desc.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 190, 511, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color:#383a59;\n"
"	color:#8891b9;\n"
"	border-style:none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0.471091, x2:1, y2:0.466, stop:0 rgba(255, 121, 198, 255), stop:1 rgba(170, 85, 255, 255))\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 220, 561, 31))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:#8891b9")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 250, 551, 31))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:#8891b9")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.splashScreen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.label_desc.setText(QCoreApplication.translate("MainWindow", u"<b>APP </b>Description", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Loading...</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Powered by:</span><span style=\" font-size:10pt;\"> Duko Developers</span></p></body></html>", None))
    # retranslateUi

