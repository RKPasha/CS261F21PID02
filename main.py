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

# ==> SPLASH SCREEN
from ui_loadingScreen import Ui_MainWindow

# ==> SCRAP WINDOW
from ui_scrapWindow import Ui_ScrapWindow

# ==> DATA SET WINDOW
from ui_DataSetWindow import Ui_DataSetWindow

# ==> GLOBALS
counter = 0
counter1 = 0
flag = False

# ScrapWindow


class ScrapWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ScrapWindow()
        self.ui.setupUi(self)

        global flag
        # self.ui.run()
        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.ExitBtn.clicked.connect(self.switch)
        self.ui.startBtn.clicked.connect(self.load)

        Title = []
        Rating = []
        Screen_size = []
        Storage = []
        Ram = []
        User_review = []
        Price = []
        Url = []

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
        self.data = Ui_DataSetWindow()
        import pandas as pd
        try:
            if flag:
                flag = False
            else:
                flag = True
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.progress)
            self.timer.start(25)
            df = pd.read_csv("kimovil1.csv")
            Title = df.Title
            Rating = df.Ratings
            Screen_size = df.ScreenSize
            Storage = df.Storage
            Ram = df.RAM
            User_review = df.user_reviews
            Price = df.Price
            Url = df.URL
            dataframe = pd.DataFrame({'Title': Title, 'Rating': Rating, 'Screen_size': Screen_size,
                                     'Storage': Storage, 'Ram': Ram, 'User_review': User_review, 'Price': Price, 'Url': Url})
            self.show()
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
        import pandas as pd
        try:
            self.all_data = pd.read_csv('kimovil.csv')
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
        print(fCombo1, fCombo2, lCombo, fText1, fText2)
        self.clear()

    def sort(self):
        cCombo = self.ui.col_comboBox.currentIndex()
        aCombo = self.ui.ass_comboBox.currentIndex()
        sCombo = self.ui.sort_comboBox.currentIndex()
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
