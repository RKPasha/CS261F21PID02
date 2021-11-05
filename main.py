################################################################################
##
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0
##
################################################################################

from os import error
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from numpy import empty
import pandas as pd
import timeit
# ==> SPLASH SCREEN
from ui_loadingScreen import Ui_MainWindow

# ==> SCRAP WINDOW
from ui_scrapWindow import Ui_ScrapWindow

# ==> DATA SET WINDOW
from ui_DataSetWindow import Ui_DataSetWindow

# ==> Algorithms
from Algorithms import sort

# ==> GLOBALS
counter = 0
counter1 = 0
flag = False
dataframe = pd.DataFrame()


class csvRow():
    def __init__(self, dataframe):
        self.Title = dataframe.Title
        self.Ratings = dataframe.Ratings
        self.ScreenSize = dataframe.ScreenSize
        self.Storage = dataframe.Storage
        self.Ram = dataframe.Ram
        self.user_reviews = dataframe.user_reviews
        self.Price = dataframe.Price
        self.Url = dataframe.Url


class CSV():
    def __init__(self, csvData):
        self.row = []
        for i in range(len(csvData)):
            self.row.append(csvRow(csvData[i]))

# ScrapWindow


class ScrapWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ScrapWindow()
        self.ui.setupUi(self)

        global flag
        global dataframe
        # self.ui.run()
        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.ExitBtn.clicked.connect(self.switch)
        self.ui.startBtn.clicked.connect(self.load)

    def progress(self):
        global counter1
  # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter1)
 # CLOSE SPLASH SCREE AND OPEN APP
        if counter1 > 100 and flag:
            # STOP TIMER
            self.timer.stop()
# SHOW MAIN WINDOW
            self.main = DataSetWindow()
            self.main.show()
 # CLOSE SPLASH SCREEN
            self.close()
   # INCREASE COUNTER
        counter1 += 1

    def load(self):
        global flag
        global dataframe
        self.data = Ui_DataSetWindow()
        try:
            if flag:
                flag = False
            else:
                flag = True
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.progress)
            self.timer.start(25)
            dataframe = pd.read_csv("kimovil.csv")
            self.show()
            # print(df.Title)
        except error:
            print(error)

    def switch(self):
        self.dataSet = DataSetWindow()
        self.dataSet.show()
        self.raise_()
        self.hide() == True


class DataSetWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_DataSetWindow()
        self.ui.setupUi(self)
        global dataframe
        import pandas as pd
        if dataframe.empty:
            # print("in if")
            try:
                self.all_data = pd.read_csv('data.csv')
                dataframe = self.all_data
                # self.csv = CSV(list(self.all_data.iloc))
                NumRows = len(self.all_data.index)
                self.ui.tableWidget.setColumnCount(len(self.all_data.columns))
                self.ui.tableWidget.setRowCount(NumRows)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    self.all_data.columns)
                for i in range(NumRows):
                    for j in range(len(self.all_data.columns)):
                        self.ui.tableWidget.setItem(
                            i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.tableWidget.resizeRowsToContents()

            except:
                print("An Error Occured!")
        else:
            try:
                self.all_data = dataframe
                NumRows = len(self.all_data.index)
                # self.csv = CSV(list(self.all_data.iloc))
                self.ui.tableWidget.setColumnCount(len(self.all_data.columns))
                self.ui.tableWidget.setRowCount(NumRows)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    self.all_data.columns)
                for i in range(NumRows):
                    for j in range(len(self.all_data.columns)):
                        self.ui.tableWidget.setItem(
                            i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.tableWidget.resizeRowsToContents()
            except:
                print("An Error Occured!")

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.exitBtn.clicked.connect(sys.exit)
        self.ui.scrapBtn.clicked.connect(self.switch)
        self.ui.sortBtn.clicked.connect(self.sort)
        self.ui.clearBtn.clicked.connect(self.clear)
        self.ui.filterBtn.clicked.connect(self.filter)

    def switch(self):
        self.scrap = ScrapWindow()
        self.scrap.show()
        self.raise_()
        self.hide() == True

    def clear(self):
        # print('clear clicked')
        self.ui.filter_comboBox1.setCurrentIndex(0)
        self.ui.filter_comboBox2.setCurrentIndex(0)
        self.ui.logical_op_comboBox.setCurrentIndex(0)
        self.ui.filter_textBox1.setText("")
        self.ui.filter_textBox2.setText("")

    def filter(self):
        fCombo1 = self.ui.filter_comboBox1.currentIndex()
        fCombo2 = self.ui.filter_comboBox2.currentIndex()
        lCombo = self.ui.logical_op_comboBox.currentIndex()
        fText1 = self.ui.filter_textBox1.toPlainText()
        fText2 = self.ui.filter_textBox2.toPlainText()
        # print(fCombo1, fCombo2, lCombo, fText1, fText2)
        self.clear()

    def refreshWindow(self):
        self.main = DataSetWindow()
        self.main.show()
        self.hide()

    def printSortedDataOnTerminal(self, arr):
        for i in range(len(self.csv.row)):
            print(arr.row[i].Title, ' , ', arr.row[i].Ratings, ' , ', arr.row[i].ScreenSize, ' , ', arr.row[i].Storage, ' , ', arr.row[i].Ram, ' , ', arr.row[i].user_reviews, ' , ', arr.row[i].Price, ' , ', arr.row[i].Url, ' , '
                  )

    def updateTable(self, arr, aCombo):
        if aCombo == 1:
            try:
                self.all_data = dataframe
                NumRows = len(self.all_data.index)
                self.ui.tableWidget.setColumnCount(len(self.all_data.columns))
                self.ui.tableWidget.setRowCount(NumRows)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    self.all_data.columns)
                for i in range(NumRows):
                    self.ui.tableWidget.setItem(
                        i, 0, QTableWidgetItem(str(arr.row[i].Title)))
                    self.ui.tableWidget.setItem(
                        i, 1, QTableWidgetItem(str(arr.row[i].Ratings)))
                    self.ui.tableWidget.setItem(
                        i, 2, QTableWidgetItem(str(arr.row[i].ScreenSize)))
                    self.ui.tableWidget.setItem(
                        i, 3, QTableWidgetItem(str(arr.row[i].Storage)))
                    self.ui.tableWidget.setItem(
                        i, 4, QTableWidgetItem(str(arr.row[i].Ram)))
                    self.ui.tableWidget.setItem(
                        i, 5, QTableWidgetItem(str(arr.row[i].user_reviews)))
                    self.ui.tableWidget.setItem(
                        i, 6, QTableWidgetItem(str(arr.row[i].Price)))
                    self.ui.tableWidget.setItem(
                        i, 7, QTableWidgetItem(str(arr.row[i].Url)))

                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.tableWidget.resizeRowsToContents()
            except:
                print("An Error Occured!")

        elif aCombo == 2:
            try:
                self.all_data = dataframe
                NumRows = len(self.all_data.index)
                self.ui.tableWidget.setColumnCount(len(self.all_data.columns))
                self.ui.tableWidget.setRowCount(NumRows)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    self.all_data.columns)
                for i in range(NumRows):
                    self.ui.tableWidget.setItem(
                        i, 0, QTableWidgetItem(str(arr.row[NumRows-i-1].Title)))
                    self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(
                        str(arr.row[NumRows-i-1].Ratings)))
                    self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(
                        str(arr.row[NumRows-i-1].ScreenSize)))
                    self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(
                        str(arr.row[NumRows-i-1].Storage)))
                    self.ui.tableWidget.setItem(
                        i, 4, QTableWidgetItem(str(arr.row[NumRows-i-1].Ram)))
                    self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(
                        str(arr.row[NumRows-i-1].user_reviews)))
                    self.ui.tableWidget.setItem(
                        i, 6, QTableWidgetItem(str(arr.row[NumRows-i-1].Price)))
                    self.ui.tableWidget.setItem(
                        i, 7, QTableWidgetItem(str(arr.row[NumRows-i-1].Url)))

                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.tableWidget.resizeRowsToContents()
            except:
                print("An Error Occured!")

        elif aCombo == 0:
            QMessageBox.about(
                self, "Alert!", "Please Select an option From Sort By Combo Box")

    def sort(self):
        cCombo = self.ui.col_comboBox.currentIndex()
        aCombo = self.ui.ass_comboBox.currentIndex()
        sCombo = self.ui.sort_comboBox.currentIndex()
        arr = []
        arr1 = []

        def storageFix(str):
            return int(str[:len(str)-2])

        def ratingsFix(str):
            if str == "?":
                return 0.0
            return float(str)

        def scSizeFix(str):
            return float(str.replace("\"", ""))

        def reviewFix(str):
            if str == 'No user reviews':
                return 0
            else:
                str = str.replace(" reviews", '')
                return int(str)

        def priceFix(str):
            str = str.replace("$", '')
            str = str.replace(",", '')
            return int(str)

        if cCombo == 1:
            arr = list(dataframe.Title)
        elif cCombo == 2:
            arr = list(dataframe.Ratings)
        elif cCombo == 3:
            arr = list(dataframe.ScreenSize)
        elif cCombo == 4:
            arr = list(dataframe.Storage)
        elif cCombo == 5:
            arr = list(dataframe.Ram)
        elif cCombo == 6:
            arr = list(dataframe.user_reviews)
        elif cCombo == 7:
            arr = list(dataframe.Price)

        # print(arr)

        if sCombo == 1:
            if cCombo == 1:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                arr = sort.insertionSort(self.csv, arr)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)
                # self.refreshWindow()

            elif cCombo == 2:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(ratingsFix(i))
                arr = sort.insertionSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)
                # self.refreshWindow()

            elif cCombo == 3:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(scSizeFix(i))
                arr = sort.insertionSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)
                # self.refreshWindow()

            elif cCombo == 4 or cCombo == 5:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(storageFix(i))
                arr = sort.insertionSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)
                # self.refreshWindow()

            elif cCombo == 6:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(reviewFix(i))
                arr = sort.insertionSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)
                # self.refreshWindow()

            elif cCombo == 7:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(priceFix(i))
                arr = sort.insertionSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)
                # self.refreshWindow()

        elif sCombo == 2:
            # arr = sort.SelectionSort(arr)
            if cCombo == 1:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                arr = sort.SelectionSort(self.csv, arr)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 2:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(ratingsFix(i))
                arr = sort.SelectionSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 3:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(scSizeFix(i))
                arr = sort.SelectionSort(self.csv, arr1)
                start = timeit.default_timer()
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 4 or cCombo == 5:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(storageFix(i))
                arr = sort.SelectionSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 6:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(reviewFix(i))
                arr = sort.SelectionSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 7:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(priceFix(i))
                arr = sort.SelectionSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

        elif sCombo == 3:
            # arr = sort.BubbleSort(arr)
            if cCombo == 1:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                arr = sort.BubbleSort(self.csv, arr)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 2:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(ratingsFix(i))
                arr = sort.BubbleSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 3:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(scSizeFix(i))
                arr = sort.BubbleSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 4 or cCombo == 5:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(storageFix(i))
                arr = sort.BubbleSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 6:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(reviewFix(i))
                arr = sort.BubbleSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 7:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(priceFix(i))
                arr = sort.BubbleSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

        elif sCombo == 4:
            # arr = sort.quickSort(arr, 0, len(arr)-1)
            if cCombo == 1:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                arr = sort.quickSort(self.csv, arr, 0, len(arr)-1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 2:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(ratingsFix(i))
                arr = sort.quickSort(self.csv, arr1, 0, len(arr1)-1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 3:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)
                for i in arr:
                    arr1.append(scSizeFix(i))
                arr = sort.quickSort(self.csv, arr1, 0, len(arr1)-1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 4 or cCombo == 5:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(storageFix(i))
                arr = sort.quickSort(self.csv, arr1, 0, len(arr1)-1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 6:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(reviewFix(i))
                arr = sort.quickSort(self.csv, arr1, 0, len(arr1)-1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 7:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(priceFix(i))
                arr = sort.quickSort(self.csv, arr1, 0, len(arr1)-1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

        elif sCombo == 5:
            # arr = sort.CountingSort(arr)
            if cCombo == 1 or cCombo == 2 or cCombo == 3:
                QMessageBox.about(
                    self, "Alert!", "Radix Sort can't implement on Floats and Strings")

            elif cCombo == 4 or cCombo == 5:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(storageFix(i))
                arr = sort.CountingSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 6:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(reviewFix(i))
                arr = sort.CountingSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 7:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(priceFix(i))
                arr = sort.CountingSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

        elif sCombo == 6:
            if cCombo == 1 or cCombo == 2 or cCombo == 3:
                QMessageBox.about(
                    self, "Alert!", "Radix Sort can't implement on Floats and Strings")

            elif cCombo == 4 or cCombo == 5:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(storageFix(i))
                arr = sort.RadixSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)
                
            elif cCombo == 6:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(reviewFix(i))
                arr = sort.RadixSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)
                
            elif cCombo == 7:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(priceFix(i))
                arr = sort.RadixSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

        elif sCombo == 7:
            # arr = sort.bucketSort(arr)
            if cCombo == 1:
                QMessageBox.about(
                    self, "Alert!", "Bucket Sort can't implement on Strings")
            elif cCombo == 2:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(ratingsFix(i))
                arr = sort.bucketSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 3:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(scSizeFix(i))
                arr = sort.bucketSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 4 or cCombo == 5:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(storageFix(i))
                arr = sort.bucketSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 6:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(reviewFix(i))
                arr = sort.bucketSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 7:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(priceFix(i))
                arr = sort.bucketSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)


        elif sCombo == 8:
            if cCombo == 1:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                arr = sort.mergeSort(self.csv, arr)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 2:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(ratingsFix(i))
                arr = sort.mergeSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 3:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(scSizeFix(i))
                arr = sort.mergeSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 4 or cCombo == 5:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(storageFix(i))
                arr = sort.mergeSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 6:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(reviewFix(i))
                arr = sort.mergeSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

            elif cCombo == 7:
                self.csv = CSV(list(self.all_data.iloc))
                start = timeit.default_timer()
                for i in arr:
                    arr1.append(priceFix(i))
                arr = sort.mergeSort(self.csv, arr1)
                self.updateTable(arr, aCombo)
                stop = timeit.default_timer()
                Time = stop-start
                self.ui.lcdNumber.display(Time)

        elif sCombo == 9:

            arr = sort.timSort(arr)
            print(arr)

        self.ui.col_comboBox.setCurrentIndex(0)
        self.ui.ass_comboBox.setCurrentIndex(0)
        self.ui.sort_comboBox.setCurrentIndex(0)

# SPLASH SCREEN


class LoadingScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # UI ==> INTERFACE CODES
        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)
        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_desc.setText("<strong>WELCOME</strong> TO WHAT MOBILE")

        # Change Texts
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_desc.setText(
            "<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3500, lambda: self.ui.label_desc.setText(
            "<strong>LOADING</strong> USER INTERFACE"))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter
     # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)
     # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            # SHOW MAIN WINDOW
            self.main = DataSetWindow()
            self.main.show()
            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingScreen()
    sys.exit(app.exec_())
