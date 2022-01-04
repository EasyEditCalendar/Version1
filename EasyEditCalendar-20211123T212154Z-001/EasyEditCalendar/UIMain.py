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

#shift file
from Shift import shift

#for UI
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from qt_material import apply_stylesheet

import mainwindow
import loginMenu

#system imports
import sys
import json
from collections import OrderedDict

#For Encription
from Crypto.Cipher import AES


#deletes token.json to force google login each time
if os.path.exists("token.json"):
    os.remove("token.json")


# Opening JSON file
with open("Storage.json", "r") as inputfile:
 
# returns JSON object as
# a dictionary
    data = json.load(inputfile, object_pairs_hook=OrderedDict)
 
# Iterating through the json
# list


#finds and counts number of lines in file
line_count = 0
for i in data['employees']:
    line_count+=1

#creates array w/ x indexs based on number of employees found
employeesArray = {}
employeesArray[line_count - 1] = employee(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)



line_count = 0
for i in data['shifts']:
    line_count+=1

shiftsArray = {}
empty = []
shiftsArray[line_count - 1] = shift(0, empty, 0, 0)


count = 0

for i in data['employees']:
    print(i)
    availability = i['availability']
    employeesArray[count] = employee(count, i['requestHrs'], i['email'], i['name'], availability[0], availability[1], availability[2], availability[3], availability[4], availability[5], availability[6], availability[7], availability[8], availability[9], availability[10], availability[11], availability[12], availability[13], i['rank'])
    count = count + 1

count = 0

for i in data['shifts']:
    print(i)
    people = i['people']
    shiftsArray[count] = shift(i['numPeople'], people, i['date'], i['start'], i['end'])
    count = count + 1



def writeEmployeeInfo():
            #sets up output for .json file
            output = {
                "employees" : [
                ],
                "shifts" : [
                 ]
            }
            for x in range(0, len(employeesArray) - 1):
                
                output["employees"].append(employeesArray[x].getDictionary())
                print(output)
  

            for x in range(0, len(shiftsArray) - 1):
                
                output["shifts"].append(shiftsArray[x].getDictionary())
                print(output)
            
            # Serializing json 
            json_object = json.dumps(output, indent = 4)
  
            # Writing to sample.json
            with open("Storage.json", "w") as outfile:
                outfile.write(json_object)  



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

        self.main.setWindowTitle("Easy Edit Calendar")
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
        deleteID = self.spinBox_2.value()
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
        self.email.setText(str(employeesArray[valueID].getEmail()))
        self.Name.setText(str(employeesArray[valueID].getName()))
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
    app_width = screen_dimensions.width() * .30
    app_height = screen_dimensions.height() * 0.40
    app_size = QSize(app_width, app_height)
    form.resize(app_size)

    form.setWindowTitle("Easy Edit Calendar")
    form.show()
    
    
    
    app.exec()


# The following checks to make sure this script isn't being called from
# another python script. If it is indeed the main running script,
#  it executes the main function.
if __name__ == '__main__':
    main()
