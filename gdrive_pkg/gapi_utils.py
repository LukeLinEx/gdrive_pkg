from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import yaml

mod_path = "/".join(__file__.split("/")[:-2])

with open('{}/config.yaml'.format(mod_path)) as f:
    cred_path = yaml.load(f, Loader=yaml.FullLoader)
    cred_path = cred_path["cred_path"]

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

"""Shows basic usage of the Drive v3 API.
Prints the names and ids of the first 10 files the user has access to.
"""
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('{}/token.pickle'.format(cred_path)):
    with open('{}/token.pickle'.format(cred_path), 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            '{}/credentials.json'.format(cred_path), SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('{}/token.pickle'.format(cred_path), 'wb') as token:
        pickle.dump(creds, token)

dservice = build('drive', 'v3', credentials=creds)
sservice = build('sheets', 'v4', credentials=creds)
