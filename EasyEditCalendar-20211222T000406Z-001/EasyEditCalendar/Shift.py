#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:49:27 2021

@author: Andrew R.
"""

#Imports
import os

class shift:
    
    def __init__(self, numPeople, shiftAttend = [], start, end):
        self.numPeople = numPeople
        self.shiftAttend = shiftAttend
        self.start = start
        self.end = end
        
        
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
        return int(self.End)
    
    def shiftFull(self):
        if self.numPeople == len(self.shiftAttend):
            return True
        else:
            return False
        
        
    #editing functions
    def addPerson(self, person):
        if self.shiftfull == False:
            workers = len(self.shiftAttend)
            self.shiftAttend[workers] = person