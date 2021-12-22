#Imports
import os


#start Employee Class
class employee:

    #defaults
    def __init__(self, ID, Hr, email, name, monStart, monEnd, tueStart, tueEnd, wedStart, wedEnd, thurStart, thurEnd, friStart, friEnd, satStart, satEnd, sunStart, sunEnd, level):
        #base Info
        self.ID=ID
        self.Hr=Hr
        self.email=email
        self.name=str(name)
        self.level=level

        #Availiabity
        self.monStart=monStart
        self.monEnd=monEnd

        self.tueStart=tueStart
        self.tueEnd=tueEnd

        self.wedStart=wedStart
        self.wedEnd=wedEnd

        self.thurStart=thurStart
        self.thurEnd=thurEnd

        self.friStart=friStart
        self.friEnd=friEnd

        self.satStart=satStart
        self.satEnd=satEnd

        self.sunStart=sunStart
        self.sunEnd=sunEnd
    
    #testing
    
    #Starts with mon at 0, tue at 1 etc
    def isAvailable(self, weekDay, timeStart, timeEnd):
        if (weekDay==0):
            if ((timeStart>=self.monStart) and (timeEnd<=self.monEnd)):
                return 1
            else:
                return 0
        elif (weekDay==1):
            if ((timeStart>=self.tueStart) and (timeEnd<=self.tueEnd)):
                return 1
            else:
                return 0
        elif (weekDay==2):
            if ((timeStart>=self.wedStart) and (timeEnd<=self.wedEnd)):
                return 1
            else:
                return 0
        elif (weekDay==3):
            if ((timeStart>=self.thurStart) and (timeEnd<=self.thurEnd)):
                return 1
            else:
                return 0
        elif (weekDay==4):
            if ((timeStart>=self.friStart) and (timeEnd<=self.friEnd)):
                return 1
            else:
                return 0
        elif (weekDay==5):
            if ((timeStart>=self.satStart) and (timeEnd<=self.satEnd)):
                return 1
            else:
                return 0
        elif (weekDay==6):
            if ((timeStart>=self.sunStart) and (timeEnd<=self.sunEnd)):
                return 1
            else:
                return 0
            
        return 0
    
    
    #return functions
    #employee.getID()
    def getID(self):
        return self.ID

    def getHours(self):
        return self.Hr

    def getEmail(self):
    
        # return string  
        return self.email 

    def getName(self):
        return self.name
    
    def getLevel(self):
        return self.level

    def getMonStart(self):
        return self.monStart

    def getMonEnd(self):
        return self.monEnd

    def getTueStart(self):
        return self.tueStart

    def getTueEnd(self):
        return self.tueEnd

    def getWedStart(self):
        return self.wedStart

    def getWedEnd(self):
        return self.wedEnd

    def getThurStart(self):
        return self.thurStart

    def getThurEnd(self):
        return self.thurEnd

    def getFriStart(self):
        return self.friStart

    def getFriEnd(self):
        return self.friEnd

    def getSatStart(self):
        return self.satStart

    def getSatEnd(self):
        return self.satEnd

    def getSunStart(self):
        return self.sunStart

    def getSunEnd(self):
        return self.sunEnd
    
    
    #Set Methods
    def setHours(self, newHours):
        self.Hr = newHours
    
    def setEmail(self, newEmail):
        self.email = newEmail

    def setName(self, newName):
        self.name = newName
        
    def setLevel(self, newLevel):
        self.level = newLevel

    def setMonStart(self, newMonStart):
        self.monStart = newMonStart

    def setMonEnd(self, newMonEnd):
        self.monEnd = newMonEnd

    def setTueStart(self, newTueStart):
        self.tueStart = newTueStart

    def setTueEnd(self, newTueEnd):
        self.tueEnd = newTueEnd

    def setWedStart(self, newWedStart):
        self.wedStart = newWedStart

    def setWedEnd(self, newWedEnd):
        self.wedEnd = newWedEnd

    def setThurStart(self, newThurStart):
        self.thurStart = newThurStart

    def setThurEnd(self, newThurEnd):
        self.thurEnd = newThurEnd

    def setFriStart(self, newFriStart):
        self.friStart = newFriStart

    def setFriEnd(self, newFriEnd):
        self.friEnd = newFriEnd

    def setSatStart(self, newSatStart):
        self.satStart = newSatStart

    def setSatEnd(self, newSatEnd):
        self.satEnd = newSatEnd

    def setSunStart(self, newSunStart):
        self.sunStart = newSunStart

    def setSunEnd(self, newSunEnd):
        self.sunEnd = newSunEnd
    
#Open EmployeeSaveFile
#read = open("Employees.txt", "r")
#write = open("Employees.txt", "a")



#finds and counts number of lines in file
#file = open("Employees.txt", "r")
#line_count = 0
#for line in file:
#    if line != "\n":
#        line_count += 1
#file.close()

#creates array w/ x indexs based on number of employees found
#employeesArray = {}
#employeesArray[line_count//17] = employee(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

#for x in range(line_count//17):
#    tempHr = read.readline().splitlines() 
#    tempEmail = read.readline().splitlines() 
#    tempName = read.readline().splitlines() 
#    tempMonStart = read.readline().splitlines() 
#    tempMonEnd = read.readline().splitlines() 
#    tempTueStart = read.readline().splitlines() 
#    tempTueEnd = read.readline().splitlines() 
#    tempWedStart = read.readline().splitlines() 
#    tempWedEnd = read.readline().splitlines() 
#    tempThurStart = read.readline().splitlines() 
#    tempThurEnd = read.readline().splitlines() 
#    tempFriStart = read.readline().splitlines() 
#    tempFriEnd = read.readline().splitlines() 
#    tempSatStart = read.readline().splitlines() 
#    tempSatEnd = read.readline().splitlines() 
#    tempSunStart = read.readline().splitlines() 
#    tempSunEnd = read.readline().splitlines() 
#    employeesArray[x] = employee(x, tempHr, tempEmail, tempName, tempMonStart, tempMonEnd, tempTueStart, tempTueEnd, tempWedStart, tempWedEnd, tempThurStart, tempThurEnd, tempFriStart, tempFriEnd, tempSatStart, tempSatEnd, tempSunStart, tempSunEnd)