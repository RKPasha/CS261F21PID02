# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scrapWindowaQvRPW.ui'
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

import res1_rc

class Ui_ScrapWindow(object):
    def setupUi(self, ScrapWindow):
        if ScrapWindow.objectName():
            ScrapWindow.setObjectName(u"ScrapWindow")
        ScrapWindow.resize(826, 569)
        self.centralwidget = QWidget(ScrapWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(40, 42, 54);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 0, 531, 121))
        self.label.setStyleSheet(u"image: url(:/images/Logo_pink.png);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 130, 731, 61))
        self.label_2.setStyleSheet(u"QLabel{\n"
"color: rgb(0, 204, 204);\n"
"border: 2px dashed rgb(255, 121, 198);\n"
"border-radius:12px;\n"
"}")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 200, 371, 221))
        self.label_3.setStyleSheet(u"image: url(:/images/start1.png);")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 380, 91, 81))
        self.label_4.setStyleSheet(u"image: url(:/images/exit-button-orb-1098096-removebg-preview.png);")
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 480, 711, 31))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: #383a59;\n"
"	color: #8891b9;\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.477273, stop:0 rgba(0, 204, 204, 255), stop:1 rgba(255, 121, 198, 255));\n"
"	border-radius: 10px;\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.frame)

        ScrapWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ScrapWindow)

        QMetaObject.connectSlotsByName(ScrapWindow)
    # setupUi

    def retranslateUi(self, ScrapWindow):
        ScrapWindow.setWindowTitle(QCoreApplication.translate("ScrapWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("ScrapWindow", u"     What Mobile gathers data from websites to reveal the latest smartphones.The scrapped data contains feature,price tags, ratings, and reviews. ", None))
        self.label_3.setText("")
        self.label_4.setText("")
    # retranslateUi

