# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDateTimeEdit, QHBoxLayout,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1072, 531)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMovable(True)
        self.createEventTab = QWidget()
        self.createEventTab.setObjectName(u"createEventTab")
        self.horizontalLayout_3 = QHBoxLayout(self.createEventTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.calendarWidget = QCalendarWidget(self.createEventTab)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.horizontalLayout.addWidget(self.calendarWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineTitle = QLineEdit(self.createEventTab)
        self.lineTitle.setObjectName(u"lineTitle")

        self.verticalLayout_3.addWidget(self.lineTitle)

        self.plainTextDesc = QPlainTextEdit(self.createEventTab)
        self.plainTextDesc.setObjectName(u"plainTextDesc")

        self.verticalLayout_3.addWidget(self.plainTextDesc)

        self.dateTimeStart = QDateTimeEdit(self.createEventTab)
        self.dateTimeStart.setObjectName(u"dateTimeStart")
        self.dateTimeStart.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.dateTimeStart)

        self.dateTimeEnd = QDateTimeEdit(self.createEventTab)
        self.dateTimeEnd.setObjectName(u"dateTimeEnd")
        self.dateTimeEnd.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.dateTimeEnd)

        self.createButton = QPushButton(self.createEventTab)
        self.createButton.setObjectName(u"createButton")

        self.verticalLayout_3.addWidget(self.createButton)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.createEventTab, "")
        self.EmployeeTab = QWidget()
        self.EmployeeTab.setObjectName(u"EmployeeTab")
        self.horizontalLayout_4 = QHBoxLayout(self.EmployeeTab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FindEmployee = QHBoxLayout()
        self.FindEmployee.setObjectName(u"FindEmployee")
        self.Namelabel = QLabel(self.EmployeeTab)
        self.Namelabel.setObjectName(u"Namelabel")

        self.FindEmployee.addWidget(self.Namelabel)

        self.Name = QLineEdit(self.EmployeeTab)
        self.Name.setObjectName(u"Name")

        self.FindEmployee.addWidget(self.Name)

        self.IDLabel = QLabel(self.EmployeeTab)
        self.IDLabel.setObjectName(u"IDLabel")

        self.FindEmployee.addWidget(self.IDLabel)

        self.ID = QSpinBox(self.EmployeeTab)
        self.ID.setObjectName(u"ID")
        self.ID.setEnabled(True)
        self.ID.setInputMethodHints(Qt.ImhNone)

        self.FindEmployee.addWidget(self.ID)


        self.verticalLayout.addLayout(self.FindEmployee)

        self.EmployeeInfo = QHBoxLayout()
        self.EmployeeInfo.setSpacing(6)
        self.EmployeeInfo.setObjectName(u"EmployeeInfo")
        self.EmployeeInfo.setContentsMargins(-1, -1, -1, 0)
        self.emailLabel = QLabel(self.EmployeeTab)
        self.emailLabel.setObjectName(u"emailLabel")

        self.EmployeeInfo.addWidget(self.emailLabel)

        self.email = QLineEdit(self.EmployeeTab)
        self.email.setObjectName(u"email")

        self.EmployeeInfo.addWidget(self.email)

        self.HrsReqLabel = QLabel(self.EmployeeTab)
        self.HrsReqLabel.setObjectName(u"HrsReqLabel")

        self.EmployeeInfo.addWidget(self.HrsReqLabel)

        self.HrsReq = QSpinBox(self.EmployeeTab)
        self.HrsReq.setObjectName(u"HrsReq")

        self.EmployeeInfo.addWidget(self.HrsReq)


        self.verticalLayout.addLayout(self.EmployeeInfo)

        self.Monday = QHBoxLayout()
        self.Monday.setObjectName(u"Monday")
        self.MonLabel = QLabel(self.EmployeeTab)
        self.MonLabel.setObjectName(u"MonLabel")
        self.MonLabel.setMaximumSize(QSize(75, 16777215))

        self.Monday.addWidget(self.MonLabel)

        self.MonStart = QTimeEdit(self.EmployeeTab)
        self.MonStart.setObjectName(u"MonStart")

        self.Monday.addWidget(self.MonStart)

        self.MonEnd = QTimeEdit(self.EmployeeTab)
        self.MonEnd.setObjectName(u"MonEnd")

        self.Monday.addWidget(self.MonEnd)


        self.verticalLayout.addLayout(self.Monday)

        self.Tuesday = QHBoxLayout()
        self.Tuesday.setObjectName(u"Tuesday")
        self.TueLabel = QLabel(self.EmployeeTab)
        self.TueLabel.setObjectName(u"TueLabel")
        self.TueLabel.setMaximumSize(QSize(75, 16777215))

        self.Tuesday.addWidget(self.TueLabel)

        self.TueStart = QTimeEdit(self.EmployeeTab)
        self.TueStart.setObjectName(u"TueStart")

        self.Tuesday.addWidget(self.TueStart)

        self.TueEnd = QTimeEdit(self.EmployeeTab)
        self.TueEnd.setObjectName(u"TueEnd")

        self.Tuesday.addWidget(self.TueEnd)


        self.verticalLayout.addLayout(self.Tuesday)

        self.Wedsday = QHBoxLayout()
        self.Wedsday.setObjectName(u"Wedsday")
        self.WedLabel = QLabel(self.EmployeeTab)
        self.WedLabel.setObjectName(u"WedLabel")
        self.WedLabel.setMaximumSize(QSize(75, 16777215))

        self.Wedsday.addWidget(self.WedLabel)

        self.WedStart = QTimeEdit(self.EmployeeTab)
        self.WedStart.setObjectName(u"WedStart")

        self.Wedsday.addWidget(self.WedStart)

        self.WedEnd = QTimeEdit(self.EmployeeTab)
        self.WedEnd.setObjectName(u"WedEnd")

        self.Wedsday.addWidget(self.WedEnd)


        self.verticalLayout.addLayout(self.Wedsday)

        self.Thursday = QHBoxLayout()
        self.Thursday.setObjectName(u"Thursday")
        self.ThurLabel = QLabel(self.EmployeeTab)
        self.ThurLabel.setObjectName(u"ThurLabel")
        self.ThurLabel.setMaximumSize(QSize(75, 16777215))

        self.Thursday.addWidget(self.ThurLabel)

        self.ThurStart = QTimeEdit(self.EmployeeTab)
        self.ThurStart.setObjectName(u"ThurStart")

        self.Thursday.addWidget(self.ThurStart)

        self.ThurEnd = QTimeEdit(self.EmployeeTab)
        self.ThurEnd.setObjectName(u"ThurEnd")

        self.Thursday.addWidget(self.ThurEnd)


        self.verticalLayout.addLayout(self.Thursday)

        self.Fri = QHBoxLayout()
        self.Fri.setObjectName(u"Fri")
        self.FriLabel = QLabel(self.EmployeeTab)
        self.FriLabel.setObjectName(u"FriLabel")
        self.FriLabel.setMaximumSize(QSize(75, 16777215))

        self.Fri.addWidget(self.FriLabel)

        self.FriStart = QTimeEdit(self.EmployeeTab)
        self.FriStart.setObjectName(u"FriStart")

        self.Fri.addWidget(self.FriStart)

        self.FriEnd = QTimeEdit(self.EmployeeTab)
        self.FriEnd.setObjectName(u"FriEnd")

        self.Fri.addWidget(self.FriEnd)


        self.verticalLayout.addLayout(self.Fri)

        self.Saturday = QHBoxLayout()
        self.Saturday.setObjectName(u"Saturday")
        self.SatLabel = QLabel(self.EmployeeTab)
        self.SatLabel.setObjectName(u"SatLabel")
        self.SatLabel.setMaximumSize(QSize(75, 16777215))

        self.Saturday.addWidget(self.SatLabel)

        self.SatStart = QTimeEdit(self.EmployeeTab)
        self.SatStart.setObjectName(u"SatStart")

        self.Saturday.addWidget(self.SatStart)

        self.SatEnd = QTimeEdit(self.EmployeeTab)
        self.SatEnd.setObjectName(u"SatEnd")

        self.Saturday.addWidget(self.SatEnd)


        self.verticalLayout.addLayout(self.Saturday)

        self.Sunday = QHBoxLayout()
        self.Sunday.setObjectName(u"Sunday")
        self.SunLabel = QLabel(self.EmployeeTab)
        self.SunLabel.setObjectName(u"SunLabel")
        self.SunLabel.setMaximumSize(QSize(75, 16777215))

        self.Sunday.addWidget(self.SunLabel)

        self.SunStart = QTimeEdit(self.EmployeeTab)
        self.SunStart.setObjectName(u"SunStart")

        self.Sunday.addWidget(self.SunStart)

        self.SunEnd = QTimeEdit(self.EmployeeTab)
        self.SunEnd.setObjectName(u"SunEnd")

        self.Sunday.addWidget(self.SunEnd)


        self.verticalLayout.addLayout(self.Sunday)

        self.UseBox = QHBoxLayout()
        self.UseBox.setObjectName(u"UseBox")
        self.SaveButton = QPushButton(self.EmployeeTab)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setMinimumSize(QSize(850, 0))

        self.UseBox.addWidget(self.SaveButton)

        self.spinBox = QSpinBox(self.EmployeeTab)
        self.spinBox.setObjectName(u"spinBox")

        self.UseBox.addWidget(self.spinBox)

        self.Find = QPushButton(self.EmployeeTab)
        self.Find.setObjectName(u"Find")

        self.UseBox.addWidget(self.Find)


        self.verticalLayout.addLayout(self.UseBox)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.EmployeeTab, "")
        self.employeeListTab = QWidget()
        self.employeeListTab.setObjectName(u"employeeListTab")
        self.verticalLayoutWidget = QWidget(self.employeeListTab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 9, 1031, 441))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.verticalLayoutWidget)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_2.addWidget(self.listView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.spinBox_2 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.spinBox_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.employeeListTab, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1072, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineTitle.setText(QCoreApplication.translate("MainWindow", u"Event Title", None))
        self.plainTextDesc.setPlainText(QCoreApplication.translate("MainWindow", u"Event Description", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createEventTab), QCoreApplication.translate("MainWindow", u"Event Creation", None))
        self.Namelabel.setText(QCoreApplication.translate("MainWindow", u"Employee Name:", None))
        self.IDLabel.setText(QCoreApplication.translate("MainWindow", u"Employee ID Num:", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.HrsReqLabel.setText(QCoreApplication.translate("MainWindow", u"Weekly Hours Requested:", None))
        self.MonLabel.setText(QCoreApplication.translate("MainWindow", u"Monday:", None))
        self.TueLabel.setText(QCoreApplication.translate("MainWindow", u"Tuesday:", None))
        self.WedLabel.setText(QCoreApplication.translate("MainWindow", u"Wedsday:", None))
        self.ThurLabel.setText(QCoreApplication.translate("MainWindow", u"Thursday:", None))
        self.FriLabel.setText(QCoreApplication.translate("MainWindow", u"Friday:", None))
        self.SatLabel.setText(QCoreApplication.translate("MainWindow", u"Saturday:", None))
        self.SunLabel.setText(QCoreApplication.translate("MainWindow", u"Sunday:", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Find.setText(QCoreApplication.translate("MainWindow", u"Find Empolyee With ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EmployeeTab), QCoreApplication.translate("MainWindow", u"Employee Info Edit", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Create Employee", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete Employee", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.employeeListTab), QCoreApplication.translate("MainWindow", u"Employee List", None))
    # retranslateUi

