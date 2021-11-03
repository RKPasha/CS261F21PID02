# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_DataSetWindowzZCRQB.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys


from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *





class Ui_DataSetWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1116, 724)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1091, 121))
        self.label.setStyleSheet(u"image: url(Logo_pink.png);")
        self.clearBtn = QPushButton(self.frame)
        self.clearBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setGeometry(QRect(430, 200, 101, 31))
        self.clearBtn.setStyleSheet(u"QPushButton{\n"
"	font: 75 11pt \"Comic Sans MS\";\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}"
"QPushButton::hover{\n"
"background-color: rgb(250, 250, 245);\n"
"border-radius: 15px;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"}")
        self.filter_comboBox1 = QComboBox(self.frame)
        self.filter_comboBox1.addItem("")
        self.filter_comboBox1.addItem("")
        self.filter_comboBox1.setObjectName(u"filter_comboBox1")
        self.filter_comboBox1.setGeometry(QRect(40, 130, 161, 31))
        self.filter_comboBox1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 63 10pt \"Lucida Bright\";")
        self.sort_comboBox = QComboBox(self.frame)
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.setObjectName(u"sort_comboBox")
        self.sort_comboBox.setGeometry(QRect(750, 580, 161, 31))
        self.sort_comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 63 10pt \"Lucida Bright\";")
        self.sortBtn = QPushButton(self.frame)
        self.sortBtn.setObjectName(u"sortBtn")
        self.sortBtn.setGeometry(QRect(500, 640, 132, 41))
        self.sortBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 204, 204);\n"
"border-radius: 15px;\n"
"font: 75 11pt \"Comic Sans MS\";\n"
"}"
"QPushButton::hover{\n"
"background-color: rgb(0, 210, 210);\n"
"border-radius: 15px;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"}")
        self.logical_op_comboBox = QComboBox(self.frame)
        self.logical_op_comboBox.addItem("")
        self.logical_op_comboBox.addItem("")
        self.logical_op_comboBox.setObjectName(u"logical_op_comboBox")
        self.logical_op_comboBox.setGeometry(QRect(450, 130, 161, 31))
        self.logical_op_comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 63 10pt \"Lucida Bright\";")
        self.tableWidget = QTableWidget(self.frame)
        # if (self.tableWidget.columnCount() < 9):
        #     self.tableWidget.setColumnCount(9)
        # __qtablewidgetitem = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        # __qtablewidgetitem1 = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        # __qtablewidgetitem2 = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        # __qtablewidgetitem3 = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        # __qtablewidgetitem4 = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        # __qtablewidgetitem5 = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        # __qtablewidgetitem6 = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        # __qtablewidgetitem7 = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        # __qtablewidgetitem8 = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 260, 1051, 301))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.filter_textBox2 = QTextEdit(self.frame)
        self.filter_textBox2.setObjectName(u"filter_textBox2")
        self.filter_textBox2.setGeometry(QRect(880, 130, 161, 31))
        self.filter_textBox2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.filter_comboBox2 = QComboBox(self.frame)
        self.filter_comboBox2.addItem("")
        self.filter_comboBox2.addItem("")
        self.filter_comboBox2.setObjectName(u"filter_comboBox2")
        self.filter_comboBox2.setGeometry(QRect(660, 130, 161, 31))
        self.filter_comboBox2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 63 10pt \"Lucida Bright\";")
        self.filterBtn = QPushButton(self.frame)
        self.filterBtn.setObjectName(u"filterBtn")
        self.filterBtn.setGeometry(QRect(560, 200, 101, 31))
        self.filterBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.filterBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 204, 204);\n"
"border-radius: 15px;\n"
"font: 75 11pt \"Comic Sans MS\";\n"
"}"
"QPushButton::hover{\n"
"background-color: rgb(0, 210, 210);\n"
"border-radius: 15px;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"}")
        self.filter_textBox1 = QTextEdit(self.frame)
        self.filter_textBox1.setObjectName(u"filter_textBox1")
        self.filter_textBox1.setGeometry(QRect(250, 130, 161, 31))
        self.filter_textBox1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.exitBtn = QPushButton(self.frame)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setGeometry(QRect(1010, 650, 71, 41))
        self.exitBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(195, 0, 0);\n"
