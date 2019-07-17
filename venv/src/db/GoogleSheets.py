from __future__ import print_function

import os.path
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

signup_sheet_id = "1-RmPRj6BYUaIiS3czcyhPRnBP6BFRQAuW16IZ4C46Yw"
signup_sheet_range = "Form Responses 1!A2:X"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


# Authentication for google sheets
def auth():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    picklePath = "venv/resources/token.pickle"
    credentialsPath = "venv/resources/credentials.json"
    if os.path.exists(picklePath):
        with open(picklePath, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentialsPath, SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(picklePath, 'wb') as token:
            pickle.dump(creds, token)
    return creds

# Fetches the signup sheet from google sheets
def getSheet():
    creds = auth()
    service = build("sheets", "v4", credentials=creds)

    # Call sheets api
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=signup_sheet_id, range=signup_sheet_range).execute()
    values = result.get("values", [])

    if not values:
        print("No data found")
    else:
        return values

# Parses the spreadsheet values from the google sheet import
# and builds Participant, Runner, and Volunteer objects
def parseValues(values):
    print("Values:")
    print(values)


if __name__ == "__main__":
    values = getSheet()
    parseValues(values)