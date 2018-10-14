from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'


def get_service():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
        return build('drive', 'v3', http=creds.authorize(Http()))


def create_folder(foldername, parentid):


def upload_file(filename, folderid):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    sheet_metadata = {
        'name': 'My Report',
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload('BlueMidterm.csv',
                            mimetype='text/csv',
                            resumable=True)
    sheet = service.files().create(body=sheet_metadata,
                                   media_body=media,
                                   fields='id').execute()


if __name__ == '__main__':
    main()
