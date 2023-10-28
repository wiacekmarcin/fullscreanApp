from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

fhome = '/home/marcin/git.devel.marcin/fulscreanapp/fullscreanApp'
ftemp = '/home/marcin/tmp'


def main(name):
    creds = None
    
    if os.path.exists(os.path.join(fhome, name, 'token.json')):
        creds = Credentials.from_authorized_user_file(os.path.join(fhome, name, 'token.json'), SCOPES)
    
    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        dt = datetime.date.today()
        now = datetime.datetime(dt.year, dt.month, dt.day, 0, 0, 0).isoformat() + 'Z'  # 'Z' indicates UTC time
        end = (datetime.datetime.utcnow() + datetime.timedelta(days=800)).isoformat() + 'Z'

        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              timeMax=end, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        fres = open(os.path.join(ftemp, 'calendar_%s.txt' % name), 'w+')
        fres.write("")

        if not events:
            print('No upcoming events found.')

        # Prints the start and name of the next 10 events
        
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            fres.write("%s %s\n" % (start, event['summary']))
        fres.close()

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main('alicja')
    main('marcin')
