#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:07:55 2021

@author: user
"""

from CalendarMain import main, getEvents

#used for GUI
import tkinter as tk 


def refreshEvents():
    newText = getEvents()
    lbl_showEvents["text"] = newText

main()

window = tk.Tk()

window.columnconfigure([0,], minsize=50, weight=1)
window.rowconfigure([0, 1], minsize=50, weight=1)
   
lbl_showEvents = tk.Label(master=window, text="No upcoming events found.")
lbl_showEvents.grid(row=0, column=0)
    
btn_refresh = tk.Button(master=window, text="Refresh Events", command=refreshEvents)
btn_refresh.grid(row=1, column=0, sticky="nsew")
    
refreshEvents()
    
window.mainloop()

    
window.mainloop()