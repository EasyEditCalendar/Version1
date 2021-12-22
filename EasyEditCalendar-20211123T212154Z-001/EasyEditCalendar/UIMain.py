#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:07:55 2021

@author: user
"""

from CalendarMain import *
#getEvents returns recent 10 events in string
#main assiangs logins
#createEvent(name, description, start Time & Date, end Time & Date) this creates a event with these peramitars

import os

#employees file
from Employee import employee

#for UI
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from qt_material import apply_stylesheet
import mainwindow
import loginMenu
import sys


#deletes token.json to force google login each time
if os.path.exists("token.json"):
    os.remove("token.json")


#Open EmployeeSaveFile
read = open("Employees.txt", "r")
#write = open("Employees.txt", "a")



#finds and counts number of lines in file
file = open("Employees.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()

#creates array w/ x indexs based on number of employees found
employeesArray = {}
employeesArray[line_count//18] = employee(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


#read txt file
for x in range(line_count//18):
    tempHr = read.readline().splitlines()
    tempHr = int(tempHr[0])
    
    tempEmail = read.readline().splitlines() 
    tempEmail = str(tempEmail[0])
    
    tempName = read.readline().splitlines() 
    tempName = str(tempName[0])
    
    tempLevel = read.readline().splitlines()
    tempLevel = int(tempLevel[0])
    
    tempMonStart = read.readline().splitlines() 
    tempMonStart = int(tempMonStart[0])
    
    tempMonEnd = read.readline().splitlines() 
    tempMonEnd = int(tempMonEnd[0])
    
    tempTueStart = read.readline().splitlines() 
    tempTueStart = int(tempTueStart[0])
    
    tempTueEnd = read.readline().splitlines() 
    tempTueEnd = int(tempTueEnd[0])
    
    tempWedStart = read.readline().splitlines() 
    tempWedStart = int(tempWedStart[0])
    
    tempWedEnd = read.readline().splitlines() 
    tempWedEnd = int(tempWedEnd[0])
    
    tempThurStart = read.readline().splitlines() 
    tempThurStart = int(tempThurStart[0])
    
    tempThurEnd = read.readline().splitlines() 
    tempThurEnd = int(tempThurEnd[0])
    
    tempFriStart = read.readline().splitlines() 
    tempFriStart = int(tempFriStart[0])
    
    tempFriEnd = read.readline().splitlines() 
    tempFriEnd = int(tempFriEnd[0])
    
    tempSatStart = read.readline().splitlines() 
    tempSatStart = int(tempSatStart[0])
    
    tempSatEnd = read.readline().splitlines() 
    tempSatEnd = int(tempSatEnd[0])
    
    tempSunStart = read.readline().splitlines() 
    tempSunStart = int(tempSunStart[0])
    
    tempSunEnd = read.readline().splitlines() 
    tempSunEnd = int(tempSunEnd[0])
    
   #pass read info to array
    employeesArray[x] = employee(x, tempHr, tempEmail, tempName, tempMonStart, tempMonEnd, tempTueStart, tempTueEnd, tempWedStart, tempWedEnd, tempThurStart, tempThurEnd, tempFriStart, tempFriEnd, tempSatStart, tempSatEnd, tempSunStart, tempSunEnd, tempLevel)




def writeEmployeeInfo():
            print(len(employeesArray) - 1)
            writeFile = open("Employees.txt", "w")
            for x in range(0, len(employeesArray) - 1):
#                tempHr = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getHours()), '\n'])
#                tempEmail = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getEmail()), '\n'])
#                tempName = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getName()), '\n'])
#                tempMonStart = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getLevel()), '\n'])
                
                writeFile.writelines([str(employeesArray[x].getMonStart()), '\n'])
#                tempMonEnd = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getMonEnd()), '\n'])
#                tempTueStart = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getTueStart()), '\n'])
#                tempTueEnd = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getTueEnd()), '\n'])
#                tempWedStart = read.readline().spl        model = QtGui.QStandardItemModel()
                writeFile.writelines([str(employeesArray[x].getWedStart()), '\n'])
#                tempWedEnd = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getWedEnd()), '\n'])
#                tempThurStart = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getThurStart()), '\n'])
#                tempThurEnd = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getThurEnd()), '\n'])
#                tempFriStart = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getFriStart()), '\n'])
#                tempFriEnd = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getFriEnd()), '\n'])
#                tempSatStart = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getSatStart()), '\n'])
#                tempSatEnd = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getSatEnd()), '\n'])
#                tempSunStart = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getSunStart()), '\n'])
#                tempSunEnd = read.readline().splitlines() 
                writeFile.writelines([str(employeesArray[x].getSunEnd()), '\n'])





class LoginWindow(QtWidgets.QMainWindow, loginMenu.Ui_MainWindow):
    def append_message(self, message):
        self.log_window.append(message + '\n')
        self.log_window.verticalScrollBar().setValue(
            self.log_window.verticalScrollBar().maximum())

    def append_error(self, message):
        message = "<br />".join(message.split("\n"))
        self.log_window.append("<font color=\"FireBrick\">{}</font><br>".format(
            message))
        self.log_window.verticalScrollBar().setValue(
            self.log_window.verticalScrollBar().maximum())

    def append_warning(self, message):
        message = "<br />".join(message.split("\n"))
        self.log_window.append("<font color=\"Gold\">{}</font><br>".format(
            message))
        self.log_window.verticalScrollBar().setValue(
            self.log_window.verticalScrollBar().maximum())

    def append_info(self, message):
        message = "<br />".join(message.split("\n"))
        self.log_window.append("<font color=\"White\">{}</font><br>".format(
            message))
        self.log_window.verticalScrollBar().setValue(
            self.log_window.verticalScrollBar().maximum())




    def __init__(self, parent=None):
        
        super(LoginWindow, self).__init__(parent)  
        self.setupUi(self)


        self.GoogleLoginButton.clicked.connect(self.googleLogin)


    def googleLogin(self):
        #gets assigns tokens Etc. A.K.A Login
        login()
        self.main = MyMainAppWindow()




        self.main.show()
        self.close()





class MyMainAppWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def append_message(self, message):
        self.log_window.append(message + '\n')
        self.log_window.verticalScrollBar().setValue(
            self.log_window.verticalScrollBar().maximum())

    def append_error(self, message):
        message = "<br />".join(message.split("\n"))
        self.log_window.append("<font color=\"FireBrick\">{}</font><br>".format(
            message))
        self.log_window.verticalScrollBar().setValue(
            self.log_window.verticalScrollBar().maximum())

    def append_warning(self, message):
        message = "<br />".join(message.split("\n"))
        self.log_window.append("<font color=\"Gold\">{}</font><br>".format(
            message))
        self.log_window.verticalScrollBar().setValue(
            self.log_window.verticalScrollBar().maximum())

    def append_info(self, message):
        message = "<br />".join(message.split("\n"))
        self.log_window.append("<font color=\"White\">{}</font><br>".format(
            message))
        self.log_window.verticalScrollBar().setValue(
            self.log_window.verticalScrollBar().maximum())

    def __init__(self, parent=None):
        super(MyMainAppWindow, self).__init__(parent)  
        self.setupUi(self)


        self.createButton.clicked.connect(self.createEventClicked)
        self.Find.clicked.connect(self.findEmployeeClicked)
        self.SaveButton.clicked.connect(self.saveEmployeeInfo)
        self.pushButton_2.clicked.connect(self.createNewEmployee)
        self.pushButton.clicked.connect(self.deleteEmployee)
        self.listView.clicked.connect(self.updateEmployeeListIndex)
        
        
        self.employeeInfoUpdate()
        
        #Testing View List
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)

        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        
        for i in range(0, len(employeesArray) - 1):
            item = QtGui.QStandardItem(str(i) + ': ' + employeesArray[i].getName())
            model.appendRow(item)
            
            
        #Fix spinbox sizes
        self.spinBox_2.setMaximum(len(employeesArray) - 2)
        self.spinBox_2.setMinimum(0)
        
        self.spinBox.setMaximum(len(employeesArray) - 2)
        self.spinBox.setMinimum(0)


    def updateEmployeeListIndex(self):
        selectedIndex = self.listView.selectedIndexes()
        #print(selectedIndex[0].row())
        self.spinBox_2.setValue(int(selectedIndex[0].row()))
        self.spinBox.setValue(int(selectedIndex[0].row()))
        self.employeeInfoUpdate()

    def set_input_file(self):
        download_path = QStandardPaths.standardLocations(
            QStandardPaths.DownloadLocation)[0]
        options = QFileDialog.Options()
        input_file_path, _ = QFileDialog.getOpenFileName(
            None, "Open", download_path,
            "Excel Workbook (*.xlsx);;All Files (*)",
            options=options)
        if input_file_path == "":
            self.append_message("No input file selected")
        else:
            self.append_message(
                "\"{}\" selected as input spreadsheet.".format(input_file_path))
            self.input_file_path = input_file_path
            self.input_file_entry.setText(input_file_path)

    def createEventClicked(self):
        eventTitle = self.lineTitle.text()
        print(eventTitle)

        eventDescription = self.plainTextDesc.toPlainText()
        print(eventDescription)

        startDate = self.dateTimeStart.dateTime().toString(Qt.ISODate)
        print(startDate)

        endDate = self.dateTimeEnd.dateTime().toString(Qt.ISODate)
        print(endDate)
        
        

        createEvent(eventTitle, eventDescription, startDate, endDate)


    def saveEmployeeInfo(self):
        valueID = self.ID.value()
        
        employeesArray[valueID].setEmail(self.email.displayText())
        employeesArray[valueID].setName(self.Name.displayText())
        employeesArray[valueID].setHours(self.HrsReq.value())
        
        employeesArray[valueID].setMonStart(self.MonStart.time().hour())
        employeesArray[valueID].setMonEnd(self.MonEnd.time().hour())
        
        employeesArray[valueID].setTueStart(self.TueStart.time().hour())
        employeesArray[valueID].setTueEnd(self.TueEnd.time().hour())
        
        employeesArray[valueID].setWedStart(self.WedStart.time().hour())
        employeesArray[valueID].setWedEnd(self.WedEnd.time().hour())
        
        employeesArray[valueID].setThurStart(self.ThurStart.time().hour())
        employeesArray[valueID].setThurEnd(self.ThurEnd.time().hour())
        
        employeesArray[valueID].setFriStart(self.FriStart.time().hour())
        employeesArray[valueID].setFriEnd(self.FriEnd.time().hour())
        
        employeesArray[valueID].setSatStart(self.SatStart.time().hour())
        employeesArray[valueID].setSatEnd(self.SatEnd.time().hour())
        
        employeesArray[valueID].setSunStart(self.SunStart.time().hour())
        employeesArray[valueID].setSunEnd(self.SunEnd.time().hour())
        
        
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        
        for i in range(0, len(employeesArray) - 1):
            item = QtGui.QStandardItem(str(i) + ': ' + employeesArray[i].getName())
            model.appendRow(item)
        
        
        writeEmployeeInfo()


    def findEmployeeClicked(self):  
        self.saveEmployeeInfo()
        self.employeeInfoUpdate()
        
    def createNewEmployee(self):
        #employeesArray.append(employee(len(employeesArray), 0, "Sample@Company.com", "First Last", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4))


        #copy array
        employeesArray2 = {}
        employeesArray2[len(employeesArray)] = employee(int(len(employeesArray)-1), 0, 'Sample@Company.com', 'First Last', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4)

        for x in range(0, len(employeesArray2) - 1):
            print(employeesArray[x].getName())
            employeesArray2[x] = employeesArray[x]
        
        employeesArray.update(employeesArray2)
        
        #print(int(len(employeesArray)-1))
        
        
        
        #Write to files and Save Array
        self.saveEmployeeInfo()
        self.employeeInfoUpdate()
        

        #Update Spin boxes
        self.spinBox.setMaximum(len(employeesArray) - 2)
        self.spinBox.setValue(len(employeesArray) - 2)
        
        self.spinBox_2.setMaximum(len(employeesArray) - 2)
        self.spinBox_2.setValue(len(employeesArray) - 2)
        
        self.findEmployeeClicked()
        self.tabWidget.setCurrentIndex(1)
        
    def deleteEmployee(self):
        deleteID = self.spinBox_2.value() - 1
        for x in range(deleteID, len(employeesArray) - 2):
            employeesArray[x] = employeesArray[x + 1]
            
        del employeesArray[len(employeesArray) - 1]
        
        self.spinBox_2.setMaximum(len(employeesArray) - 2)
        self.spinBox_2.setValue(len(employeesArray) - 2)
        
        self.spinBox.setMaximum(len(employeesArray) - 2)
        self.spinBox.setValue(len(employeesArray) - 2)
        
        self.spinBox.setMaximum(len(employeesArray) - 2)
        self.findEmployeeClicked()
        self.tabWidget.setCurrentIndex(1)
        
    def employeeInfoUpdate(self):
        valueID = self.spinBox.value()
        #print(valueID)
        self.ID.setValue(valueID)
        self.ID.setMinimum(valueID)
        self.ID.setMaximum(valueID)
        self.email.setText(employeesArray[valueID].getEmail())
        self.Name.setText(employeesArray[valueID].getName())
        self.HrsReq.setValue(employeesArray[valueID].getHours())
        
        #Hours 
        tempTime = QTime(employeesArray[valueID].getMonStart(), 0, 0)
        self.MonStart.setTime(tempTime)
        tempTime = QTime(employeesArray[valueID].getMonEnd(), 0, 0)
        self.MonEnd.setTime(tempTime)
        
        tempTime = QTime(employeesArray[valueID].getTueStart(), 0, 0)
        self.TueStart.setTime(tempTime)
        tempTime = QTime(employeesArray[valueID].getTueEnd(), 0, 0)
        self.TueEnd.setTime(tempTime)
        
        tempTime = QTime(employeesArray[valueID].getWedStart(), 0, 0)
        self.WedStart.setTime(tempTime)
        tempTime = QTime(employeesArray[valueID].getWedEnd(), 0, 0)
        self.WedEnd.setTime(tempTime)
        
        tempTime = QTime(employeesArray[valueID].getThurStart(), 0, 0)
        self.ThurStart.setTime(tempTime)
        tempTime = QTime(employeesArray[valueID].getThurEnd(), 0, 0)
        self.ThurEnd.setTime(tempTime)
        
        tempTime = QTime(employeesArray[valueID].getFriStart(), 0, 0)
        self.FriStart.setTime(tempTime)
        tempTime = QTime(employeesArray[valueID].getFriEnd(), 0, 0)
        self.FriEnd.setTime(tempTime)
        
        tempTime = QTime(employeesArray[valueID].getSatStart(), 0, 0)
        self.SatStart.setTime(tempTime)
        tempTime = QTime(employeesArray[valueID].getSatEnd(), 0, 0)
        self.SatEnd.setTime(tempTime)
        
        tempTime = QTime(employeesArray[valueID].getSunStart(), 0, 0)
        self.SunStart.setTime(tempTime)
        tempTime = QTime(employeesArray[valueID].getSunEnd(), 0, 0)
        self.SunEnd.setTime(tempTime)
       

# Loads all the code written above and starts the application.
def main():
    #if not QtWidgets.QApplication.instance():
    #    app = QtWidgets.QApplication(sys.argv)
    #else:
    #    app = QtWidgets.QApplication.instance()
    
    app = QtWidgets.QApplication(sys.argv)
    form = LoginWindow()
    #form = MyMainAppWindow()

    apply_stylesheet(app, theme='dark_blue.xml')

    screen_dimensions = app.primaryScreen().availableGeometry().size()
    app_width = screen_dimensions.width() * 0.40
    app_height = screen_dimensions.height() * 0.60
    app_size = QSize(app_width, app_height)
    #form.resize(app_size)

    form.setWindowTitle("Easy Edit Calendar")
    form.show()
    
    
    
    app.exec()


# The following checks to make sure this script isn't being called from
# another python script. If it is indeed the main running script,
#  it executes the main function.
if __name__ == '__main__':
    main()
