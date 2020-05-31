import gspread
from oauth2client.service_account import ServiceAccountCredentials
#import pandas as pd
import requests
import urllib.request
import schedule
import time
from bs4 import BeautifulSoup


currday = 0
class AutoStatUpdater(object):
	mat = []
	col_countries = 1
	col_total_cases = 2
	col_total_deaths = 3
		#print(mat)

	def grabdata():
		global mat
		result = requests.get("https://www.worldometers.info/coronavirus/")
		src = result.content
		soup= BeautifulSoup(src, 'lxml')
		table = soup.find('table')
		table_rows = table.find_all('tr')
		
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		creds = ServiceAccountCredentials.from_json_keyfile_name('CoronavirusTracking.json', scope)
		client = gspread.authorize(creds)
		sheet = client.open('CoronavirusTracker').sheet1
		length = len(table_rows)
		mat = []
		rowEdit = []
		for tr in table_rows:
			td = tr.find_all('td')
			row = [i.text for i in td]
			if row != []:
				row[3] = row[3].replace('+','')
				row[5] = row[5].replace('+','')
				mat.append(row[1:3] + [row[4]] + [row[3]] + [row[5]])
		print("updating spreadsheet")
		global currday
		currday = currday + 1
		col_countries = 1
		col_total_cases = 2
		col_total_deaths = 3
		col_new_cases = 3 + 2*currday	
		col_new_deaths = 4 + 2*currday
		epoc = 15
		count = 1
		cnt = 0
		if mat!=[]:
			for i in mat:
				if cnt%epoc==0:
					if cnt!=0:
						print("100s sleep starting: part " + str(int(cnt/epoc)) + " updated")
					else:
						print("100s sleep starting: ensuring update doesnt overlap with API restrictions")
					time.sleep(100)
					print("100s sleep done: updating part " + str(1+int(cnt/epoc)))
				count = count + 1
				cnt = cnt + 1
				sheet.update_cell(count, col_countries, i[0])
				sheet.update_cell(count, col_total_cases, i[1])
				sheet.update_cell(count, col_total_deaths, i[2])
				sheet.update_cell(count, col_new_cases, i[3])
				sheet.update_cell(count, col_new_deaths, i[4])

	schedule.every().day.at("16:50").do(grabdata)

	while True:
		schedule.run_pending()
		time.sleep(1)