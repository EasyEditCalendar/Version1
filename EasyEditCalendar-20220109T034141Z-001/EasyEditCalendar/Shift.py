#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:49:27 2021

@author: Andrew R.
"""

#Imports
import os

class shift:
    
    def __init__(self, numPeople, shiftAttend = [], date = 0, Start = 0, End = 0):
        self.numPeople = numPeople
        self.shiftAttend = shiftAttend
        self.start = Start
        self.end = End
        self.date = date
        
        
    #testing Functions
    def getPeople(self):
        return self.shiftAttend
    
    def getPerson(self, personID):
        return self.shiftAttend[personID]
    
    def getNumPeople(self):
        return int(self.numPeople)
    
    def getStart(self):
        return int(self.start)
    
    def getEnd(self):
        return int(self.end)
    
    def getDate(self):
        return int(self.date)
    
    def shiftFull(self):
        if self.numPeople == len(self.shiftAttend):
            return True
        else:
            return False

    def getDictionary(self):
        dictionary = {
                    "numPeople" : int(self.numPeople),
                    "date" : int(self.date),
                    "start" : int(self.start),
                    "end" : int(self.end),
                    "people" : self.shiftAttend
                }
        return dictionary
        
        
    #editing functions
    def addPerson(self, person):
        if self.shiftfull == False:
            workers = len(self.shiftAttend)
            self.shiftAttend[workers] = person