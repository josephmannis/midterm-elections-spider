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
    service = get_service()

    folder_metadata = {
        'name': foldername,
        'parents': parentid,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    file = service.files().create(body=file_metadata,
                                  fields='id').execute()

    return file.get('id')


def upload_sheet(filename, folderid):

    sheet_metadata = {
        'name': filename,
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }

    media = MediaFileUpload(filename,
                            mimetype='text/csv',
                            resumable=True)
    sheet = service.files().create(body=sheet_metadata,
                                   media_body=media,
                                   fields='id').execute()


if __name__ == '__main__':
    main()
