# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(659, 382)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.OverallTitle = QLabel(self.centralwidget)
        self.OverallTitle.setObjectName(u"OverallTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.OverallTitle.setFont(font)
        self.OverallTitle.setTextFormat(Qt.AutoText)
        self.OverallTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.OverallTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.UserLabel = QLabel(self.centralwidget)
        self.UserLabel.setObjectName(u"UserLabel")

        self.horizontalLayout.addWidget(self.UserLabel)

        self.UserInput = QLineEdit(self.centralwidget)
        self.UserInput.setObjectName(u"UserInput")

        self.horizontalLayout.addWidget(self.UserInput)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PassLabel = QLabel(self.centralwidget)
        self.PassLabel.setObjectName(u"PassLabel")

        self.horizontalLayout_2.addWidget(self.PassLabel)

        self.PassInput = QLineEdit(self.centralwidget)
        self.PassInput.setObjectName(u"PassInput")
        self.PassInput.setText(u"")
        self.PassInput.setFrame(True)
        self.PassInput.setEchoMode(QLineEdit.Password)
        self.PassInput.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.PassInput)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.SavePass = QCheckBox(self.centralwidget)
        self.SavePass.setObjectName(u"SavePass")
        self.SavePass.setLayoutDirection(Qt.LeftToRight)
        self.SavePass.setChecked(False)

        self.horizontalLayout_3.addWidget(self.SavePass)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.LoginButton = QPushButton(self.centralwidget)
        self.LoginButton.setObjectName(u"LoginButton")
        font1 = QFont()
        font1.setPointSize(15)
        self.LoginButton.setFont(font1)

        self.verticalLayout.addWidget(self.LoginButton)

        self.GoogleLoginButton = QPushButton(self.centralwidget)
        self.GoogleLoginButton.setObjectName(u"GoogleLoginButton")
        self.GoogleLoginButton.setMaximumSize(QSize(190, 50))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(66, 133, 244, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(227, 227, 227, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(160, 160, 160, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        brush5 = QBrush(QColor(240, 240, 240, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush5)
        brush6 = QBrush(QColor(105, 105, 105, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(0, 120, 215, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        brush8 = QBrush(QColor(0, 0, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        brush10 = QBrush(QColor(245, 245, 245, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush)
        brush11 = QBrush(QColor(255, 255, 220, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush10)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        brush14 = QBrush(QColor(120, 120, 120, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        brush15 = QBrush(QColor(247, 247, 247, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush16)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.GoogleLoginButton.setPalette(palette)
        font2 = QFont()
        font2.setBold(True)
        self.GoogleLoginButton.setFont(font2)
        icon = QIcon()
        icon.addFile(u"btn_google_signin_dark_pressed_ios@3x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GoogleLoginButton.setIcon(icon)
        self.GoogleLoginButton.setIconSize(QSize(200, 200))

        self.verticalLayout.addWidget(self.GoogleLoginButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.RightToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.OverallTitle.setText(QCoreApplication.translate("MainWindow", u"Easy Edit Calendar", None))
        self.UserLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.PassLabel.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.SavePass.setText(QCoreApplication.translate("MainWindow", u"Save Password", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.GoogleLoginButton.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

