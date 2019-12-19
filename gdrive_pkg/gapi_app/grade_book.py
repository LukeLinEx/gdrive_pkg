from ..gapi_utils import sservice, dservice

def create_grade_book(name):
    spreadsheet = {
        'properties': {
            'title': name
        }
    }
    spreadsheet = sservice.spreadsheets().create(body=spreadsheet,
                                        fields='spreadsheetId').execute()
    print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
