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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDateTimeEdit,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1070, 531)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
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
        self.Employee = QWidget()
        self.Employee.setObjectName(u"Employee")
        self.horizontalLayout_4 = QHBoxLayout(self.Employee)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FindEmployee = QHBoxLayout()
        self.FindEmployee.setObjectName(u"FindEmployee")
        self.Namelabel = QLabel(self.Employee)
        self.Namelabel.setObjectName(u"Namelabel")

        self.FindEmployee.addWidget(self.Namelabel)

        self.Name = QLineEdit(self.Employee)
        self.Name.setObjectName(u"Name")

        self.FindEmployee.addWidget(self.Name)

        self.IDLabel = QLabel(self.Employee)
        self.IDLabel.setObjectName(u"IDLabel")

        self.FindEmployee.addWidget(self.IDLabel)

        self.ID = QSpinBox(self.Employee)
        self.ID.setObjectName(u"ID")
        self.ID.setEnabled(True)
        self.ID.setInputMethodHints(Qt.ImhNone)

        self.FindEmployee.addWidget(self.ID)


        self.verticalLayout.addLayout(self.FindEmployee)

        self.EmployeeInfo = QHBoxLayout()
        self.EmployeeInfo.setSpacing(6)
        self.EmployeeInfo.setObjectName(u"EmployeeInfo")
        self.EmployeeInfo.setContentsMargins(-1, -1, -1, 0)
        self.emailLabel = QLabel(self.Employee)
        self.emailLabel.setObjectName(u"emailLabel")

        self.EmployeeInfo.addWidget(self.emailLabel)

        self.email = QLineEdit(self.Employee)
        self.email.setObjectName(u"email")

        self.EmployeeInfo.addWidget(self.email)

        self.HrsReqLabel = QLabel(self.Employee)
        self.HrsReqLabel.setObjectName(u"HrsReqLabel")

        self.EmployeeInfo.addWidget(self.HrsReqLabel)

        self.HrsReq = QSpinBox(self.Employee)
        self.HrsReq.setObjectName(u"HrsReq")

        self.EmployeeInfo.addWidget(self.HrsReq)


        self.verticalLayout.addLayout(self.EmployeeInfo)

        self.Monday = QHBoxLayout()
        self.Monday.setObjectName(u"Monday")
        self.MonLabel = QLabel(self.Employee)
        self.MonLabel.setObjectName(u"MonLabel")
        self.MonLabel.setMaximumSize(QSize(75, 16777215))

        self.Monday.addWidget(self.MonLabel)

        self.MonStart = QTimeEdit(self.Employee)
        self.MonStart.setObjectName(u"MonStart")

        self.Monday.addWidget(self.MonStart)

        self.MonEnd = QTimeEdit(self.Employee)
        self.MonEnd.setObjectName(u"MonEnd")

        self.Monday.addWidget(self.MonEnd)


        self.verticalLayout.addLayout(self.Monday)

        self.Tuesday = QHBoxLayout()
        self.Tuesday.setObjectName(u"Tuesday")
        self.TueLabel = QLabel(self.Employee)
        self.TueLabel.setObjectName(u"TueLabel")
        self.TueLabel.setMaximumSize(QSize(75, 16777215))

        self.Tuesday.addWidget(self.TueLabel)

        self.TueStart = QTimeEdit(self.Employee)
        self.TueStart.setObjectName(u"TueStart")

        self.Tuesday.addWidget(self.TueStart)

        self.TueEnd = QTimeEdit(self.Employee)
        self.TueEnd.setObjectName(u"TueEnd")

        self.Tuesday.addWidget(self.TueEnd)


        self.verticalLayout.addLayout(self.Tuesday)

        self.Wedsday = QHBoxLayout()
        self.Wedsday.setObjectName(u"Wedsday")
        self.WedLabel = QLabel(self.Employee)
        self.WedLabel.setObjectName(u"WedLabel")
        self.WedLabel.setMaximumSize(QSize(75, 16777215))

        self.Wedsday.addWidget(self.WedLabel)

        self.WedStart = QTimeEdit(self.Employee)
        self.WedStart.setObjectName(u"WedStart")

        self.Wedsday.addWidget(self.WedStart)

        self.WedEnd = QTimeEdit(self.Employee)
        self.WedEnd.setObjectName(u"WedEnd")

        self.Wedsday.addWidget(self.WedEnd)


        self.verticalLayout.addLayout(self.Wedsday)

        self.Thursday = QHBoxLayout()
        self.Thursday.setObjectName(u"Thursday")
        self.ThurLabel = QLabel(self.Employee)
        self.ThurLabel.setObjectName(u"ThurLabel")
        self.ThurLabel.setMaximumSize(QSize(75, 16777215))

        self.Thursday.addWidget(self.ThurLabel)

        self.ThurStart = QTimeEdit(self.Employee)
        self.ThurStart.setObjectName(u"ThurStart")

        self.Thursday.addWidget(self.ThurStart)

        self.ThurEnd = QTimeEdit(self.Employee)
        self.ThurEnd.setObjectName(u"ThurEnd")

        self.Thursday.addWidget(self.ThurEnd)


        self.verticalLayout.addLayout(self.Thursday)

        self.Fri = QHBoxLayout()
        self.Fri.setObjectName(u"Fri")
        self.FriLabel = QLabel(self.Employee)
        self.FriLabel.setObjectName(u"FriLabel")
        self.FriLabel.setMaximumSize(QSize(75, 16777215))

        self.Fri.addWidget(self.FriLabel)

        self.FriStart = QTimeEdit(self.Employee)
        self.FriStart.setObjectName(u"FriStart")

        self.Fri.addWidget(self.FriStart)

        self.FriEnd = QTimeEdit(self.Employee)
        self.FriEnd.setObjectName(u"FriEnd")

        self.Fri.addWidget(self.FriEnd)


        self.verticalLayout.addLayout(self.Fri)

        self.Saturday = QHBoxLayout()
        self.Saturday.setObjectName(u"Saturday")
        self.SatLabel = QLabel(self.Employee)
        self.SatLabel.setObjectName(u"SatLabel")
        self.SatLabel.setMaximumSize(QSize(75, 16777215))

        self.Saturday.addWidget(self.SatLabel)

        self.SatStart = QTimeEdit(self.Employee)
        self.SatStart.setObjectName(u"SatStart")

        self.Saturday.addWidget(self.SatStart)

        self.SatEnd = QTimeEdit(self.Employee)
        self.SatEnd.setObjectName(u"SatEnd")

        self.Saturday.addWidget(self.SatEnd)


        self.verticalLayout.addLayout(self.Saturday)

        self.Sunday = QHBoxLayout()
        self.Sunday.setObjectName(u"Sunday")
        self.SunLabel = QLabel(self.Employee)
        self.SunLabel.setObjectName(u"SunLabel")
        self.SunLabel.setMaximumSize(QSize(75, 16777215))

        self.Sunday.addWidget(self.SunLabel)

        self.SunStart = QTimeEdit(self.Employee)
        self.SunStart.setObjectName(u"SunStart")

        self.Sunday.addWidget(self.SunStart)

        self.SunEnd = QTimeEdit(self.Employee)
        self.SunEnd.setObjectName(u"SunEnd")
        self.SunEnd.setCurrentSection(QDateTimeEdit.HourSection)

        self.Sunday.addWidget(self.SunEnd)


        self.verticalLayout.addLayout(self.Sunday)

        self.UseBox = QHBoxLayout()
        self.UseBox.setObjectName(u"UseBox")
        self.SaveButton = QPushButton(self.Employee)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setMinimumSize(QSize(850, 0))

        self.UseBox.addWidget(self.SaveButton)

        self.spinBox = QSpinBox(self.Employee)
        self.spinBox.setObjectName(u"spinBox")

        self.UseBox.addWidget(self.spinBox)

        self.Find = QPushButton(self.Employee)
        self.Find.setObjectName(u"Find")

        self.UseBox.addWidget(self.Find)


        self.verticalLayout.addLayout(self.UseBox)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.Employee, "")
        self.EmployeeList = QWidget()
        self.EmployeeList.setObjectName(u"EmployeeList")
        self.EmployeeList.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.EmployeeList)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listView = QListView(self.EmployeeList)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_4.addWidget(self.listView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = QPushButton(self.EmployeeList)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.EmployeeList)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.spinBox_2 = QSpinBox(self.EmployeeList)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_5.addWidget(self.spinBox_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.EmployeeList, "")
        self.WeeklyShifts = QWidget()
        self.WeeklyShifts.setObjectName(u"WeeklyShifts")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WeeklyShifts.sizePolicy().hasHeightForWidth())
        self.WeeklyShifts.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.WeeklyShifts)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Days = QVBoxLayout()
        self.Days.setObjectName(u"Days")
        self.ShiftDaysLabel = QLabel(self.WeeklyShifts)
        self.ShiftDaysLabel.setObjectName(u"ShiftDaysLabel")

        self.Days.addWidget(self.ShiftDaysLabel)

        self.ShiftDays = QComboBox(self.WeeklyShifts)
        self.ShiftDays.setObjectName(u"ShiftDays")

        self.Days.addWidget(self.ShiftDays)


        self.horizontalLayout_10.addLayout(self.Days)

        self.StartTime = QVBoxLayout()
        self.StartTime.setObjectName(u"StartTime")
        self.label = QLabel(self.WeeklyShifts)
        self.label.setObjectName(u"label")

        self.StartTime.addWidget(self.label)

        self.StartTimeShift = QTimeEdit(self.WeeklyShifts)
        self.StartTimeShift.setObjectName(u"StartTimeShift")

        self.StartTime.addWidget(self.StartTimeShift)


        self.horizontalLayout_10.addLayout(self.StartTime)

        self.EndTime = QVBoxLayout()
        self.EndTime.setObjectName(u"EndTime")
        self.label_2 = QLabel(self.WeeklyShifts)
        self.label_2.setObjectName(u"label_2")

        self.EndTime.addWidget(self.label_2)

        self.EndTimeShift = QTimeEdit(self.WeeklyShifts)
        self.EndTimeShift.setObjectName(u"EndTimeShift")

        self.EndTime.addWidget(self.EndTimeShift)


        self.horizontalLayout_10.addLayout(self.EndTime)

        self.EmployeesNeeded = QVBoxLayout()
        self.EmployeesNeeded.setObjectName(u"EmployeesNeeded")
        self.Employees = QLabel(self.WeeklyShifts)
        self.Employees.setObjectName(u"Employees")

        self.EmployeesNeeded.addWidget(self.Employees)

        self.EmployeesInShift = QSpinBox(self.WeeklyShifts)
        self.EmployeesInShift.setObjectName(u"EmployeesInShift")

        self.EmployeesNeeded.addWidget(self.EmployeesInShift)


        self.horizontalLayout_10.addLayout(self.EmployeesNeeded)

        self.CreateNewShift = QPushButton(self.WeeklyShifts)
        self.CreateNewShift.setObjectName(u"CreateNewShift")

        self.horizontalLayout_10.addWidget(self.CreateNewShift)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.MondayShifts = QListView(self.WeeklyShifts)
        self.MondayShifts.setObjectName(u"MondayShifts")

        self.horizontalLayout_8.addWidget(self.MondayShifts)

        self.TuesdayShifts = QListView(self.WeeklyShifts)
        self.TuesdayShifts.setObjectName(u"TuesdayShifts")

        self.horizontalLayout_8.addWidget(self.TuesdayShifts)

        self.WedsdayShifts = QListView(self.WeeklyShifts)
        self.WedsdayShifts.setObjectName(u"WedsdayShifts")

        self.horizontalLayout_8.addWidget(self.WedsdayShifts)

        self.ThursdayShifts = QListView(self.WeeklyShifts)
        self.ThursdayShifts.setObjectName(u"ThursdayShifts")

        self.horizontalLayout_8.addWidget(self.ThursdayShifts)

        self.FridayShifts = QListView(self.WeeklyShifts)
        self.FridayShifts.setObjectName(u"FridayShifts")

        self.horizontalLayout_8.addWidget(self.FridayShifts)

        self.SaturdayShifts = QListView(self.WeeklyShifts)
        self.SaturdayShifts.setObjectName(u"SaturdayShifts")

        self.horizontalLayout_8.addWidget(self.SaturdayShifts)

        self.SundayShifts = QListView(self.WeeklyShifts)
        self.SundayShifts.setObjectName(u"SundayShifts")

        self.horizontalLayout_8.addWidget(self.SundayShifts)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.tabWidget.addTab(self.WeeklyShifts, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout_7.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1070, 22))
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
        self.MonStart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.MonEnd.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.TueLabel.setText(QCoreApplication.translate("MainWindow", u"Tuesday:", None))
        self.TueStart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.TueEnd.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.WedLabel.setText(QCoreApplication.translate("MainWindow", u"Wedsday:", None))
        self.WedStart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.WedEnd.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.ThurLabel.setText(QCoreApplication.translate("MainWindow", u"Thursday:", None))
        self.ThurStart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.ThurEnd.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.FriLabel.setText(QCoreApplication.translate("MainWindow", u"Friday:", None))
        self.FriStart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.FriEnd.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.SatLabel.setText(QCoreApplication.translate("MainWindow", u"Saturday:", None))
        self.SatStart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.SatEnd.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.SunLabel.setText(QCoreApplication.translate("MainWindow", u"Sunday:", None))
        self.SunStart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.SunEnd.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Find.setText(QCoreApplication.translate("MainWindow", u"Find Empolyee With ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Employee), QCoreApplication.translate("MainWindow", u"Employees", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Create Employee", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete Employee", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EmployeeList), QCoreApplication.translate("MainWindow", u"Employee List", None))
        self.ShiftDaysLabel.setText(QCoreApplication.translate("MainWindow", u"Day:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start Time:", None))
        self.StartTimeShift.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h AP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End Time:", None))
        self.Employees.setText(QCoreApplication.translate("MainWindow", u"Employees In Shift:", None))
        self.CreateNewShift.setText(QCoreApplication.translate("MainWindow", u"Create New Shift", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WeeklyShifts), QCoreApplication.translate("MainWindow", u"Weekly Shifts", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi

