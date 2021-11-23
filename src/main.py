#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:26:06 2021

@author: Andrew J. Rohm
"""
from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

#used for GUI
import tkinter as tk 

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    window = tk.Tk()
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    def getEvents():
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        lbl_showEvents["text"] = 'Upcoming 10 events:'
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
        
        if not events:
            print('No upcoming events found.')
            lbl_showEvents["text"] = lbl_showEvents["text"] + '\nNo upcoming events found.'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            lbl_showEvents["text"] = lbl_showEvents["text"] + '\n' + start + ' ' + event['summary']
        
    #Split to UI
    
    window.columnconfigure([0,], minsize=50, weight=1)
    window.rowconfigure([0, 1], minsize=50, weight=1)
   
    lbl_showEvents = tk.Label(master=window, text="No upcoming events found.")
    lbl_showEvents.grid(row=0, column=0)
    
    btn_refresh = tk.Button(master=window, text="Refresh Events", command=getEvents)
    btn_refresh.grid(row=1, column=0, sticky="nsew")
    
    getEvents()
    
    window.mainloop()


if __name__ == '__main__':
    main()