#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os
try:
    os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")
except:
    pass
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
except ImportError:
    pass
try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PyQt5.QtWinExtras import QtWin
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

import resources

# import imutils
# import random
# from PIL import Image

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(180, 0))
        self.widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_3.setIcon(QIcon(':/fullscreen_button.png'))
        self.pushButton_2.setIcon(QIcon(':/save_button.png'))
        self.pushButton.setIcon(QIcon(':/folder_open_button.png'))

        spacerItem = QtWidgets.QSpacerItem(20, 176, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        #Added code here
        self.widget_2.setMinimumSize(QtCore.QSize(420, 500))
        sizePolicy_2 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.widget_2.setSizePolicy(sizePolicy_2)
        #Ended code here
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        # Added code here
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 2, 1)
        # Ended code here
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("../../eye_chart.png"))
        # Added code here
        self.label.setMinimumSize(420, 500)
        # Ended code here
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        # start added code
        self.gridLayout.addWidget(self.label, 0, 1, 2, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 534, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("background-color: #282828")
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.horizontalLayout.addWidget(self.widget_2)
        # end added code
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(380, 16777215))
        self.widget_3.setObjectName("widget_3")
        #self.widget_3.setStyleSheet("background-color: #282828")
        # START CODE
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 4, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.widget_3)
        # https://stackoverflow.com / questions / 64617155 / how - to - prevent - to - change - sliders - value - by - clicking - on - slider - in -pyqt
        self.verticalSlider_2.setPageStep(0)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout_3.addWidget(self.verticalSlider_2, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 3, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.spinBox = QtWidgets.QSpinBox(self.widget_3)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_2.addWidget(self.spinBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalSlider_3 = QtWidgets.QSlider(self.widget_3)
        self.verticalSlider_3.setPageStep(0)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.horizontalLayout_2.addWidget(self.verticalSlider_3)
        spacerItem9 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_3)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_4.addWidget(self.spinBox_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalSlider = QtWidgets.QSlider(self.widget_3)
        self.verticalSlider.setPageStep(0)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_2.addWidget(self.verticalSlider, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 3)
        spacerItem10 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 0, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout_3.addWidget(self.doubleSpinBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.widget_3)
        # END CODE
        """
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 4, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.widget_3)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_2.setMaximum(100)
        # https://stackoverflow.com / questions / 64617155 / how - to - prevent - to - change - sliders - value - by - clicking - on - slider - in -pyqt
        self.verticalSlider_2.setPageStep(0)
        self.gridLayout_3.addWidget(self.verticalSlider_2, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 3, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.spinBox = QtWidgets.QSpinBox(self.widget_3)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(100)
        self.verticalLayout_2.addWidget(self.spinBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalSlider = QtWidgets.QSlider(self.widget_3)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setPageStep(0)
        self.gridLayout_2.addWidget(self.verticalSlider, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 0, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setMaximum(100)
        self.verticalLayout_3.addWidget(self.doubleSpinBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        """

        """
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(self.widget_3)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        # https://stackoverflow.com/questions/64617155/how-to-prevent-to-change-sliders-value-by-clicking-on-slider-in-pyqt
        self.verticalSlider.setPageStep(0)
        self.gridLayout_2.addWidget(self.verticalSlider, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 3, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 4, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.widget_3)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_2.setPageStep(0)
        self.gridLayout_3.addWidget(self.verticalSlider_2, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.widget_3)
        """
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menuFile)
        self.menuView.setObjectName("menuView")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':/folder_open.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")

        self.actionSave = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(':/save.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")

        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(':/content_copy.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon2)
        self.actionCopy.setObjectName("actionCopy")

        #self.actionPase = QtWidgets.QAction(MainWindow)
        #icon3 = QtGui.QIcon()
        #icon3.addPixmap(QtGui.QPixmap(":/content_paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.actionPase.setIcon(icon3)
        #self.actionPase.setObjectName("actionPase")

        self.actionFullScreen = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFullScreen.setIcon(icon4)
        self.actionFullScreen.setObjectName("actionFullScreen")

        self.actionExitFullScreen = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/fullscreen_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExitFullScreen.setIcon(icon5)
        self.actionExitFullScreen.setObjectName("actionExitFullScreen")

        #self.actionExit = QtWidgets.QAction(MainWindow)
        #icon5 = QtGui.QIcon()
        #icon5.addPixmap(QtGui.QPixmap(":/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.actionExit.setIcon(icon5)
        #self.actionExit.setObjectName("actionExit")

        self.actionInformation = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInformation.setIcon(icon6)
        self.actionInformation.setObjectName("actionInformation")

        self.actionUser_Manual = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/import_contacts.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUser_Manual.setIcon(icon7)
        self.actionUser_Manual.setObjectName("actionUser_Manual")

        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/visibility.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuView.setIcon(icon8)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        #self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        #self.menuEdit.addAction(self.actionPase)
        self.menuFile.addAction(self.menuView.menuAction())
        self.menuHelp.addAction(self.actionInformation)
        self.menuHelp.addAction(self.actionUser_Manual)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuView.addAction(self.actionExitFullScreen)
        self.menuView.addAction(self.actionFullScreen)

        self.retranslateUi(MainWindow)
        self.verticalSlider.valueChanged['int'].connect(self.noise_value)
        self.verticalSlider_2.valueChanged['int'].connect(self.brightness_value)
        self.verticalSlider_3.valueChanged['int'].connect(self.blur_value)
        self.pushButton.clicked.connect(self.loadImage)
        self.pushButton_2.clicked.connect(self.savePhoto)
        self.pushButton_3.clicked.connect(self.switchFullScreen)
        self.pushButton_4.clicked.connect(self.switchFullScreen)
        # https://www.youtube.com/watch?v=6_I03zHlhjA
        self.verticalSlider_2.valueChanged['int'].connect(self.spinBox.setValue)
        self.verticalSlider.valueChanged['int'].connect(self.doubleSpinBox.setValue)
        self.verticalSlider_3.valueChanged['int'].connect(self.spinBox_2.setValue)
        self.spinBox.valueChanged['int'].connect(self.verticalSlider_2.setValue)
        self.spinBox_2.valueChanged['int'].connect(self.verticalSlider_3.setValue)
        self.doubleSpinBox.valueChanged['double'].connect(self.verticalSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionNew.triggered.connect(lambda: self.loadImage())
        #self.actionPase.triggered.connect(lambda: self.loadImage())
        self.actionSave.triggered.connect(lambda: self.savePhoto())
        #self.actionExit.triggered.connect(lambda: self.exit_window())
        self.actionExitFullScreen.triggered.connect(lambda: self.exit_full())
        self.actionFullScreen.triggered.connect(lambda: self.full_view())

        # Added code here
        self.filename = None  # Will hold the image address location
        self.savefilename = None  # Will hold saved image address
        self.tmp = None  # Will hold the temporary image for display
        self.brightness_value_now = 0  # Updated brightness value
        self.blur_value_now = 0  # Updated blur value
        self.noise_value_now = 0  # Updated noise value

        try:
            style = QtCore.QFile(":stylesheet")
            style.open(QtCore.QIODevice.ReadOnly)
            #app.setStyleSheet(((style.readAll()).data()).decode("latin1"))
            app.setStyleSheet(QtCore.QTextStream(style).readAll())
        except:
            pass

        if self.filename == "":
            self.pushButton_4.hide()
        elif self.filename is None:
            self.pushButton_4.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VSS Diagnostic"))
        self.pushButton.setText(_translate("MainWindow", " Open         "))
        self.pushButton_2.setText(_translate("MainWindow", " Save          "))
        self.pushButton_3.setText(_translate("MainWindow", "Fullscreen"))
        self.pushButton_4.setText(_translate("MainWindow", "⛶"))
        self.label_4.setText(_translate("MainWindow",
                                        "Adjust the sliders to customize the amount of noise and brightness added to the image. "))
        self.label_2.setText(_translate("MainWindow", "Salt & Pepper Noise"))
        self.label_3.setText(_translate("MainWindow", "Brightness"))
        self.label_5.setText(_translate("MainWindow", "Blur"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))

        self.actionNew.setText(_translate("MainWindow", "Open"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Open a new image"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+O"))

        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save an image"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy an image or value"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))

        #self.actionPase.setText(_translate("MainWindow", "Paste"))
        #self.actionPase.setStatusTip(_translate("MainWindow", "Paste an Image"))
        #self.actionPase.setShortcut(_translate("MainWindow", "Ctrl+V"))

        self.actionFullScreen.setText(_translate("MainWindow", "FullScreen"))
        self.actionFullScreen.setStatusTip(_translate("MainWindow", "Present the image in FullScreen"))
        self.actionFullScreen.setShortcut(_translate("MainWindow", "Ctrl+F"))

        self.actionExitFullScreen.setText(_translate("MainWindow", "Default"))
        self.actionExitFullScreen.setStatusTip(_translate("MainWindow", "Present the default view of image"))
        self.actionExitFullScreen.setShortcut(_translate("MainWindow", "Esc"))

        #self.actionExit.setText(_translate("MainWindow", "Exit"))
        #self.actionExit.setStatusTip(_translate("MainWindow", "Close the application"))
        #self.actionExit.setShortcut(_translate("MainWindow", "Alt+X"))

        self.actionInformation.setText(_translate("MainWindow", "Information"))
        self.actionUser_Manual.setText(_translate("MainWindow", "User Manual"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def loadImage(self):
        """ This function will load the user selected image
            and set it to label using the setPhoto function
        """
        # Beginning of application no file at all.
        if self.filename is None:
            self.filename = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")[0]
            self.conditions("Please pick an image to use this application.")
        # You pressed open and then you clikced cancel.
        elif self.filename == "":
            self.filename = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")[0]
            self.conditions("Please pick an image to use this application.")

        # An image file already exists in the application.
        else:
            # image present in the application but not saved.
            if self.savefilename == None:
                question = QtWidgets.QMessageBox.question(self, "Confirm",
                                                          "Are you sure you want to choose a new image?\nAll changes to the current image will be lost.",
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
                                                          QtWidgets.QMessageBox.No)
                # I am sure I don't want to save
                if question == QtWidgets.QMessageBox.Yes:
                    self.verticalSlider.setValue(0.0)
                    self.verticalSlider_2.setValue(0)
                    self.filename = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")[0]
                    self.conditions("Please choose a valid image file.\nThe image configuration has not been saved.")
            # image present in the application, you clicked save, but then clicked cancel. Basically not saved in this case also.
            elif self.savefilename == "":
                question = QtWidgets.QMessageBox.question(self, "Confirm",
                                                          "Are you sure you want to choose a new image?\nAll changes to the current image will be lost.",
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
                                                          QtWidgets.QMessageBox.No)
                if question == QtWidgets.QMessageBox.Yes:
                    self.verticalSlider.setValue(0)
                    self.verticalSlider_2.setValue(0)
                    self.filename = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")[0]
                    self.conditions("Please choose a valid image file.\nThe image configuration has not been saved.")

            # image present in the application and saved
            # HERE ALSO THERE IS THE PROBLEM! If the image is saved once, then you make changes to the same image, it doesn't recognize those changes as the savefilename is still the same. Somehow maybe have to connect the slider change function to this.
            # Basically above problem is same as the problem with the application closing.
            elif self.savefilename is not None and self.brightness_value_now != 0 or self.noise_value_now != 0 or self.blur_value_now != 0:
                question = QtWidgets.QMessageBox.question(self, "Confirm",
                                                          "Are you sure you want to choose a new image?\nOnly the last saved changes to the image will be available.",
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
                                                          QtWidgets.QMessageBox.No)
                if question == QtWidgets.QMessageBox.Yes:
                    self.verticalSlider.setValue(0)
                    self.verticalSlider_2.setValue(0)
                    self.filename = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")[0]
                    self.conditions("Please choose a valid image file.\nThe image configuration has not been saved.")

            else:
                self.verticalSlider.setValue(0.0)
                self.verticalSlider_2.setValue(0)
                self.filename = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")[0]
                # this is for the case that you save an image, and then you choose a new image (the savefilename has to get reset cause it's a new image.)
                self.savefilename = None
                self.conditions("Please choose a valid image file.\nOnly the last saved configuration is available.")

    # JUMP
    # You press open, then cancel the application
    def conditions(self, text1):
        # pressed open and then cancel, and this becomes the filename
        if self.filename == "":
            self.popup_critical(text1)
        # you never pressed open (actually I think this one doesn't make sense here cause how can you never press open after pressing open? But still I've left it here for now. If it's really unnecesary we can remove later)
        elif self.filename is None:
            self.popup_critical(text1)
            return False
        else:
            self.image = cv2.imread(self.filename)
            self.setPhoto(self.image)
            self.pushButton_4.show()

    def popup_critical(self, text):
        self.removePhoto()
        self.pushButton_4.hide()
        choose_img = QMessageBox()
        choose_img.setIcon(QMessageBox.Critical)
        choose_img.setText("Information")
        choose_img.setInformativeText(text)
        choose_img.setWindowTitle("Instruction")
        choose_img.exec_()
        return False

    def popup_warning(self, text, text1):
        choose_img = QMessageBox()
        choose_img.setIcon(QMessageBox.Warning)
        choose_img.setText("Warning!")
        choose_img.setInformativeText(text)
        choose_img.setWindowTitle(text1)
        choose_img.exec_()
        # self.loadImage()
        return False

    def setPhoto(self, image):
        """ This function will take image input and resize it
            only for display purpose and convert it to QImage
            to set at the label.
        """
        """
        self.tmp = image
        # image = imutils.resize(image, height=890)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        #self.label.setPixmap(QtGui.QPixmap.fromImage(image))
        self.label.setPixmap(
            QtGui.QPixmap.fromImage(image).scaled(self.label.height(), self.label.width(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        """
        self.tmp = image
        # image = imutils.resize(image, height=890)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap(image)
        #self.label.setPixmap(self.pixmap)
        self.label.setPixmap(self.pixmap.scaled(
            self.widget_2.size(), QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation))
        # this ensures the label can also re-size downwards
        self.label.setMinimumSize(1, 1)
        # get resize events for the label
        self.label.installEventFilter(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

    #https: // stackoverflow.com / questions / 27676034 / pyqt - place - scaled - image - in -centre - of - label
    def eventFilter(self, source, event):
        if (source is self.label and event.type() == QtCore.QEvent.Resize):
            # re-scale the pixmap when the label resizes
            self.label.setPixmap(self.pixmap.scaled(
                self.widget_2.size(), QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation))
        return super(MainWindow, self).eventFilter(source, event)

    def removePhoto(self):
        """ This function will take image input and resize it
            only for display purpose and convert it to QImage
            to set at the label.
        """
        self.label.clear()

    def brightness_value(self, value):
        """ This function will take value from the slider
            for the brightness from 0 to 99
        """
        # if no file is chosen
        if self.filename is None:
            self.popup_warning('Please pick an image before trying to adjust the slider values.', "Warning- Pick image")
        # if you clicked open and then cancel, the filename becomes "".
        elif self.filename == "":
            self.popup_warning('Please pick an image before trying to adjust the slider values.', "Warning- Pick image")
        else:
            global bv
            self.brightness_value_now = value
            print('Brightness: ', value)
            bv = str(value)
            self.update()

    def noise_value(self, value):
        """ This function will take value from the slider
            for the blur from 0 to 99 """
        # if no file is chosen
        if self.filename is None:
            self.popup_warning('Please pick an image before trying to adjust the slider values.', "Warning- Pick image")
        # if you clicked open and then cancel, the filename becomes "".
        elif self.filename == "":
            self.popup_warning('Please pick an image before trying to adjust the slider values.', "Warning- Pick image")
        else:
            global nv
            global nvp
            self.noise_value_now = value / 100
            print('Noise: ', self.noise_value_now)
            nv = str(value / 100)
            nvp = str(value)
            self.update()

        # way to go: append all these noise values to a list
        # take the last value from the python list
        # Output the last value to a txt file, brightness value should also be outputted to the same txt file
        # the output file should have same name as the image and should be saved in the same directory as the image as well

    def blur_value(self, value):
        """ This function will take value from the slider
            for the blur from 0 to 99 """
        # if no file is chosen
        if self.filename is None:
            self.popup_warning('Please pick an image before trying to adjust the slider values.', "Warning- Pick image")
        # if you clicked open and then cancel, the filename becomes "".
        elif self.filename == "":
            self.popup_warning('Please pick an image before trying to adjust the slider values.', "Warning- Pick image")
        else:
            global blv
            self.blur_value_now = value
            print('Blur: ', value)
            blv = str(value)
            self.update()

    def changeBrightness(self, img, value):
        """ This function will take an image (img) and the brightness
            value. It will perform the brightness change using OpenCv
            and after split, will merge the img and return it.
        """
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value
        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    def changeBlur(self, img, value):
        """ This function will take the img image and blur values as inputs.
            After perform blur operation using opencv function, it returns
            the image img.
        """
        kernel_size = (value + 1, value + 1)  # +1 is to avoid 0
        img = cv2.blur(img, kernel_size)
        return img

    # noise overlaid over image (addition)
    def salt_pepper_noise(self, image, prob):
        """
        Add salt and pepper noise to image
        prob: Probability of the noise
        """
        output = image.copy()
        if len(image.shape) == 2:
            black = 0
            white = 255
        else:
            colorspace = image.shape[2]
            if colorspace == 3:  # RGB
                black = np.array([0, 0, 0], dtype='uint8')
                white = np.array([255, 255, 255], dtype='uint8')
            else:  # RGBA
                black = np.array([0, 0, 0, 255], dtype='uint8')
                white = np.array([255, 255, 255, 255], dtype='uint8')
        probs = np.random.random(image.shape[:2])
        image[probs < (prob / 2)] = black
        image[probs > 1 - (prob / 2)] = white
        return image

    def update(self):
        """ This function will update the photo according to the
            current values of blur and brightness and set it to photo label.
        """
        img = self.changeBrightness(self.image, self.brightness_value_now)
        img = self.salt_pepper_noise(img, self.noise_value_now)
        img = self.changeBlur(img, self.blur_value_now)
        self.setPhoto(img)

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def savePhoto(self):
        """ This function will save the image"""
        # here provide the output file name
        # lets say we want to save the output as a time stamp
        # uncomment the two lines below

        # import time
        # filename = 'Snapshot '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'

        # Or we can give any name such as output.jpg or output.png as well
        # filename = 'Snapshot.png'

        # Or a much better option is to let user decide the location and the extension
        # using a file dialog.

        # no file name is open in the application, you never even tried clicking open
        if self.filename is None:
            print(self.filename)
            self.popup_warning('Please pick an image before trying to save.', "Warning")
        # you clicked open and then pressed cancel
        elif self.filename == "":
            print(self.filename)
            self.popup_warning('Please pick an image before trying to save.', "Warning")
        # the case where the image is there in the application, if you press save the image and then cancel, the savefilename becomes ""
        elif self.savefilename == "":
            print(self.savefilename)
            self.test_cases()
        # the image file is already saved i.e. a savefilename exists already
        elif self.savefilename is not None:
            print(self.savefilename)
            question1 = QtWidgets.QMessageBox.question(self, "Confirm",
                                                       "Save changes to the same file?",
                                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
                                                       QtWidgets.QMessageBox.Yes)
            if question1 == QtWidgets.QMessageBox.Yes:
                self.save_conditions()  # just save
            elif question1 == QtWidgets.QMessageBox.No:
                self.test_cases()  # save as

        # there is a file open in the application and the file is not saved yet
        else:
            self.test_cases()

    def test_cases(self):
        # open the save dialog
        self.savefilename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[
            0]
        # you clicked cancel after pressing save
        if self.savefilename == "":
            self.popup_warning(
                'Please choose a directory to save the current configuration. Otherwise, all changes to the current image will be lost.',
                "Warning")

        # you never clicked save
        elif self.savefilename is None:
            self.popup_warning(
                'Please choose a directory to save the current configuration. Otherwise, all changes to the current image will be lost.',
                "Warning")

        # you don't click cancel after pressing save
        else:
            self.save_conditions()

    def save_conditions(self):
        try:
            cv2.imwrite(self.savefilename, self.tmp)
            print('Image saved as:', self.savefilename)
            with open(self.savefilename + "_" + 'details.txt', 'w') as f:
            # if bv and nv exist, i.e these variables exist only if the brightness and noise function are called
            # for those function to be called the slider has to be moved
                try:
                    my_bright_text = bv
                    my_noise_text = nv
                    my_noise_pr_text = nvp
                    my_blur_text = blv
                    # Have to add a percentage f.writeline thing as well cause currently the GUI application shows a value from 0 to 100
                    f.write("The brightness value:" + my_bright_text + "\n")
                    f.write("The blur value:" + my_blur_text + "\n")
                    f.writelines("The noise value:" + my_noise_text + "\n")
                    f.writelines("The percentage of noise:" + my_noise_pr_text + "%" + "\n")
                # if slider is not moved, the bv and nv variables don't exist
                # this is basically for saving an image without moving the slider
                except:
                    f.write("The brightness value: 0" + "\n")
                    f.write("The blur value: 0" + "\n")
                    f.writelines("The noise value: 0" + "\n")
                    f.writelines("The percentage of noise: 0" + "\n")
        except:
            self.savefilename = None
            self.popup_critical(
                'Since you are on a Linux/MAC system, you have to specify the image format extension along with the filename.\nFor example,\nsaved_image.jpg')

    def switchFullScreen(self):
        # self.setLayout(self.findLayout("full"))
        # self.show()
        # https://stackoverflow.com/questions/54734244/create-a-full-screen-button-in-pyqt5
        if self.filename is None:
            self.popup_warning('Please pick an image first before trying to go fullscreen.', "Warning- Pick an image")

        elif self.filename == "":
            self.popup_warning('Please pick an image first before trying to go fullscreen.', "Warning- Pick an image")
        else:
            if self.sender().text() == "⛶":
                self.widget.hide()
                self.widget_3.hide()
                self.widget_2.show()
                self.pushButton_4.setText("⛶")
            elif self.pushButton_3.text() == "Fullscreen":
                self.widget.hide()
                self.widget_3.hide()
                self.widget_2.show()
                self.pushButton_4.setText("╬")

        if self.sender().text() == "⛶":
            self.widget.hide()
            self.widget_3.hide()
            self.widget_2.show()
            self.pushButton_4.setText("╬")

        elif self.sender().text() == "╬":
            self.widget.show()
            self.widget_3.show()
            self.widget_2.show()
            self.pushButton_4.setText("⛶")

    def closeEvent(self, event):
        # print("Close clicked")
        # Ask for confirmation
        # https://stackoverflow.com/questions/63798064/pyqt5-closeevent-how-do-i-use-it-correctly

        # if the file is unsaved (you pressed save and then cancel so basically didn't save it) and a file is open
        if self.savefilename == "" and self.filename is not None and self.filename != "":
            answer2 = QtWidgets.QMessageBox.question(self, "Confirm Exit...",
                                                     "Are you sure you want to exit?\nAll changes till now will be lost.",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            event.ignore()
            if answer2 == QtWidgets.QMessageBox.Yes:
                event.accept()

        # if the file is unsaved (there is no savefilename at all, you didn't even try clicking the save button) and a file is open
        elif self.savefilename is None and self.filename is not None and self.filename != "":
            answer2 = QtWidgets.QMessageBox.question(self, "Confirm Exit...",
                                                     "Are you sure you want to exit?\nAll changes till now will be lost.",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            event.ignore()
            if answer2 == QtWidgets.QMessageBox.Yes:
                event.accept()

        # file has been saved, but after saving changes were made. Somehow linking it to slider.
        # Only problem is if both slider values are changed to 0 it doesn't work.
        # Another probelm, even if the file is saved, the popup comes somehow have to track the update function maybe
        elif self.savefilename is not None and self.brightness_value_now != 0 or self.noise_value_now != 0 or self.blur_value_now != 0:
            answer2 = QtWidgets.QMessageBox.question(self, "Confirm Exit...",
                                                     "Are you sure you want to exit?\nOnly the last saved configuration is available.",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            event.ignore()
            if answer2 == QtWidgets.QMessageBox.Yes:
                event.accept()

    def mouseDoubleClickEvent(self, event):
        """ This function detects if image is double-clicked and accordingly presents image in Fullscreen or Default view"""
        if self.pushButton_4.text() == "⛶":
            self.widget.hide()
            self.widget_3.hide()
            self.widget_2.show()
            self.pushButton_4.setText("╬")
        else:
            self.widget.show()
            self.widget_3.show()
            self.widget_2.show()
            self.pushButton_4.setText("⛶")

    def exit_full(self):
        """ This function disables Fullscreen view"""
        if self.pushButton_4.text() == "╬":
            self.widget.show()
            self.widget_3.show()
            self.widget_2.show()
            self.pushButton_4.setText("⛶")

    def full_view(self):
        """ This function enables Fullscreen view"""
        if self.pushButton_4.text() == "⛶":
            self.widget.hide()
            self.widget_3.hide()
            self.widget_2.show()
            self.pushButton_4.setText("╬")

    # Working tested part:

    # image has been saved. but then when we close it without making any changes, since the slider values are not 0, the dialog "do you want to close without saving" still pops up.

    # BUT Here is the PROBLEM! Have to add a case for:
    # 1. If file is saved and then edits are made, then the "are you sure you want to close application" message should come. It is not able to recognize changes to the file as savefilename doesn't change. Somehow maybe have to connect it with slider function.


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/logo_noise.png'))
    ui = MainWindow()
    ui.showMaximized()
    sys.exit(app.exec_())