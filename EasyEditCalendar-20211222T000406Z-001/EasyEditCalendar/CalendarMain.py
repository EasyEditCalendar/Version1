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


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def login():
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

    global service
    service = build('calendar', 'v3', credentials=creds)
    
    return service
    # Call the Calendar API
    
        
        
def getEvents():
    service = main()
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    text = 'Upcoming 10 events:'
    #lbl_showEvents["text"] = 'Upcoming 10 events:'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                  maxResults=10, singleEvents=True,
                                  orderBy='startTime').execute()
    events = events_result.get('items', [])
        
    if not events:
        print('No upcoming events found.')
        text = text + '\nNo upcoming events found.'
        #lbl_showEvents["text"] = lbl_showEvents["text"] + '\nNo upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        text = text + '\n' + start + ' ' + event['summary']
        #lbl_showEvents["text"] = lbl_showEvents["text"] + '\n' + start + ' ' + event['summary']
        
    return text

def createEvent(name, desc, startTime, endTime):
    # Refer to the Python quickstart on how to setup the environment:
    # https://developers.google.com/calendar/quickstart/python
    # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
    # stored credentials.
    
    event = {
      'summary': name,
      'description': desc,
      'start': {
        'dateTime': startTime,
        'timeZone': 'America/Chicago',
      },
      'end': {
        'dateTime': endTime,
        'timeZone': 'America/Chicago',
      },
      'reminders': {
        'useDefault': True,
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


def clearCalendar(cal):
    service.calendars().clear(cal).execute()

if __name__ == '__main__':
    login()
