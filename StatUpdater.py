import gspread
from oauth2client.service_account import ServiceAccountCredentials
#import pandas as pd
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


class StatUpdater(object):
	def __init__(self, spreadsheet_name):
		result = requests.get("https://www.worldometers.info/coronavirus/")
		src = result.content
		soup= BeautifulSoup(src, 'lxml')
		table = soup.find('table')
		table_rows = table.find_all('tr')
		self.col_countries = 1
		self.col_cases = 2
		self.col_deaths = 3
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		creds = ServiceAccountCredentials.from_json_keyfile_name('CoronavirusTracking.json', scope)
		client = gspread.authorize(creds)
		self.sheet = client.open('CoronavirusTracker').sheet1
		length = len(table_rows)
		mat = []
		rowEdit = []
		cnt = 0
		for tr in table_rows:
			td = tr.find_all('td')
			row = [i.text for i in td]
			if row != [] and cnt <100:
				mat.append(row[1:3]+[row[4]])
				cnt = cnt+1
		#print(mat)
		print("updating spreadsheet")

		count = 1
		cnt = 0
		epoc = 29
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
			self.sheet.update_cell(count,self.col_countries, i[0])
			self.sheet.update_cell(count,self.col_cases, i[1])
			self.sheet.update_cell(count,self.col_deaths, i[2])

statupdate = StatUpdater('CoronavirusTracker')
