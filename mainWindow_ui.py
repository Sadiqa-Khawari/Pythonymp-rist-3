# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.varoitapushButton = QPushButton(self.centralwidget)
        self.varoitapushButton.setObjectName(u"varoitapushButton")
        self.varoitapushButton.setGeometry(QRect(140, 20, 75, 23))
        self.varoitapushButton.setFont(font)
        self.varoitapushButton.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 113, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 80, 121, 16))
        self.TulostapushButton = QPushButton(self.centralwidget)
        self.TulostapushButton.setObjectName(u"TulostapushButton")
        self.TulostapushButton.setGeometry(QRect(250, 20, 75, 23))
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(10)
        self.TulostapushButton.setFont(font1)
        self.TulostapushButton.setStyleSheet(u"background-color: rgb(212, 98, 46);")
        self.LanguageGroupBox = QGroupBox(self.centralwidget)
        self.LanguageGroupBox.setObjectName(u"LanguageGroupBox")
        self.LanguageGroupBox.setGeometry(QRect(10, 110, 161, 131))
        self.FinnishRadioButton = QRadioButton(self.LanguageGroupBox)
        self.FinnishRadioButton.setObjectName(u"FinnishRadioButton")
        self.FinnishRadioButton.setGeometry(QRect(10, 20, 82, 17))
        self.SwedishRadioButton = QRadioButton(self.LanguageGroupBox)
        self.SwedishRadioButton.setObjectName(u"SwedishRadioButton")
        self.SwedishRadioButton.setEnabled(True)
        self.SwedishRadioButton.setGeometry(QRect(10, 50, 82, 17))
        self.tulostettuLabel = QLabel(self.centralwidget)
        self.tulostettuLabel.setObjectName(u"tulostettuLabel")
        self.tulostettuLabel.setGeometry(QRect(370, 20, 161, 21))
        font2 = QFont()
        font2.setPointSize(16)
        self.tulostettuLabel.setFont(font2)
        self.tulostettuLabel.setStyleSheet(u"color: rgb(255, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lineEdit.textChanged.connect(self.label.setText)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.varoitapushButton.setText(QCoreApplication.translate("MainWindow", u"Vaara", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.TulostapushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
        self.LanguageGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Kielivalinta", None))
        self.FinnishRadioButton.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.SwedishRadioButton.setText(QCoreApplication.translate("MainWindow", u"Ruotsi", None))
        self.tulostettuLabel.setText(QCoreApplication.translate("MainWindow", u"Ei tulostettu", None))
    # retranslateUi

