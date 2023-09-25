# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionSID = QAction(MainWindow)
        self.actionSID.setObjectName(u"actionSID")
        self.actionFastDVDNet = QAction(MainWindow)
        self.actionFastDVDNet.setObjectName(u"actionFastDVDNet")
        self.actionData_Augmentation = QAction(MainWindow)
        self.actionData_Augmentation.setObjectName(u"actionData_Augmentation")
        self.actionHeatmaps = QAction(MainWindow)
        self.actionHeatmaps.setObjectName(u"actionHeatmaps")
        self.actionHeatmaps.setCheckable(True)
        self.actionImport_Folder = QAction(MainWindow)
        self.actionImport_Folder.setObjectName(u"actionImport_Folder")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.label_right_image = QLabel(self.centralwidget)
        self.label_right_image.setObjectName(u"label_right_image")

        self.gridLayout_2.addWidget(self.label_right_image, 1, 3, 1, 1)

        self.label_left_image = QLabel(self.centralwidget)
        self.label_left_image.setObjectName(u"label_left_image")

        self.gridLayout_2.addWidget(self.label_left_image, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 1, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(10, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 4, 1, 1)

        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")

        self.gridLayout.addWidget(self.label_logo, 3, 3, 1, 1, Qt.AlignRight)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setMinimumSize(QSize(160, 50))
        font = QFont()
        font.setPointSize(17)
        self.button_start.setFont(font)
        self.button_start.setStyleSheet(u"QPushButton {\n"
"    background-color: \"#00406e\";  /* Korrekt */\n"
"    border: 2px solid blue; /* Korrekt */\n"
"    color: white;            /* Fehlt ein Semikolon, Syntaxfehler */\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: \"#007ec1\";  /* Korrekt */\n"
"    border: 2px solid blue; /* Korrekt */\n"
"    color: white;            /* Fehlt ein Semikolon, Syntaxfehler */\n"
"	border-radius: 5px\n"
"}")

        self.gridLayout.addWidget(self.button_start, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuData = QMenu(self.menubar)
        self.menuData.setObjectName(u"menuData")
        self.menuModel = QMenu(self.menubar)
        self.menuModel.setObjectName(u"menuModel")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuModel.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuData.addAction(self.actionImport)
        self.menuData.addAction(self.actionImport_Folder)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionExport)
        self.menuModel.addAction(self.actionSID)
        self.menuModel.addAction(self.actionFastDVDNet)
        self.menuOptions.addAction(self.actionData_Augmentation)
        self.menuOptions.addAction(self.actionHeatmaps)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CNN Demonstrator", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionSID.setText(QCoreApplication.translate("MainWindow", u"SID", None))
        self.actionFastDVDNet.setText(QCoreApplication.translate("MainWindow", u"FastDVDNet", None))
        self.actionData_Augmentation.setText(QCoreApplication.translate("MainWindow", u"Data Augmentation", None))
        self.actionHeatmaps.setText(QCoreApplication.translate("MainWindow", u"Heatmaps", None))
        self.actionImport_Folder.setText(QCoreApplication.translate("MainWindow", u"Import Folder", None))
        self.label_right_image.setText(QCoreApplication.translate("MainWindow", u"right_image", None))
        self.label_left_image.setText(QCoreApplication.translate("MainWindow", u"left_image", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuData.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.menuModel.setTitle(QCoreApplication.translate("MainWindow", u"Model", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