"border-radius: 15px;\n"
"font: 75 11pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(180, 0, 0);\n"
"border-radius: 15px;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"}")
        self.col_comboBox = QComboBox(self.frame)
        self.col_comboBox.addItem("")
        self.col_comboBox.addItem("")
        self.col_comboBox.addItem("")
        self.col_comboBox.addItem("")
        self.col_comboBox.addItem("")
        self.col_comboBox.addItem("")
        self.col_comboBox.addItem("")
        self.col_comboBox.addItem("")
        self.col_comboBox.setObjectName(u"col_comboBox")
        self.col_comboBox.setGeometry(QRect(250, 580, 161, 31))
        self.col_comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 63 10pt \"Lucida Bright\";")
        self.ass_comboBox = QComboBox(self.frame)
        self.ass_comboBox.addItem("")
        self.ass_comboBox.addItem("")
        self.ass_comboBox.addItem("")
        self.ass_comboBox.setObjectName(u"ass_comboBox")
        self.ass_comboBox.setGeometry(QRect(490, 580, 161, 31))
        self.ass_comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 63 10pt \"Lucida Bright\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(850, 220, 131, 21))
        self.label_2.setStyleSheet(u"font: 75 16pt \"Comic Sans MS\";\n"
"color: rgb(255, 121, 198);")
        self.lcdNumber = QLCDNumber(self.frame)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(980, 220, 71, 23))
        self.scrapBtn = QPushButton(self.frame)
        self.scrapBtn.setObjectName(u"scrapBtn")
        self.scrapBtn.setGeometry(QRect(20, 650, 151, 41))
        self.scrapBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 204, 204);\n"
"border-radius: 15px;\n"
"font: 75 11pt \"Comic Sans MS\";\n"
"}"
"QPushButton::hover{\n"
"background-color: rgb(0, 210, 210);\n"
"border-radius: 15px;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"}")
        # self.loadBtn = QPushButton(self.frame)
        # self.loadBtn.setObjectName(u"loadBtn")
        # self.loadBtn.setGeometry(QRect(70, 200, 101, 31))
        # self.loadBtn.setStyleSheet(u"QPushButton{\n"
# "	font: 75 11pt \"Comic Sans MS\";\n"
# "	background-color: rgb(255, 255, 255);\n"
# "    border-radius: 15px;\n"
# "}"
# "QPushButton::hover{\n"
# "background-color: rgb(250, 250, 245);\n"
# "border-radius: 15px;\n"
# "font: 75 13pt \"Comic Sans MS\";\n"
# "}")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dataset Window", None))
        self.label.setText("")
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.filter_comboBox1.setItemText(0, QCoreApplication.translate("MainWindow", u"Is Equal to ", None))
        self.filter_comboBox1.setItemText(1, QCoreApplication.translate("MainWindow", u"Not Equal to ", None))

        self.sort_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"--Sorting Algorithm--", None))
        self.sort_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Insertion Sort", None))
        self.sort_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Slection Sort", None))
        self.sort_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Bubble Sort", None))
        self.sort_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Quick Sort", None))
        self.sort_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Counting Sort", None))
        self.sort_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Radix Sort", None))
        self.sort_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Bucket Sort", None))
        self.sort_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Merge Sort", None))
        self.sort_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Tim Sort", None))

        # self.loadBtn.clicked.connect(self.run)
        




        self.sortBtn.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.sortBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.logical_op_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Or", None))
        self.logical_op_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"And", None))

        # ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        # ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Sr No", None));
        # ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        # ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Model", None));
        # ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        # ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        # ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        # ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ram", None));
        # ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        # ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Storage", None));
        # ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        # ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Sc Size ", None));
        # ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        # ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Color", None));
        # ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        # ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Review", None));
        # ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        # ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"URL", None));
        self.filter_comboBox2.setItemText(0, QCoreApplication.translate("MainWindow", u"Is Equal to ", None))
        self.filter_comboBox2.setItemText(1, QCoreApplication.translate("MainWindow", u"Not Equal to ", None))

        self.filterBtn.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.exitBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.col_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"--Select Column--", None))
        self.col_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Title", None))
        self.col_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Ratings", None))
        self.col_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Screen Size", None))
        self.col_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Storage", None))
        self.col_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"RAM", None))
        self.col_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"User Review", None))
        self.col_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Price", None))

        self.ass_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"--Sort By--", None))
        self.ass_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Asscending", None))
        self.ass_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Descending", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Time Taken:", None))
        self.scrapBtn.setText(QCoreApplication.translate("MainWindow", u"Scrap More Data", None))
        self.scrapBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # self.loadBtn.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        # self.loadBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    # retranslateUi
    def run(self):
                print("run called")
                import pandas as pd
                try:
                        self.all_data = pd.read_csv('kimovil.csv')
                except:
                        print("An Error Occured!")
                NumRows = len(self.all_data.index)
                self.tableWidget.setColumnCount(len(self.all_data.columns))
                self.tableWidget.setRowCount(NumRows)
                self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)
                for i in range(NumRows):
                        for j in range(len(self.all_data.columns)):
                                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.resizeRowsToContents()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_DataSetWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())