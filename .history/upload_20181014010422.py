from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload


class ScraperUploader:
    SCOPES = 'https://www.googleapis.com/auth/drive'

    def get_service(self):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
            return build('drive', 'v3', http=creds.authorize(Http()))

    def create_folder(self, foldername, parentfolderid):
        service = self.get_service()

        folder_metadata = {
            'name': foldername,
            'parents': parentfolderid,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = service.files().create(body=folder_metadata,
                                        fields='id').execute()

        return folder.get('id')

    def upload_sheet(self, filename, parentfolderid):
        service = get_service()

        sheet_metadata = {
            'name': filename,
            'parents': parentfolderid,
            'mimeType': 'application/vnd.google-apps.spreadsheet'
        }

        media = MediaFileUpload(filename,
                                mimetype='text/csv',
                                resumable=True)
        sheet = service.files().create(body=sheet_metadata,
                                       media_body=media,
                                       fields='id').execute()
