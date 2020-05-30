import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('CoronavirusTracking.json', scope)

client = gspread.authorize(creds)

sheet = client.open('CoronavirusTracker').sheet1

stuff = sheet.get_all_records()

print(stuff)